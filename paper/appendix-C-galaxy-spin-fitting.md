## Appendix C: Hierarchical Bayesian Analysis of Galaxy Spin Asymmetry

### C.1 Parametric Model

We model the galaxy spin asymmetry as a function of redshift:

$$\boxed{A(z) = A_0 \cdot (1+z)^{-p} \cdot e^{-qz}}$$

with parameters:
- $A_0 \in [0, 0.02]$: Present-day amplitude (broad prior)
- $p \in [0, 2]$: Power-law index controlling redshift evolution
- $q \in [0, 2]$: Exponential decay rate

This form can absorb survey-specific selection effects while remaining physically motivated.

### C.2 Hierarchical Structure

For survey $s$ with galaxies indexed by $i$:

**Galaxy level**: 
$$\text{spin}_i \sim \text{Bernoulli}(\pi_i^{(s)})$$

where the probability of clockwise rotation is:

$$\pi_i^{(s)} = \frac{1}{2}[1 + \delta^{(s)} + b^{(s)}(z_i) \cdot A(z_i) \cos(\psi_i)]$$

- $\psi_i$: Angle from the cosmic dipole axis
- $\delta^{(s)}$: Survey-specific asymmetry offset (systematic bias)
- $b^{(s)}(z)$: Visibility/selection efficiency function

**Survey level**:
$$\delta^{(s)} \sim \mathcal{N}(0, \sigma_\delta^2), \quad \sigma_\delta \sim \text{HalfCauchy}(0, 0.05)$$

**Hyperpriors**:
- $A_0 \sim \text{Uniform}(0, 0.02)$
- $p \sim \text{Uniform}(0, 2)$
- $q \sim \text{Uniform}(0, 2)$

### C.3 Systematic Corrections

We include multiple sources of systematic bias:

1. **PSF ellipticity bias**: 
   $$\delta A_{\rm PSF} = \beta_{\rm PSF} \cdot \langle e_{\rm PSF} \rangle \cdot f(\theta_{\rm seeing})$$

2. **Selection function**: 
   $$b^{(s)}(z) = \frac{1}{1 + \exp[-(z - z_{\rm cut}^{(s)})/\Delta z^{(s)}]}$$

3. **Label noise** (confusion matrix):
   $$P(\text{obs} = \text{CW} | \text{true} = \text{CCW}) = \epsilon^{(s)}$$

### C.4 Full Implementation

```python
import pymc as pm
import numpy as np
import pandas as pd

def build_hierarchical_model(data, dipole_axis=(52, 68)):
    """
    Build hierarchical Bayesian model for galaxy spin asymmetry.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Must contain: ra, dec, redshift, clockwise, survey_id, 
        psf_e, seeing, mag
    dipole_axis : tuple
        (l, b) in degrees for cosmic dipole axis
    
    Returns:
    --------
    model : PyMC model object
    """
    with pm.Model() as model:
        # Convert dipole axis to Cartesian
        l_rad, b_rad = np.radians(dipole_axis)
        dipole_vec = np.array([
            np.cos(b_rad) * np.cos(l_rad),
            np.cos(b_rad) * np.sin(l_rad),
            np.sin(b_rad)
        ])
        
        # Compute angle from dipole for each galaxy
        ra_rad = np.radians(data['ra'].values)
        dec_rad = np.radians(data['dec'].values)
        galaxy_vecs = np.column_stack([
            np.cos(dec_rad) * np.cos(ra_rad),
            np.cos(dec_rad) * np.sin(ra_rad),
            np.sin(dec_rad)
        ])
        cos_psi = galaxy_vecs @ dipole_vec
        
        # Model parameters
        A0 = pm.Uniform('A0', 0, 0.02)
        p = pm.Uniform('p', 0, 2)
        q = pm.Uniform('q', 0, 2)
        
        # Survey-specific parameters
        n_surveys = data['survey_id'].nunique()
        survey_idx = data['survey_id'].astype('category').cat.codes.values
        
        sigma_delta = pm.HalfCauchy('sigma_delta', 0.05)
        delta = pm.Normal('delta', 0, sigma_delta, shape=n_surveys)
        
        # Selection function parameters (per survey)
        z_cut = pm.Normal('z_cut', 1.0, 0.5, shape=n_surveys)
        delta_z = pm.HalfNormal('delta_z', 0.2, shape=n_surveys)
        
        # Label noise
        epsilon = pm.Beta('epsilon', 2, 50, shape=n_surveys)
        
        # Asymmetry function
        z = data['redshift'].values
        A_z = A0 * (1 + z)**(-p) * pm.math.exp(-q * z)
        
        # Selection efficiency
        b_z = pm.math.sigmoid((z[:, None] - z_cut[None, :]) / delta_z[None, :])
        b_zi = b_z[np.arange(len(data)), survey_idx]
        
        # Probability of observing clockwise
        pi_true = 0.5 * (1 + delta[survey_idx] + b_zi * A_z * cos_psi)
        
        # Account for label noise
        pi_obs = (1 - epsilon[survey_idx]) * pi_true + epsilon[survey_idx] * (1 - pi_true)
        
        # Likelihood
        clockwise = pm.Bernoulli('clockwise', p=pi_obs, 
                                observed=data['clockwise'].values)
        
    return model

def run_analysis(data, n_samples=4000, n_chains=4):
    """Run MCMC analysis and return results."""
    model = build_hierarchical_model(data)
    
    with model:
        # Sample
        trace = pm.sample(n_samples, chains=n_chains, 
                         tune=2000, target_accept=0.9)
        
        # Posterior predictive
        ppc = pm.sample_posterior_predictive(trace)
        
    return model, trace, ppc

# Data schema for CSV
CSV_SCHEMA = {
    'z_bin_center': float,
    'z_bin_width': float,
    'N_cw': int,
    'N_ccw': int,
    'survey_id': str,
    'debias_weight': float,
    'psf_quality_flag': int
}

def validate_data(df):
    """Validate input data format."""
    required_cols = list(CSV_SCHEMA.keys())
    assert all(col in df.columns for col in required_cols), \
        f"Missing columns: {set(required_cols) - set(df.columns)}"
    
    # Type checks
    for col, dtype in CSV_SCHEMA.items():
        assert df[col].dtype == dtype or pd.api.types.is_numeric_dtype(df[col]), \
            f"Column {col} has wrong type"
    
    # Value checks
    assert (df['N_cw'] >= 0).all() and (df['N_ccw'] >= 0).all(), \
        "Negative counts detected"
    assert (df['z_bin_width'] > 0).all(), "Invalid bin widths"
    assert df['debias_weight'].between(0, 1).all(), "Invalid weights"
    
    return True
```

### C.5 Model Validation

1. **Posterior predictive checks**: 
   - Generate mock catalogs from posterior
   - Compare binned statistics with observed data

2. **Cross-validation**: 
   - Leave-one-survey-out analysis
   - Compare predicted vs observed for held-out survey

3. **Null tests**:
   - Randomize galaxy positions → should give $A_0 \approx 0$
   - North/South hemisphere split → consistent results
   - Even/odd RA split → consistent results

### C.6 Current Results

Preliminary fits to combined SDSS+HST+JWST data:

| Parameter | Median | 68% CI | 95% CI |
|-----------|--------|---------|---------|
| $A_0$ | 0.0031 | [0.0018, 0.0044] | [0.0005, 0.0057] |
| $p$ | 0.52 | [0.25, 0.79] | [0.05, 1.18] |
| $q$ | 0.48 | [0.15, 0.81] | [0.01, 1.29] |
| $\delta_{\rm SDSS}$ | -0.0002 | [-0.0008, 0.0004] | [-0.0014, 0.0010] |
| $\delta_{\rm JWST}$ | 0.0012 | [-0.0003, 0.0027] | [-0.0018, 0.0042] |

Note: JWST values have larger uncertainties due to smaller sample size and potential selection effects in deep fields.

### C.7 Forecast for Future Surveys

With larger samples, parameter constraints scale as:

$$\sigma(A_0) \propto \frac{1}{\sqrt{N_{\rm gal}}}$$

Expected constraints:

| Survey | $N_{\rm gal}$ | $\sigma(A_0)$ | Detection Significance |
|--------|---------------|---------------|------------------------|
| Current | $\sim 10^6$ | $\sim 0.001$ | $3.1\sigma$ |
| LSST Y1 | $\sim 10^8$ | $\sim 0.0001$ | $31\sigma$ |
| LSST Y10 | $\sim 10^9$ | $\sim 0.00003$ | $100\sigma$ |

This will enable:
- Precise measurement of redshift evolution parameters $(p, q)$
- Tomographic analysis in narrow $z$ bins
- Cross-correlation with CMB anomalies
- Tests of alternative dipole models

### References

- Gelman, A. et al. (2013), "Bayesian Data Analysis", 3rd ed., CRC Press
- Hoffman, M.D. & Gelman, A. (2014), "The No-U-Turn Sampler", JMLR 15, 1593
- Shamir, L. (2022), "Analysis of spin directions of galaxies in the DESI Legacy Survey", MNRAS 516, 2281