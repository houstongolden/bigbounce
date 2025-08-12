## Data & Methods — CMB EB Pipeline (Forecast)

### CMB E-B Power Spectrum Construction

**Theory**: Cosmic birefringence rotates E-modes into B-modes by angle $\beta$:
$$C_\ell^{EB} = 2\beta C_\ell^{EE} \quad \text{(small angle approximation)}$$

**Full expression** (beyond small angle):
$$C_\ell^{EB} = \sin(2\beta) C_\ell^{EE}$$
$$C_\ell^{EE,\text{obs}} = \cos^2(2\beta) C_\ell^{EE} + \sin^2(2\beta) C_\ell^{BB}$$

**Mapping to parity-odd operator**:
$$\beta = \frac{1}{2}\int_0^{\eta_0} d\eta \, \frac{d\alpha}{d\eta}$$

where $\alpha(\eta)$ is the rotation angle along photon path, related to $(\alpha/M)$ through:
$$\frac{d\alpha}{d\eta} = \frac{4\pi}{M_{\text{Pl}}} \left(\frac{\alpha}{M}\right) \dot{\phi} f(\eta)$$

with $f(\eta)$ encoding the cosmological evolution.

### Instrument Models

**LiteBIRD (2030s)**:
- Frequency channels: 40-402 GHz (15 bands)
- Angular resolution: 18-71 arcmin
- Sky fraction: $f_{\text{sky}} = 0.7$
- Polarization sensitivity: 2.2 μK·arcmin
- Systematic error budget: 0.1 μK²

**CMB-S4 (2028+)**:
- Frequency channels: 30-280 GHz
- Angular resolution: 1-10 arcmin
- Sky fraction: $f_{\text{sky}} = 0.4$
- Polarization sensitivity: 1.4 μK·arcmin (deep survey)
- Delensing capability: 95% at $\ell < 100$

**AliCPT (2025+)**:
- Frequency channels: 90, 150 GHz
- Angular resolution: 9-11 arcmin
- Sky fraction: $f_{\text{sky}} = 0.1$ (Northern sky)
- Polarization sensitivity: 5 μK·arcmin
- Focus on reionization bump

### Noise Model

**Instrumental noise**:
$$N_\ell = \left(\frac{\sigma_P \theta_{\text{FWHM}}}{T_{\text{CMB}}}\right)^2 \exp\left[\frac{\ell(\ell+1)\theta_{\text{FWHM}}^2}{8\ln 2}\right]$$

where:
- $\sigma_P$: Polarization sensitivity per detector
- $\theta_{\text{FWHM}}$: Beam full-width half-maximum
- $T_{\text{CMB}} = 2.7255$ K

**Total variance** (Knox formula):
$$\text{Var}(C_\ell^{EB}) = \frac{1}{(2\ell+1)f_{\text{sky}}} \left[(C_\ell^{EE} + N_\ell^{EE})(C_\ell^{BB} + N_\ell^{BB}) + (C_\ell^{EB})^2\right]$$

### Forecast Method

**Fisher matrix approach**:
$$F_{ij} = \sum_\ell \frac{\partial C_\ell}{\partial p_i} \text{Cov}_\ell^{-1} \frac{\partial C_\ell}{\partial p_j}$$

where $p_i \in \{\beta, \tau, A_s, ...\}$ includes birefringence and cosmological parameters.

**Monte Carlo validation**:
1. Generate 1000 realizations with input $\beta$
2. Recover using quadratic estimator
3. Validate error bars and bias

**Binning strategy**:
- Ultra-low-$\ell$: $\ell = 2-10$ (individual modes)
- Reionization: $\ell = 10-30$ (Δℓ = 5)
- Intermediate: $\ell = 30-200$ (Δℓ = 20)
- High-$\ell$: $\ell > 200$ (less sensitive to birefringence)

### Systematic Error Budget

**Known systematics and mitigation**:

| Systematic | Effect on EB | Mitigation | Residual |
|------------|--------------|------------|----------|
| Beam mismatch | Spurious EB | Beam map from planets | < 0.1% |
| Polarization angle | Rotates E→B | Pre-flight calibration | < 0.5° |
| Bandpass mismatch | Frequency decorrelation | Component separation | < 1% |
| Time-varying systematics | Scan-synchronous signal | Half-mission splits | < 0.01 μK² |

### Null Test Plan

1. **Half-mission splits**: First vs second half of mission
2. **Detector splits**: Odd vs even detectors  
3. **Frequency splits**: Low vs high frequency channels
4. **Sky splits**: Northern vs Southern ecliptic hemispheres
5. **TB consistency**: $C_\ell^{TB} = 0$ within errors

### Analysis Pipeline

**Component separation**: 
- SMICA/NILC/SEVEM methods
- Foreground templates from Planck
- EB-specific cleaning (dust has negligible EB)

**Likelihood**:
- Low-$\ell$: Pixel-based exact likelihood
- High-$\ell$: Gaussian approximation
- Joint with temperature and EE

**Parameter estimation**:
- MCMC: CosmoMC/Cobaya framework
- Nested sampling for evidence calculation
- Profile likelihood for $\beta$ constraints

### Data Products

**Power spectra** (FITS format):
```
# Primary HDU: binned C_ell^EB
ell_min, ell_max, ell_center, C_EB, sigma_C_EB, cov_index

# Extension: covariance matrix
cov_EB_EB, cov_EB_EE, cov_EB_TE, ...
```

**Likelihood files** (HDF5):
- Compressed covariance matrices
- Window functions
- Beam transfer functions
- Foreground marginalization parameters

**Simulations**: 
- 100 signal + noise realizations per configuration
- FFP10-style systematic simulations
- Available at [Simulation repository]

All products follow LAMBDA/NERSC formatting standards for CMB data.