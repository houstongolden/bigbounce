# Analysis Pipeline Documentation

This directory contains the analysis pipelines for the spin-torsion cosmology paper.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run galaxy spin fit
python scripts/spin_fit_stan.py

# Run CMB EB forecast
python scripts/eb_forecast.py

# Run validation checks
python scripts/figure_checks.py
```

## Pipeline Overview

### 1. Galaxy Spin Analysis (`spin_fit_stan.py`)

Hierarchical Bayesian fit to galaxy spin asymmetry data using Stan.

**Inputs**:
- `data/galaxy_spin_bins.csv`: Binned galaxy counts by survey and redshift

**Outputs**:
- `output/spin_fit/parameter_summary.csv`: MCMC parameter estimates
- `output/spin_fit/A_z_posterior.csv`: Asymmetry vs redshift with uncertainties
- `output/spin_fit/diagnostic_plots.png`: MCMC diagnostics and fit visualization

**Model**: 
- $A(z) = A_0(1+z)^{-p}e^{-qz}$ with survey-specific biases
- Accounts for selection effects and label noise

### 2. CMB E-B Forecast (`eb_forecast.py`)

Calculates detection significance for cosmic birefringence.

**Inputs**:
- `config/eb_forecast_params.yml`: Configuration (angles, bins, experiments)
- `data/cls_EE_theory.csv`: Theoretical CMB EE spectrum
- `data/instrument_*.csv`: Instrument noise curves

**Outputs**:
- `output/eb_forecast/eb_forecast_binned.csv`: C_ℓ^EB by multipole and angle
- `output/eb_forecast/eb_forecast_summary.csv`: Total SNR vs birefringence angle
- `output/eb_forecast/eb_forecast_plots.png`: Visualization of detectability

**Method**:
- Small-angle approximation: $C_\ell^{EB} \approx 2\beta C_\ell^{EE}$
- Knox formula for variance calculation
- Binned analysis for computational efficiency

### 3. Joint Likelihood Analysis

Combines CMB and galaxy spin constraints with proper correlation.

```python
from scripts.joint_likelihood import joint_significance

# Example usage
AE, sE = 2e-4, 1e-4  # CMB measurement
AG, sG = 0.003, 0.001  # Galaxy spin measurement
rho = 0.3  # Correlation

A_combined, sigma_combined, Z_combined = joint_significance(
    AE, sE, AG, sG, rho=rho
)
```

### 4. Validation Checks (`figure_checks.py`)

CI/CD validation ensuring:
- Data format compliance
- Physical value ranges
- Proper correlation implementation
- Reproducibility (seeds, versions)
- Unit consistency

Run before any commit to ensure data integrity.

## Data Format Specifications

### Galaxy Spin Data (CSV)

| Column | Type | Description | Valid Range |
|--------|------|-------------|-------------|
| z_bin_center | float | Redshift bin center | [0, 10] |
| z_bin_width | float | Bin width | > 0 |
| N_cw | int | Clockwise count | ≥ 0 |
| N_ccw | int | Counter-clockwise count | ≥ 0 |
| survey_id | str | Survey identifier | — |
| b_weight | float | Selection weight | [0, 1] |
| psf_quality_flag | int | Quality flag | {0, 1} |

### CMB Theory Spectrum (CSV)

| Column | Type | Description | Units |
|--------|------|-------------|-------|
| ell | int | Multipole | ≥ 2 |
| C_ell_EE | float | EE power spectrum | μK² |

### Instrument Specification (CSV)

| Column | Type | Description | Units |
|--------|------|-------------|-------|
| ell | int | Multipole | ≥ 2 |
| N_ell_EE | float | Noise power spectrum | μK² |
| beam_fwhm_arcmin | float | Beam width | arcmin |
| f_sky_override | float | Sky fraction (optional) | [0, 1] |

## Configuration

Main configuration in `config/eb_forecast_params.yml`:

```yaml
beta_grid_deg: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
f_sky: 0.4
ell_min: 2
ell_max: 200
bin_width: 10
rho_grid: [0.0, 0.3, 0.5]
random_seed: 42
```

## Reproducibility

1. **Environment**: Use provided `requirements.txt` or `environment.yml`
2. **Random seeds**: Set in all stochastic processes
3. **Data versioning**: Tag releases with Zenodo DOIs
4. **Code versioning**: Git commit hashes in outputs

## Testing

```bash
# Unit tests
pytest tests/

# Integration test with example data
python scripts/run_full_pipeline.py --test

# Validation checks
python scripts/figure_checks.py
```

## Troubleshooting

**Stan compilation errors**: Ensure C++ compiler is available
```bash
# macOS
brew install gcc

# Linux
sudo apt-get install build-essential
```

**Memory issues**: Reduce MCMC chains or samples
```python
fit = run_mcmc(data, n_chains=2, n_samples=1000)  # Reduced
```

**Convergence problems**: Check data quality and priors
- Ensure sufficient counts per bin (N > 100)
- Verify priors are sensible for your data
- Increase warmup iterations

## Citation

If you use these pipelines, please cite:
```bibtex
@article{golden2024spintorsion,
  title={Geometric Dark Energy from Spin-Torsion Cosmology},
  author={Golden, Houston},
  journal={arXiv preprint arXiv:2024.xxxxx},
  year={2024}
}
```