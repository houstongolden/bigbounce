## Parameter Summary and Priors

This section provides a single source of truth for all model parameters used in our framework.

### Model Parameters

| Parameter | Symbol | Meaning | Units | Prior | Section | Value/Constraint |
|-----------|--------|---------|-------|-------|---------|------------------|
| **Fundamental Theory** |
| Parity-odd coefficient | $\alpha/M$ | Loop quantum gravity parity-odd operator | $\text{energy}^{-1}$ | Log-uniform or Gaussian | 2.1, App. L | Phenomenological |
| Vorticity coefficient | $c_\omega$ | Coefficient in $\Lambda_{\text{eff}}$ equation | — | Fixed by conventions | 2.3, App. R | $c_\omega = -1$ |
| Immirzi parameter | $\gamma$ | Barbero-Immirzi parameter | — | Real, $\gamma \approx 0.2375$ | 2.1 | From black hole entropy |
| **Galaxy Spin Model** |
| Present amplitude | $A_0$ | Galaxy spin asymmetry at $z=0$ | — | Uniform(0, 0.02) | 3.2, App. C | $0.0031_{-0.0013}^{+0.0013}$ |
| Power-law index | $p$ | Redshift evolution exponent | — | Uniform(0, 2) | 3.2, App. C | $0.52_{-0.27}^{+0.27}$ |
| Exponential decay | $q$ | Redshift decay rate | — | Uniform(0, 2) | 3.2, App. C | $0.48_{-0.33}^{+0.33}$ |
| Survey offset | $\delta^{(s)}$ | Systematic bias per survey | — | $\mathcal{N}(0, \sigma_\delta^2)$ | App. C | Survey-dependent |
| Label noise | $\epsilon^{(s)}$ | Misclassification rate | — | Beta(2, 50) | App. C | $\sim 0.04$ typical |
| Selection efficiency | $b^{(s)}(z)$ | Visibility function | — | Weakly regularized | App. C | Survey-dependent |
| **Cosmological Parameters** |
| Hubble constant | $H_0$ | Present expansion rate | km/s/Mpc | Gaussian(70, 5) | 3.3 | $69.2 \pm 0.8$ |
| Matter density | $\Omega_m$ | Matter fraction | — | Gaussian(0.3, 0.02) | 3.3 | $0.315 \pm 0.007$ |
| Curvature | $\Omega_k$ | Spatial curvature | — | Gaussian(0, 0.002) | 3.3 | $0.001 \pm 0.002$ |
| Extra relativistic species | $\Delta N_{\text{eff}}$ | Additional neutrino species | — | Gaussian(0, 0.3) | 3.3 | $0.3 \pm 0.2$ |
| Vorticity | $\omega/H$ | Cosmic rotation rate | — | Bounded by isotropy | 2.3, 3.3 | $< 5 \times 10^{-11}$ |
| **Observational Constraints** |
| CMB E-B amplitude | $C_\ell^{EB}$ | E-B correlation at $\ell=2-4$ | $\mu\text{K}^2$ | Derived from $\alpha/M$ | 3.1 | $\sim 2 \times 10^{-4}$ |
| Birefringence angle | $\beta$ | Cosmic birefringence | degrees | Related to $\alpha/M$ | 3.1 | $0.30 \pm 0.11$ |

### Priors and Assumptions

1. **Convention Choices**:
   - Metric signature: $(-, +, +, +)$
   - Levi-Civita: $\varepsilon^{0123} = +1$
   - 1+3 covariant definitions as in Appendix R

2. **Physical Bounds**:
   - $A_0 \geq 0$ (asymmetry is non-negative)
   - $\gamma$ real (unitarity requirement)
   - $\omega/H < 10^{-10}$ (isotropy constraint)

3. **Regime of Validity**:
   - Almost-FLRW background
   - Small vorticity and shear
   - Perfect fluid matter at background level
   - Rotation affects only parity-odd observables

### Joint Constraints

When combining CMB E-B and galaxy spin measurements, we use the joint likelihood framework from Appendix J with correlation parameter $\rho \in [0, 0.5]$ to account for potential systematic correlations.

### Notes

- All error bars represent 68% confidence intervals unless otherwise stated
- Preliminary values based on current data; will be updated with future observations
- The parity-odd coefficient $\alpha/M$ is treated phenomenologically pending full UV completion