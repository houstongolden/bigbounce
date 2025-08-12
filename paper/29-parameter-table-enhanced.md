## Parameters & Priors Table

| Group | Parameter | Symbol | Units | Prior | Used in |
|-------|-----------|--------|-------|-------|---------|
| **Parity-odd operator** | Loop coefficient | $(\alpha/M)$ | 1/E | log-uniform $[10^{-40}, 10^{-15}]$ eV$^{-1}$ | EB forecast, joint likelihood |
| **Rotation (body)** | Vorticity coefficient | $c_\omega$ | — | Fixed by Appendix R (this paper: $-1$) | Definitions only |
| **Spin model** | Amplitude | $A_0$ | — | $[0, 0.02]$ | Spin fit, Fig. 2 |
| | Redshift index | $p$ | — | $[0, 2]$ | Spin fit |
| | Redshift decay | $q$ | — | $[0, 2]$ | Spin fit |
| **Survey nuisances** | Survey offset | $\delta^{(s)}$ | — | $\mathcal{N}(0, 0.02^2)$ | Spin fit |
| | Label noise | $\epsilon^{(s)}$ | — | Beta(2, 20) | Spin fit |
| | Selection weight | $b^{(s)}(z_i)$ | — | $[0, 1]$ (provided) | Spin fit |
| **Probe normalization** | EB response | $\beta_E$ | — | 1 (default) | Joint likelihood |
| | Spin response | $\beta_G$ | — | 1 (default) | Joint likelihood |
| **Probe correlation** | Correlation | $\rho$ | — | $\{0, 0.3, 0.5\}$ (scan) | Joint likelihood |
| **ΛCDM (fits)** | Physical baryons | $\Omega_b h^2$ | — | $[0.019, 0.025]$ | MCMC |
| | Physical CDM | $\Omega_c h^2$ | — | $[0.10, 0.14]$ | MCMC |
| | Sound horizon angle | $100\theta_s$ | — | $[1.03, 1.05]$ | MCMC |
| | Reionization optical depth | $\tau$ | — | $[0.04, 0.12]$ | MCMC |
| | Scalar spectral index | $n_s$ | — | $[0.92, 1.00]$ | MCMC |
| | Scalar amplitude | $\ln(10^{10}A_s)$ | — | $[2.9, 3.2]$ | MCMC |
| **Extended (our model)** | Extra relativistic species | $\Delta N_{\text{eff}}$ | — | $[-0.5, 1.0]$ | MCMC |
| | Spatial curvature | $\Omega_k$ | — | $\mathcal{N}(0, 0.002)$ | MCMC |
| | Vorticity ratio | $(\omega/H)_0$ | — | $[0, 5 \times 10^{-11}]$ | MCMC (bound) |

### Notes on Priors

1. **Log-uniform priors**: Used for $(\alpha/M)$ to span many orders of magnitude without bias
2. **Gaussian priors**: Used for well-constrained parameters like $\Omega_k$
3. **Beta priors**: Natural for bounded parameters like error rates
4. **Fixed parameters**: $c_\omega$ is convention-dependent; we fix it in appendices
5. **Scan parameters**: $\rho$ is scanned over discrete values to show sensitivity

### Derived Parameters

| Parameter | Definition | Typical Value | Notes |
|-----------|------------|---------------|-------|
| Birefringence angle | $\beta = k_\beta \times (\alpha/M)$ | $0.30° \pm 0.11°$ | Minami & Komatsu (2020) |
| Dark energy scale | $\Lambda_{\text{obs}} = (\alpha/M) \times \mathcal{D}_{\text{inf}}$ | $(2.3 \text{ meV})^4$ | From dilution calculation |
| Initial rotation | $\Omega_0 = \sqrt{3\Lambda_{\text{eff}}}$ | $\sim 10^{-18}$ rad/s | From baby universe |
| Hubble constant | $H_0$ | $69.2 \pm 0.8$ km/s/Mpc | Our model fit |
| Matter clustering | $\sigma_8$ | $0.785 \pm 0.016$ | Our model fit |

### Parameter Correlations

Strong correlations exist between:
- $A_0$ and $\delta^{(s)}$: Degenerate at single redshift
- $p$ and $q$: Both control redshift evolution  
- $\Delta N_{\text{eff}}$ and $H_0$: Both shift CMB peaks
- $\Omega_k$ and distance measures: Geometric degeneracy

These are broken by:
- Multiple redshift bins (breaks $A_0$-$\delta^{(s)}$)
- Wide redshift range (separates $p$ and $q$)
- Multiple CMB peaks (breaks $\Delta N_{\text{eff}}$-$H_0$)
- BAO + SNe (breaks geometric degeneracies)