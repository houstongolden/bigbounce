## Appendix R: 1+3 Covariant Rotation Note

### R.1 Setup and Assumptions

We work in the 1+3 covariant formalism with a timelike congruence $u^a$ (normalized $u^a u_a = -1$). Define:
- Expansion: $\Theta \equiv \nabla_a u^a = 3H$
- Shear tensor: $\sigma_{ab}$ (symmetric, traceless, orthogonal to $u^a$)
- Vorticity tensor: $\omega_{ab}$ (antisymmetric, orthogonal to $u^a$)
- Magnitudes: $\sigma^2 \equiv \tfrac{1}{2}\sigma_{ab}\sigma^{ab}$, $\omega^2 \equiv \tfrac{1}{2}\omega_{ab}\omega^{ab}$

We assume an almost-FLRW background with **small** $\sigma_{ab}, \omega_{ab}$ and perfect-fluid matter.

### R.2 Constraint Equation (Generalized Friedmann)

The Gauss-Codazzi constraint gives:

$$H^2 = \frac{8\pi G}{3}\rho + \frac{\Lambda}{3} - \frac{k}{a^2} + \frac{1}{3}(\sigma^2 - \omega^2)$$

Equivalently, if one packages the kinematic correction into an "effective" constant:

$$\frac{\Lambda_{\rm eff}}{3} \equiv \frac{\Lambda}{3} + \frac{1}{3}(\sigma^2 - \omega^2)$$

Therefore:

$$\boxed{\Lambda_{\rm eff} = \Lambda + (\sigma^2 - \omega^2)}$$

### R.3 Raychaudhuri Equation (Acceleration)

$$\dot{\Theta} + \frac{1}{3}\Theta^2 + 2(\sigma^2 - \omega^2) + 4\pi G(\rho + 3p) - \Lambda = 0$$

The signs in the two equations are consistent: vorticity **reduces** $H^2$ (centrifugal "anti-focusing").

### R.4 Fixing the Coefficient Used in the Main Text

If shear is negligible at the background level ($\sigma^2 \to 0$), then:

$$\boxed{\Lambda_{\rm eff} = \Lambda - \omega^2} \quad \text{(this appendix's conventions)}$$

Therefore, if the body of the paper carries a symbolic coefficient $c_\omega$ as:

$$\Lambda_{\rm eff} = \Lambda + c_\omega\,\omega^2$$

then **with these conventions** $c_\omega = -1$. Different sign/factor conventions in the literature are absorbed here; this appendix pins the choice used in our equations/figures.

### R.5 Isotropy Bound and Practical Implications

CMB/Bianchi analyses imply $(\omega/H)_0 \lesssim \text{few} \times 10^{-11}$ (95% CL). Hence:

$$\frac{|c_\omega\,\omega^2|}{H_0^2} \lesssim \mathcal{O}(10^{-20})$$

Rotation is **negligible for background expansion** and should be probed via **parity-odd observables** (EB, galaxy-spin handedness), not via late-time $H(z)$.

### References

- Ellis, G.F.R. & van Elst, H. (1999), "Cosmological models", NATO Sci. Ser. C 541, 1-116 [gr-qc/9812046]
- Tsagas, C.G., Challinor, A. & Maartens, R. (2008), "Relativistic cosmology and large-scale structure", Phys. Rep. 465, 61-147
- Saadeh, D. et al. (2016), "How isotropic is the Universe?", Phys. Rev. Lett. 117, 131302
- Planck Collaboration (2020), "Planck 2018 results. VII. Isotropy and statistics", A&A 641, A7