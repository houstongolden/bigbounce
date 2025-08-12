#!/usr/bin/env python3
"""
Galaxy Spin Asymmetry Hierarchical Bayesian Fit
Using Stan for MCMC sampling
"""

import numpy as np
import pandas as pd
import stan
import arviz as az
import matplotlib.pyplot as plt
from pathlib import Path

# Stan model code
STAN_CODE = """
data {
  int<lower=1> S;                 // number of surveys
  int<lower=1> B;                 // total bins across all surveys
  int<lower=1> s_of_bin[B];       // survey index per bin
  vector[B] z;                    // redshift centers
  int<lower=0> N_cw[B];           // clockwise counts
  int<lower=0> N_ccw[B];          // counter-clockwise counts
  vector<lower=0, upper=1>[B] b;  // selection weights per bin (input)
  real<lower=0> sigma_delta;      // prior width for survey offsets
}

parameters {
  real<lower=0, upper=0.02> A0;
  real<lower=0, upper=2> p;
  real<lower=0, upper=2> q;
  vector[S] delta;                // survey offsets
  vector<lower=0, upper=0.5>[S] eps; // label-noise per survey
}

transformed parameters {
  vector[B] A_z;
  vector[B] pi_raw;
  vector[B] pi_corr;
  
  A_z = A0 * pow(1 + z, -p) .* exp(-q * z);
  
  for (i in 1:B) {
    pi_raw[i]  = 0.5 * (1 + delta[s_of_bin[i]] + b[i] * A_z[i]);
    // label-noise mixing: with prob eps, flip labels
    pi_corr[i] = (1 - eps[s_of_bin[i]]) * pi_raw[i] + eps[s_of_bin[i]] * (1 - pi_raw[i]);
  }
}

model {
  // Priors
  delta ~ normal(0, sigma_delta);
  eps ~ beta(2, 20);  // Prior expectation ~0.09, concentrated < 0.2
  
  // Likelihood
  for (i in 1:B) {
    int N = N_cw[i] + N_ccw[i];
    N_cw[i] ~ binomial(N, fmin(fmax(pi_corr[i], 1e-6), 1 - 1e-6));
  }
}

generated quantities {
  // For posterior predictive checks
  vector[B] A_post = A_z;
  int N_cw_pred[B];
  
  for (i in 1:B) {
    int N = N_cw[i] + N_ccw[i];
    N_cw_pred[i] = binomial_rng(N, pi_corr[i]);
  }
}
"""

def load_spin_data(csv_path):
    """Load and validate galaxy spin data."""
    df = pd.read_csv(csv_path)
    
    # Validate columns
    required = ['z_bin_center', 'N_cw', 'N_ccw', 'survey_id', 'b_weight']
    assert all(col in df.columns for col in required), f"Missing columns: {set(required) - set(df.columns)}"
    
    # Validate values
    assert (df['N_cw'] >= 0).all() and (df['N_ccw'] >= 0).all(), "Negative counts"
    assert df['b_weight'].between(0, 1).all(), "Invalid weights"
    
    # Convert survey_id to numeric
    df['survey_idx'] = pd.Categorical(df['survey_id']).codes
    
    return df

def prepare_stan_data(df, sigma_delta=0.02):
    """Prepare data dictionary for Stan."""
    return {
        'S': df['survey_id'].nunique(),
        'B': len(df),
        's_of_bin': df['survey_idx'].values + 1,  # Stan uses 1-based indexing
        'z': df['z_bin_center'].values,
        'N_cw': df['N_cw'].values.astype(int),
        'N_ccw': df['N_ccw'].values.astype(int),
        'b': df['b_weight'].values,
        'sigma_delta': sigma_delta
    }

def run_mcmc(data, n_chains=4, n_samples=2000, n_warmup=1000):
    """Run Stan MCMC sampling."""
    model = stan.build(STAN_CODE, data=data)
    fit = model.sample(num_chains=n_chains, num_samples=n_samples, num_warmup=n_warmup)
    return fit

def extract_results(fit, df):
    """Extract and summarize results."""
    # Convert to ArviZ for easier analysis
    idata = az.from_pystan(fit)
    
    # Parameter summary
    params = ['A0', 'p', 'q']
    summary = az.summary(idata, var_names=params)
    
    # Extract posterior samples
    A0_samples = idata.posterior['A0'].values.flatten()
    p_samples = idata.posterior['p'].values.flatten()
    q_samples = idata.posterior['q'].values.flatten()
    
    # Calculate A(z) for a grid of redshifts
    z_grid = np.linspace(0, 3, 100)
    A_z_samples = np.array([
        A0_samples[i] * (1 + z_grid)**(-p_samples[i]) * np.exp(-q_samples[i] * z_grid)
        for i in range(len(A0_samples))
    ])
    
    # Percentiles
    A_z_median = np.percentile(A_z_samples, 50, axis=0)
    A_z_p16 = np.percentile(A_z_samples, 16, axis=0)
    A_z_p84 = np.percentile(A_z_samples, 84, axis=0)
    
    return {
        'summary': summary,
        'idata': idata,
        'z_grid': z_grid,
        'A_z_median': A_z_median,
        'A_z_p16': A_z_p16,
        'A_z_p84': A_z_p84
    }

def plot_results(results, df, output_path):
    """Create diagnostic plots."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. A(z) with data
    ax = axes[0, 0]
    z_grid = results['z_grid']
    ax.fill_between(z_grid, results['A_z_p16'], results['A_z_p84'], 
                    alpha=0.3, label='68% CI')
    ax.plot(z_grid, results['A_z_median'], 'b-', label='Median')
    
    # Add binned data
    for _, row in df.iterrows():
        A_obs = (row['N_cw'] - row['N_ccw']) / (row['N_cw'] + row['N_ccw'])
        A_err = np.sqrt(4 * row['N_cw'] * row['N_ccw']) / (row['N_cw'] + row['N_ccw'])**1.5
        ax.errorbar(row['z_bin_center'], A_obs, yerr=A_err, fmt='o', alpha=0.6)
    
    ax.set_xlabel('Redshift z')
    ax.set_ylabel('Asymmetry A(z)')
    ax.legend()
    ax.set_title('Galaxy Spin Asymmetry vs Redshift')
    
    # 2. Parameter posteriors
    ax = axes[0, 1]
    idata = results['idata']
    az.plot_posterior(idata, var_names=['A0', 'p', 'q'], ax=ax)
    
    # 3. Trace plots
    ax = axes[1, 0]
    az.plot_trace(idata, var_names=['A0'], ax=[ax])
    
    # 4. Posterior predictive check
    ax = axes[1, 1]
    N_cw_pred = idata.posterior_predictive['N_cw_pred'].values.reshape(-1, len(df))
    N_cw_obs = df['N_cw'].values
    
    # Plot predicted vs observed
    pred_mean = N_cw_pred.mean(axis=0)
    pred_std = N_cw_pred.std(axis=0)
    ax.errorbar(N_cw_obs, pred_mean, yerr=pred_std, fmt='o', alpha=0.6)
    ax.plot([N_cw_obs.min(), N_cw_obs.max()], 
            [N_cw_obs.min(), N_cw_obs.max()], 'k--', label='Perfect agreement')
    ax.set_xlabel('Observed N_cw')
    ax.set_ylabel('Predicted N_cw')
    ax.legend()
    ax.set_title('Posterior Predictive Check')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

def save_results(results, output_dir):
    """Save results to CSV files."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Parameter summary
    results['summary'].to_csv(output_dir / 'parameter_summary.csv')
    
    # A(z) posterior
    az_df = pd.DataFrame({
        'z': results['z_grid'],
        'A_median': results['A_z_median'],
        'A_p16': results['A_z_p16'],
        'A_p84': results['A_z_p84']
    })
    az_df.to_csv(output_dir / 'A_z_posterior.csv', index=False)
    
    # Full posterior samples (subset for file size)
    n_save = min(1000, len(results['idata'].posterior['A0'].values.flatten()))
    samples_df = pd.DataFrame({
        'A0': results['idata'].posterior['A0'].values.flatten()[:n_save],
        'p': results['idata'].posterior['p'].values.flatten()[:n_save],
        'q': results['idata'].posterior['q'].values.flatten()[:n_save]
    })
    samples_df.to_csv(output_dir / 'posterior_samples.csv', index=False)

def main():
    """Run the full analysis pipeline."""
    # Configuration
    data_path = 'data/galaxy_spin_bins.csv'
    output_dir = 'output/spin_fit'
    
    # Load data
    print("Loading data...")
    df = load_spin_data(data_path)
    print(f"Loaded {len(df)} bins from {df['survey_id'].nunique()} surveys")
    
    # Prepare Stan data
    stan_data = prepare_stan_data(df)
    
    # Run MCMC
    print("Running MCMC...")
    fit = run_mcmc(stan_data)
    
    # Extract results
    print("Extracting results...")
    results = extract_results(fit, df)
    
    # Print summary
    print("\nParameter Summary:")
    print(results['summary'])
    
    # Save results
    print("\nSaving results...")
    save_results(results, output_dir)
    
    # Create plots
    print("Creating plots...")
    plot_results(results, df, Path(output_dir) / 'diagnostic_plots.png')
    
    print("\nAnalysis complete!")

if __name__ == '__main__':
    main()