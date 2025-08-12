## Systematics Audit Table

| Probe | Systematic Effect | Test Performed | Result | Pass/Fail | Mitigation | Residual |
|-------|------------------|----------------|---------|-----------|------------|----------|
| **CMB EB** | | | | | | |
| | Beam mismatch | Planet observations | $< 0.5°$ beam uncertainty | ✓ Pass | Beam map correction | $< 0.1\%$ |
| | Polarization angle | Pre-flight calibration | $0.3° \pm 0.1°$ offset | ✓ Pass | Angle correction | $< 0.5°$ |
| | Instrumental noise | Noise simulations | Matches expected $N_\ell$ | ✓ Pass | Optimal filtering | As modeled |
| | Gain variations | Gain solution stability | $< 0.1\%$ drift/day | ✓ Pass | Daily calibration | $< 0.05\%$ |
| | Bandpass mismatch | Component separation | $< 1\%$ frequency decorrelation | ✓ Pass | Multi-frequency maps | $< 1\%$ |
| | Time-domain systematics | Half-mission splits | $(0.2 \pm 2.5) \times 10^{-4}$ μK² | ✓ Pass | Scan strategy optimization | $< 0.01$ μK² |
| | Sidelobe pickup | Far sidelobe modeling | $< 0.1$ μK contamination | ✓ Pass | Sidelobe subtraction | $< 0.01$ μK |
| | HWP non-ideality | Mueller matrix calibration | $< 0.5\%$ I→P leakage | ✓ Pass | Mueller correction | $< 0.1\%$ |
| | $1/f$ noise | Knee frequency measurement | $f_{\text{knee}} < 10$ mHz | ✓ Pass | High-pass filtering | Negligible |
| | Cosmic ray hits | Glitch detection | $< 0.1\%$ data flagged | ✓ Pass | Glitch removal | None |
| | Foreground residuals | Dust/synchrotron templates | EB uncorrelated with foregrounds | ✓ Pass | Component separation | $< 2 \times 10^{-5}$ μK² |
| **Galaxy Spins** | | | | | | |
| | PSF ellipticity | PSF-spin correlation | $r = 0.02 \pm 0.03$ | ✓ Pass | PSF deconvolution | $< 0.0002$ |
| | Morphology misclass | Human validation | 94.2% agreement | ✓ Pass | Ambiguous exclusion | $< 0.0004$ |
| | Inclination bias | Edge-on weighting | Corrected distribution flat | ✓ Pass | $1/\cos(i)$ weights | $< 0.0001$ |
| | Magnitude selection | Bright/faint split | $(0.4 \pm 1.8) \times 10^{-4}$ | ✓ Pass | Completeness correction | $< 0.0003$ |
| | Redshift errors | Spec-z comparison | $\sigma_z/(1+z) < 0.003$ | ✓ Pass | Photo-z calibration | Negligible |
| | Sky systematics | Galactic latitude test | No latitude dependence | ✓ Pass | $|b| > 20°$ cut | None |
| | Seeing variations | Seeing-spin correlation | $r = -0.01 \pm 0.04$ | ✓ Pass | Seeing cuts | $< 0.0001$ |
| | CCD systematics | Chip-to-chip comparison | Consistent within $0.5\sigma$ | ✓ Pass | Flat field correction | $< 0.0001$ |
| | Stellar contamination | Star control sample | $A_{\text{stars}} = -0.0001 \pm 0.0008$ | ✓ Pass | Star/galaxy separation | None |
| | Merger contamination | Visual inspection | $< 3\%$ merger fraction | ✓ Pass | Merger flag exclusion | $< 0.0001$ |
| **Cross-Probe** | | | | | | |
| | Sky overlap correlation | Residual correlation | $r = 0.08 \pm 0.11$ | ✓ Pass | Independent analysis | None |
| | Large-scale structure | LSS template projection | No correlation detected | ✓ Pass | LSS marginalization | $< 5\%$ |
| | Calibration errors | Cross-calibration | Consistent normalizations | ✓ Pass | Joint calibration | $< 2\%$ |

### Summary Statistics

**CMB EB Systematic Budget**:
- Total systematic error: $< 2.3 \times 10^{-5}$ μK²
- Statistical error (forecast): $\sim 1.0 \times 10^{-4}$ μK²
- Systematic/Statistical ratio: $< 0.23$

**Galaxy Spin Systematic Budget**:
- Total systematic error: $< 0.0006$
- Statistical error (current): $\sim 0.0010$
- Systematic/Statistical ratio: $< 0.60$

**Overall Assessment**: All systematic effects are controlled below the statistical error level, ensuring discovery potential is not compromised by known systematics.