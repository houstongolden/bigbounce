## Joint Likelihood & Probe Correlation

### Combined Analysis Framework

We combine CMB E-B correlations and galaxy spin asymmetries using a correlated likelihood that accounts for potential systematic correlations between the two probes.

### Correlated Gaussian Likelihood

Both probes measure the same underlying parity violation amplitude $A$ with potentially different normalizations:

**Data vector**: $\mathbf{d} = (\hat{A}_E, \hat{A}_G)^T$

**Model**: $\mathbf{m}(A) = A \cdot (\beta_E, \beta_G)^T$

where $\beta_E = \beta_G = 1$ if both probes are normalized to measure the same physical quantity.

**Covariance matrix**:
$$\Sigma = \begin{pmatrix}
\sigma_E^2 & \rho\,\sigma_E\sigma_G \\
\rho\,\sigma_E\sigma_G & \sigma_G^2
\end{pmatrix}$$

where $\rho \in [-1, 1]$ is the correlation coefficient between systematic errors.

### Maximum Likelihood Estimator

The likelihood is:
$$-2\ln\mathcal{L}(A) = (\mathbf{d} - \mathbf{m})^T\Sigma^{-1}(\mathbf{d} - \mathbf{m}) + \text{const}$$

The maximum likelihood estimate and uncertainty are:
$$\hat{A} = \frac{\mathbf{T}^T\Sigma^{-1}\mathbf{d}}{\mathbf{T}^T\Sigma^{-1}\mathbf{T}}, \quad \sigma_A^2 = \frac{1}{\mathbf{T}^T\Sigma^{-1}\mathbf{T}}$$

where $\mathbf{T} = (\beta_E, \beta_G)^T$.

### Detection Significance

The combined detection significance is:
$$Z = \frac{\hat{A}}{\sigma_A}$$

**Special cases**:
- $\rho = 0$ (independent): $Z^2 = Z_E^2 + Z_G^2$ (quadrature addition)
- $\rho = 1$ (fully correlated): $Z = \text{min}(Z_E, Z_G)$ (no improvement)
- $\rho < 0$ (anti-correlated): Can give $Z > \sqrt{Z_E^2 + Z_G^2}$

### Correlation Modeling

We consider three correlation scenarios:

**1. Optimistic ($\rho = 0$)**: 
- Independent systematic errors
- Different sky coverage
- Different redshift ranges
- Maximum improvement from combination

**2. Moderate ($\rho = 0.3$)**:
- Some shared systematics (e.g., cosmology)
- Partial sky overlap
- Correlated large-scale structure
- Realistic baseline scenario

**3. Conservative ($\rho = 0.5$)**:
- Significant systematic correlation
- Shared theoretical uncertainties
- Common foreground residuals
- Minimum guaranteed improvement

### Multi-Bin Extension

For multiple $\ell$ bins (EB) and redshift bins (spins), we extend to block matrices:

$$\mathbf{d} = (\hat{A}_{E,\ell_1}, ..., \hat{A}_{E,\ell_n}, \hat{A}_{G,z_1}, ..., \hat{A}_{G,z_m})^T$$

The covariance becomes a block matrix:
$$\Sigma = \begin{pmatrix}
\Sigma_{EE} & \Sigma_{EG} \\
\Sigma_{GE} & \Sigma_{GG}
\end{pmatrix}$$

where:
- $\Sigma_{EE}$: EB covariance between $\ell$ bins
- $\Sigma_{GG}$: Galaxy spin covariance between $z$ bins  
- $\Sigma_{EG}$: Cross-covariance between probes

### Implementation

```python
def joint_significance(AE, sE, AG, sG, rho=0.0, betaE=1.0, betaG=1.0):
    """
    Calculate joint detection significance with correlation.
    
    Returns: (Ahat, sigma_A, Z)
    """
    d = np.array([AE, AG])
    T = np.array([betaE, betaG])
    Sigma = np.array([[sE**2, rho*sE*sG],
                      [rho*sE*sG, sG**2]])
    
    iS = np.linalg.inv(Sigma)
    Ahat = (T @ iS @ d) / (T @ iS @ T)
    sA = 1.0 / np.sqrt(T @ iS @ T)
    Z = Ahat / sA
    
    return Ahat, sA, Z
```

### Forecast Results

Using projected sensitivities for 2030:

| Probe | Individual $\sigma$ | Individual $Z$ |
|-------|-------------------|----------------|
| CMB EB (CMB-S4) | $1.0 \times 10^{-4}$ μK² | 2.0σ |
| Galaxy spins (LSST Y1) | $8.0 \times 10^{-4}$ | 3.8σ |

**Combined significance**:
- $\rho = 0.0$: $Z = 4.3\sigma$
- $\rho = 0.3$: $Z = 4.1\sigma$  
- $\rho = 0.5$: $Z = 3.9\sigma$

Even with conservative correlation assumptions, we achieve $>3.5\sigma$ detection by 2030.

### Advantages of Joint Analysis

1. **Increased significance**: Even modest correlation gives substantial improvement
2. **Cross-validation**: Different systematics help identify spurious signals
3. **Breaking degeneracies**: Different redshift/scale dependence
4. **Robustness**: Detection doesn't rely on single probe

This joint analysis framework can be extended to include additional parity-odd observables as they become available.