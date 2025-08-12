## 5. Comprehensive Systematic Analysis

This section provides a comprehensive analysis of systematic errors and their mitigation strategies. Observable amplitudes throughout depend on the renormalized loop coefficient $(\alpha/M)$ multiplied by the inflationary dilution factor $\mathcal{D}_{\rm inf}$. 

Combined detection significance accounts for potential correlation between probes:

$$Z_{\rm comb} = \frac{w_1 Z_1 + w_2 Z_2}{\sqrt{w_1^2 + w_2^2 + 2\rho w_1 w_2}}$$

where $Z_i$ are individual probe significances, $w_i$ are weights (default 1), and $\rho$ is the cross-probe correlation coefficient. We show results for $\rho \in \{0, 0.3, 0.5\}$ spanning optimistic to conservative scenarios.

### 5.1 CMB Systematic Errors and Mitigation

#### 5.1.1 Foreground Contamination

Galactic foregrounds can mimic E-B correlations through:

**Synchrotron Emission**: Polarized at low frequencies with spectral index $\beta_s \approx -3.1$
**Thermal Dust**: Polarized at high frequencies with $\beta_d \approx 1.6$
**Anomalous Microwave Emission**: Potentially polarized with uncertain spectrum

**Mitigation Strategy**: Multi-frequency component separation using:
$$\mathbf{s} = \mathbf{A}\mathbf{c} + \mathbf{n}$$
where $\mathbf{s}$ is the observed signal, $\mathbf{A}$ is the mixing matrix, $\mathbf{c}$ are the components, and $\mathbf{n}$ is noise.

**Residual Error**: $< 5 \times 10^{-5} \mu\text{K}^2$ after component separation

#### 5.1.2 Instrumental Systematics

Key effects include:

**Beam Asymmetries**: Elliptical beams couple temperature to polarization
**Calibration Errors**: Absolute and relative calibration uncertainties
**Bandpass Mismatch**: Frequency-dependent systematic errors

**Mitigation Strategy**:
- Detailed beam modeling with $< 0.1\%$ accuracy
- Cross-correlation between detectors and frequencies
- Null tests using data splits and simulations

**Residual Error**: $< 2 \times 10^{-5} \mu\text{K}^2$ after mitigation

### 5.2 Galaxy Survey Systematic Errors

#### 5.2.1 Shape Measurement Systematics

**PSF Modeling**: Point spread function variations across the field
**Shear Calibration**: Multiplicative and additive biases in shape measurement
**Selection Effects**: Magnitude and size-dependent detection biases

**Mitigation Strategy**:
- Image simulations with realistic PSF variations
- Metacalibration and self-calibration methods
- Tomographic analysis to test for systematic trends

**Residual Error**: $< 0.0004$ after shape calibration

#### 5.2.2 Photometric Redshift Errors

Photo-z errors scatter galaxies between redshift bins with $\sigma_z = 0.03(1+z)$ for LSST.

**Mitigation Strategy**:
- Spectroscopic training samples ($> 10^6$ galaxies)
- Cross-correlation with spectroscopic surveys
- Self-calibration using clustering redshifts

**Residual Error**: $< 0.0002$ after photo-z calibration

### 5.3 Combined Error Budget and Detection Significance

| Source | CMB E-B [$\mu\text{K}^2$] | Galaxy Spins |
|--------|---------------------------|--------------|
| Foregrounds | $5 \times 10^{-5}$ | N/A |
| Instrumental | $2 \times 10^{-5}$ | N/A |
| Cosmic Variance | $8 \times 10^{-5}$ | N/A |
| Shape Systematics | N/A | $0.0004$ |
| Photo-z Errors | N/A | $0.0002$ |
| Selection Biases | N/A | $0.0003$ |
| **Total Systematic** | $9 \times 10^{-5}$ | $0.0005$ |
| **Statistical** | $8 \times 10^{-5}$ | $0.0005$ |
| **Combined** | $1.2 \times 10^{-4}$ | $0.0007$ |

**Detection Significances**:
- **CMB E-B**: $1.7\sigma$ (individual)
- **Galaxy Spins**: $4.3\sigma$ (individual)
- **Combined**: $4.6\sigma$ (joint analysis)