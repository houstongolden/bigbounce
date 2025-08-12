#!/usr/bin/env python3
"""
CMB E-B Power Spectrum Forecast
Calculates detection significance for cosmic birefringence
"""

import numpy as np
import pandas as pd
import yaml
import matplotlib.pyplot as plt
from pathlib import Path

def load_config(config_path):
    """Load forecast configuration."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_theory_spectrum(cls_path):
    """Load theoretical CMB EE power spectrum."""
    df = pd.read_csv(cls_path)
    return df['ell'].values, df['C_ell_EE'].values

def load_instrument(inst_path):
    """Load instrument specifications."""
    df = pd.read_csv(inst_path)
    return df

def compute_eb_signal(beta_rad, C_EE):
    """
    Compute E-B power spectrum from birefringence.
    
    Small angle approximation: C_ell^EB ≈ 2β * C_ell^EE
    """
    return 2.0 * beta_rad * C_EE

def compute_variance(C_EB, C_EE, N_EE, N_BB, ell, dell, f_sky):
    """
    Compute variance of C_ell^EB measurement.
    
    Var(C_EB) ≈ [(C_EE + N_EE)(C_BB + N_BB) + C_EB^2] / [(2ℓ+1) * Δℓ * f_sky]
    
    Assumes C_BB ≈ 0 (no primordial B-modes at these scales)
    """
    numerator = (C_EE + N_EE) * N_BB + C_EB**2
    denominator = (2 * ell + 1) * dell * f_sky
    return numerator / denominator

def bin_spectrum(ell, C_ell, bin_edges):
    """Bin power spectrum."""
    digitized = np.digitize(ell, bin_edges)
    n_bins = len(bin_edges) - 1
    
    ell_bin = np.zeros(n_bins)
    C_bin = np.zeros(n_bins)
    
    for i in range(n_bins):
        mask = (digitized == i + 1)
        if np.sum(mask) > 0:
            ell_bin[i] = np.mean(ell[mask])
            C_bin[i] = np.mean(C_ell[mask])
    
    return ell_bin, C_bin

def forecast_detection(config, theory_cls, instrument):
    """Run the forecast for different birefringence angles."""
    results = []
    
    # Extract config parameters
    beta_grid = np.array(config['beta_grid_deg'])
    f_sky = config.get('f_sky', 0.5)
    ell_min = config['ell_min']
    ell_max = config['ell_max']
    bin_width = config['bin_width']
    
    # Create bins
    bin_edges = np.arange(ell_min, ell_max + bin_width, bin_width)
    
    # Get theory spectrum
    ell_theory, C_EE_theory = theory_cls
    
    # Interpolate to instrument ells
    ell_inst = instrument['ell'].values
    C_EE = np.interp(ell_inst, ell_theory, C_EE_theory)
    N_EE = instrument['N_ell_EE'].values
    
    # Conservative assumption: N_BB = N_EE
    N_BB = N_EE.copy()
    
    # Override f_sky if specified per ell
    if 'f_sky_override' in instrument.columns:
        f_sky_ell = instrument['f_sky_override'].fillna(f_sky).values
    else:
        f_sky_ell = np.full_like(ell_inst, f_sky)
    
    # Bin the spectra
    ell_bin, C_EE_bin = bin_spectrum(ell_inst, C_EE, bin_edges)
    _, N_EE_bin = bin_spectrum(ell_inst, N_EE, bin_edges)
    _, N_BB_bin = bin_spectrum(ell_inst, N_BB, bin_edges)
    _, f_sky_bin = bin_spectrum(ell_inst, f_sky_ell, bin_edges)
    
    # Remove empty bins
    mask = ell_bin > 0
    ell_bin = ell_bin[mask]
    C_EE_bin = C_EE_bin[mask]
    N_EE_bin = N_EE_bin[mask]
    N_BB_bin = N_BB_bin[mask]
    f_sky_bin = f_sky_bin[mask]
    
    # Loop over birefringence angles
    for beta_deg in beta_grid:
        beta_rad = np.deg2rad(beta_deg)
        
        # Compute E-B signal
        C_EB_bin = compute_eb_signal(beta_rad, C_EE_bin)
        
        # Compute variance per bin
        var_bin = compute_variance(
            C_EB_bin, C_EE_bin, N_EE_bin, N_BB_bin,
            ell_bin, bin_width, f_sky_bin
        )
        
        # SNR per bin
        snr_bin = C_EB_bin / np.sqrt(var_bin)
        
        # Total SNR (add in quadrature)
        snr_total = np.sqrt(np.sum(snr_bin**2))
        
        # Store results
        for i in range(len(ell_bin)):
            results.append({
                'ell_bin': int(ell_bin[i]),
                'beta_deg': beta_deg,
                'C_ell_EB': C_EB_bin[i],
                'Var': var_bin[i],
                'SNR': snr_bin[i]
            })
        
        print(f"β = {beta_deg}°: Total SNR = {snr_total:.2f}")
    
    return pd.DataFrame(results)

def save_results(df, output_dir):
    """Save forecast results."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Binned results
    df.to_csv(output_dir / 'eb_forecast_binned.csv', index=False)
    
    # Summary by angle
    summary = df.groupby('beta_deg').agg(
        SNR_tot=('SNR', lambda x: np.sqrt((x**2).sum()))
    ).reset_index()
    summary.to_csv(output_dir / 'eb_forecast_summary.csv', index=False)
    
    return summary

def plot_forecast(df, summary, output_dir):
    """Create forecast visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. C_ell^EB vs ell for different beta
    ax = axes[0, 0]
    for beta_deg in df['beta_deg'].unique():
        mask = df['beta_deg'] == beta_deg
        ax.loglog(df[mask]['ell_bin'], df[mask]['C_ell_EB'], 
                  'o-', label=f'β = {beta_deg}°')
    ax.set_xlabel('Multipole ℓ')
    ax.set_ylabel('$C_\ell^{EB}$ [μK²]')
    ax.legend()
    ax.set_title('E-B Power Spectrum')
    ax.grid(True, alpha=0.3)
    
    # 2. SNR vs ell
    ax = axes[0, 1]
    for beta_deg in df['beta_deg'].unique():
        if beta_deg > 0:  # Skip zero signal
            mask = df['beta_deg'] == beta_deg
            ax.semilogy(df[mask]['ell_bin'], df[mask]['SNR'], 
                        'o-', label=f'β = {beta_deg}°')
    ax.set_xlabel('Multipole ℓ')
    ax.set_ylabel('SNR per bin')
    ax.legend()
    ax.set_title('Signal-to-Noise Ratio')
    ax.grid(True, alpha=0.3)
    
    # 3. Total SNR vs beta
    ax = axes[1, 0]
    ax.plot(summary['beta_deg'], summary['SNR_tot'], 'bo-', linewidth=2)
    ax.axhline(y=3, color='r', linestyle='--', label='3σ detection')
    ax.axhline(y=5, color='g', linestyle='--', label='5σ detection')
    ax.set_xlabel('Birefringence angle β [degrees]')
    ax.set_ylabel('Total SNR')
    ax.legend()
    ax.set_title('Detection Significance')
    ax.grid(True, alpha=0.3)
    
    # 4. Detectability region
    ax = axes[1, 1]
    beta_fine = np.linspace(0, summary['beta_deg'].max(), 100)
    # Interpolate SNR
    snr_fine = np.interp(beta_fine, summary['beta_deg'], summary['SNR_tot'])
    
    ax.fill_between(beta_fine, 0, snr_fine, alpha=0.3, label='Detectable')
    ax.plot(beta_fine, snr_fine, 'b-', linewidth=2)
    
    # Add significance thresholds
    ax.axhline(y=3, color='r', linestyle='--', alpha=0.7)
    ax.axhline(y=5, color='g', linestyle='--', alpha=0.7)
    
    # Find minimum detectable angle
    idx_3sigma = np.where(snr_fine >= 3)[0]
    if len(idx_3sigma) > 0:
        beta_min_3sigma = beta_fine[idx_3sigma[0]]
        ax.axvline(x=beta_min_3sigma, color='r', linestyle=':', 
                   label=f'3σ: β > {beta_min_3sigma:.3f}°')
    
    ax.set_xlabel('Birefringence angle β [degrees]')
    ax.set_ylabel('Total SNR')
    ax.legend()
    ax.set_title('Detectability Region')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'eb_forecast_plots.png', dpi=150)
    plt.close()

def create_experiment_comparison(output_dir):
    """Create comparison plot for different experiments."""
    experiments = {
        'Planck': {'sigma_P': 7.0, 'beam': 10.0, 'f_sky': 0.5},
        'LiteBIRD': {'sigma_P': 2.2, 'beam': 30.0, 'f_sky': 0.7},
        'CMB-S4': {'sigma_P': 1.4, 'beam': 3.0, 'f_sky': 0.4},
        'AliCPT': {'sigma_P': 5.0, 'beam': 11.0, 'f_sky': 0.1}
    }
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    beta_range = np.linspace(0, 1.0, 50)
    
    for name, specs in experiments.items():
        # Simplified sensitivity calculation
        # SNR ∝ β * sqrt(f_sky) / sigma_P
        snr_approx = beta_range * np.sqrt(specs['f_sky']) * 1000 / specs['sigma_P']
        ax.plot(beta_range, snr_approx, label=name, linewidth=2)
    
    ax.axhline(y=3, color='r', linestyle='--', alpha=0.5, label='3σ')
    ax.axhline(y=5, color='g', linestyle='--', alpha=0.5, label='5σ')
    
    ax.set_xlabel('Birefringence angle β [degrees]')
    ax.set_ylabel('Approximate SNR')
    ax.set_title('CMB Experiment Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'experiment_comparison.png', dpi=150)
    plt.close()

def main():
    """Run the EB forecast pipeline."""
    # File paths
    config_path = 'config/eb_forecast_params.yml'
    cls_path = 'data/cls_EE_theory.csv'
    inst_path = 'data/instrument_cmbs4.csv'
    output_dir = 'output/eb_forecast'
    
    # Load inputs
    print("Loading configuration...")
    config = load_config(config_path)
    
    print("Loading theory spectrum...")
    theory_cls = load_theory_spectrum(cls_path)
    
    print("Loading instrument specifications...")
    instrument = load_instrument(inst_path)
    
    # Run forecast
    print("\nRunning forecast...")
    results_df = forecast_detection(config, theory_cls, instrument)
    
    # Save results
    print("\nSaving results...")
    summary_df = save_results(results_df, output_dir)
    
    print("\nSummary:")
    print(summary_df)
    
    # Create plots
    print("\nCreating plots...")
    plot_forecast(results_df, summary_df, Path(output_dir))
    create_experiment_comparison(Path(output_dir))
    
    print("\nForecast complete!")

if __name__ == '__main__':
    main()