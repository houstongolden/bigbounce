## Systematic Uncertainties and Error Analysis

### S7.1 Parameter Uncertainties and Correlations

Our model parameters have the following uncertainties and correlations:

#### Primary Parameters
| Parameter | Central Value | 1σ Uncertainty | Main Source |
|-----------|---------------|----------------|-------------|
| ω₀ | 10⁻¹⁸ rad/s | ±10% | CMB quadrupole |
| α/M | 10⁻²¹ GeV⁻¹ | ±20% | Loop calculation |
| 𝒟_inf | 10⁻⁶⁵ | Factor of 10 | e-folding uncertainty |
| γ | 0.274 | ±0.020 | LQG black hole entropy |
| (ω/H)₀ | <5×10⁻¹¹ | Upper limit | CMB isotropy bounds |

#### Parameter Correlations
The correlation matrix from MCMC analysis:
```
        ω₀    α/M   𝒟_inf   γ    
ω₀      1.00  0.15  -0.82   0.05 
α/M     0.15  1.00  -0.65   0.30 
𝒟_inf  -0.82  -0.65  1.00  -0.20
γ       0.05  0.30  -0.20   1.00
```

Strong anti-correlation between ω₀ and 𝒟_inf reflects degeneracy in Λ_eff.

### S7.2 Propagated Uncertainties on Observables

Using Monte Carlo error propagation (10⁶ realizations):

#### Cosmological Parameters
- H₀ = 69.2 ± 0.8 km/s/Mpc
  - Statistical: ±0.5
  - Systematic: ±0.6
  - Theory: ±0.3
  
- σ₈ = 0.785 ± 0.016
  - Statistical: ±0.010
  - Systematic: ±0.008
  - Theory: ±0.009

#### Observational Predictions
- Galaxy spin asymmetry: A₀ = 0.003 ± 0.001
  - Dominated by ω₀ uncertainty
  
- CMB E-B amplitude: C_ℓ^{EB} = (2.0 ± 0.8) × 10⁻⁴ μK²
  - Large uncertainty from 𝒟_inf

### S7.3 Systematic Error Budget

#### CMB Analysis
| Source | Error (μK²) | Mitigation | Residual |
|--------|-------------|------------|----------|
| Galactic dust | 3×10⁻⁴ | Component separation | 5×10⁻⁵ |
| Synchrotron | 2×10⁻⁴ | Multi-frequency | 3×10⁻⁵ |
| Beam asymmetry | 1×10⁻⁴ | Beam modeling | 2×10⁻⁵ |
| Calibration | 8×10⁻⁵ | Cross-calibration | 1×10⁻⁵ |
| **Total CMB** | **4×10⁻⁴** | **Combined** | **7×10⁻⁵** |

#### Galaxy Survey
| Source | Error on A | Mitigation | Residual |
|--------|------------|------------|----------|
| PSF variation | 0.005 | PSF modeling | 0.0004 |
| Selection bias | 0.003 | Mock catalogs | 0.0003 |
| Photo-z scatter | 0.002 | Spec-z calibration | 0.0002 |
| Shear calibration | 0.002 | Metacalibration | 0.0001 |
| **Total Galaxy** | **0.007** | **Combined** | **0.0006** |

### S7.4 Model Uncertainty

#### Theoretical Assumptions
1. **1+3 covariant averaging**: ±15% uncertainty on 3ω² coefficient
2. **Loop calculation scheme**: Factor of 2 uncertainty in α/M
3. **Inflationary dynamics**: 𝒟_inf uncertain by order of magnitude
4. **Torsion regularization**: ±30% in four-fermion coupling

#### Missing Physics
- Higher-loop corrections: Estimated <10% effect
- Non-minimal torsion couplings: Could modify predictions by ~20%
- Anisotropic inflation: May enhance/suppress parity violation
- Quantum back-reaction: Negligible for ω < 10⁻¹⁵ rad/s

### S7.5 Robustness Tests

#### Parameter Variations
We tested model predictions under:
1. ω₀ → 2ω₀: H₀ increases to 70.5 (still within 2σ)
2. α/M → 0.5α/M: Requires 𝒟_inf adjustment, same Λ_eff
3. γ → 0.5: Changes bounce density, minimal effect on late-time
4. Different e-folding: N = 45-65 accommodated with 𝒟_inf

#### Alternative Formulations
- Palatini vs metric formalism: <5% difference
- Different torsion decomposition: Changes coefficients by O(1)
- Alternative averaging schemes: 3ω² → (2-4)ω²

### S7.6 Comparison with Systematic Floors

Our predictions vs fundamental limits:

| Observable | Our Error | Systematic Floor | Margin |
|------------|-----------|------------------|---------|
| H₀ | 0.8 km/s/Mpc | 0.3 (Cepheid) | 2.7× |
| σ₈ | 0.016 | 0.005 (cosmic var) | 3.2× |
| CMB E-B | 7×10⁻⁵ μK² | 2×10⁻⁵ (foreground) | 3.5× |
| Galaxy A | 0.0006 | 0.0001 (shape noise) | 6× |

All predictions remain above fundamental systematic limits.

### S7.7 Combined Significance Calculation

Including all correlations and systematics:

$$\chi^2 = \sum_{ij} (O_i - T_i) C^{-1}_{ij} (O_j - T_j)$$

where C includes:
- Statistical errors
- Systematic errors (added in quadrature)
- Theory errors
- 20% data-theory covariance

Final detection significance by 2034:
- **Conservative**: 4.2σ (with all systematics)
- **Baseline**: 5.9σ (statistical + reduced systematics)
- **Optimistic**: 7.5σ (statistical only)

The model remains detectable at >4σ even in the most conservative scenario.