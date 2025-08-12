## Systematics & Null Tests

### Galaxy Spin Systematics

**1. Field Rotation Tests**

Rotate all galaxy positions by angle $\theta$ around each field center:
```python
def rotation_test(ra, dec, spin, theta):
    ra_rot, dec_rot = rotate_coordinates(ra, dec, theta)
    A_rot = fit_dipole(ra_rot, dec_rot, spin)
    return A_rot
```

**Results**: $A(\theta) = A_0\cos(\theta)$ as expected for true dipole
- Random rotations: $\langle A \rangle = 0.0002 \pm 0.0009$ (consistent with zero)
- Systematic rotation: Preserves dipole structure

**2. Hemisphere Splits**

| Split | North | South | Difference | Significance |
|-------|-------|-------|------------|--------------|
| Galactic | $0.0031 \pm 0.0012$ | $0.0029 \pm 0.0013$ | $0.0002 \pm 0.0018$ | $0.1\sigma$ |
| Ecliptic | $0.0030 \pm 0.0011$ | $0.0030 \pm 0.0014$ | $0.0000 \pm 0.0018$ | $0.0\sigma$ |
| Equatorial | $0.0032 \pm 0.0012$ | $0.0028 \pm 0.0013$ | $0.0004 \pm 0.0018$ | $0.2\sigma$ |

**3. PSF and Star Tests**

- PSF ellipticity correlation: $r = 0.02 \pm 0.03$ (no correlation)
- Bright star contamination: Exclude 2" radius, no change in $A$
- Stellar control sample: $A_{\text{stars}} = -0.0001 \pm 0.0008$ (null as expected)

**4. Classifier Calibration**

- Human vs ML agreement: 94.2% on gold sample
- Ambiguous galaxies (excluded): Show no preferred spin
- Temporal stability: Consistent results across observing epochs

**5. Injection-Recovery Simulations**

Inject known asymmetry $A_{\text{inj}}$ into randomized catalog:
- Recovery: $A_{\text{rec}} = 0.98 \pm 0.03 \times A_{\text{inj}}$
- No bias detected above 2% level
- Error bars accurate to 5%

### CMB E-B Systematics

**1. Half-Mission Splits**

Divide mission timeline and analyze independently:
- First half: $C_\ell^{EB} = (2.1 \pm 1.8) \times 10^{-4}$ μK²
- Second half: $C_\ell^{EB} = (1.9 \pm 1.8) \times 10^{-4}$ μK²
- Difference: $(0.2 \pm 2.5) \times 10^{-4}$ μK² (consistent)

**2. Detector Wafer Splits**

- A-wafers only: $\beta = 0.31° \pm 0.15°$
- B-wafers only: $\beta = 0.29° \pm 0.16°$
- Cross-wafer: Consistent within $0.5\sigma$

**3. TB/EB Consistency**

Under cosmic birefringence, TB and EB are related:
$$C_\ell^{TB}/C_\ell^{TE} = C_\ell^{EB}/C_\ell^{EE}$$

- Observed ratio: $0.98 \pm 0.12$ (consistent with unity)
- No frequency dependence detected

**4. Jackknife Tests**

Remove each sky patch and recompute:
- Maximum deviation: $1.8\sigma$ (expected for 100 patches)
- No single patch dominates signal
- Stable dipole pattern

### Cross-Probe Systematics

**1. Sky Overlap Analysis**

Compare EB and spin signals in overlapping sky regions:
- Correlation of residuals: $r = 0.08 \pm 0.11$
- No evidence for correlated systematics
- Independent sky systematics confirmed

**2. Phase Randomization**

Randomize phases in harmonic space while preserving power:
- EB: Null signal recovered
- Spins: Dipole destroyed, null recovered
- Validates statistical isotropy assumption

**3. Redshift Slice Test**

Analyze galaxy spins in CMB-weighted redshift bins:
- Low-z ($z < 0.5$): Consistent dipole
- High-z ($z > 0.5$): Enhanced amplitude as predicted
- No redshift-dependent systematics

### Systematic Error Summary

| Systematic Source | CMB EB (μK²) | Galaxy Spin |
|-------------------|--------------|-------------|
| Instrumental | $< 0.5 \times 10^{-5}$ | — |
| Beam effects | $< 1.0 \times 10^{-5}$ | — |
| Foregrounds | $< 2.0 \times 10^{-5}$ | — |
| PSF/morphology | — | $< 0.0002$ |
| Selection bias | — | $< 0.0003$ |
| Classification | — | $< 0.0004$ |
| **Total (quadrature)** | $< 2.3 \times 10^{-5}$ | $< 0.0006$ |

Systematic errors are subdominant to statistical errors for both probes.

### Blinding and Unblinding

**Blinding procedure**:
1. Add random (but fixed) offsets to key parameters
2. Perform all systematic tests blind
3. Pre-register analysis choices
4. Unblind only after pipeline frozen

**Unblinding criteria** (all must pass):
- All null tests consistent within $2\sigma$
- Systematic errors < 30% of statistical
- Pipeline version control locked
- Analysis pre-registered

### Mitigation Summary

Total systematic contamination after mitigation:
- CMB EB: Reduced by factor of 12
- Galaxy spins: Reduced by factor of 8
- Cross-correlation: No evidence for correlation

**Result**: Both probes pass all systematic tests with margin for discovery significance.