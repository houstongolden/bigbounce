## Appendix L: Parity-Odd Loop Term and Nieh-Yan Scheme Note

### L.1 EC-Holst → Axial-Axial Contact (Parity-Even)

Start from the Einstein-Cartan-Holst action (real Immirzi $\gamma$):

$$S = \frac{1}{2\kappa}\int e^I \wedge e^J \wedge {}^*R_{IJ} + \frac{1}{2\kappa\gamma}\int e^I \wedge e^J \wedge R_{IJ} + S_\psi[e,\omega,\psi], \quad \kappa = 8\pi G$$

Vary w.r.t. $\omega$, eliminate torsion (algebraic), and obtain the axial-axial contact:

$$\boxed{\mathcal{L}_{AA} = -\frac{3\pi G}{2} \cdot \frac{\gamma^2}{\gamma^2+1} \cdot J_A^2}, \quad J_A^\mu = \bar{\psi}\gamma^\mu\gamma^5\psi$$

up to conventional sign choices ($\varepsilon^{0123} = +1$).

### L.2 Parity-Odd Sector, Holst vs Nieh-Yan, and Regulator

With fermions, the Holst density differs from the **Nieh-Yan** 4-form:

$$\mathcal{NY} \equiv d(e^I \wedge T_I) - e^I \wedge e^J \wedge R_{IJ}$$

by more than a boundary term: chiral fermions generate a **torsional axial anomaly** (the "Nieh-Yan anomaly"), which is quadratically divergent in cutoff schemes. To make the finite piece unambiguous:

- Work in **dimensional regularization** (or specify Pauli-Villars with explicit subtractions)
- Introduce a **renormalized** coefficient $c_{\rm NY}(\mu)$ multiplying $\mathcal{NY}$
- State a **renormalization condition** (e.g., match to an early-time calculation and the inflationary dilution that leaves today's constant piece)

We then write the effective parity-odd operator schematically as:

$$\boxed{\mathcal{L}_{\rm odd} = c_{\rm NY}(\mu)\,\mathcal{NY} \equiv \frac{\alpha(\mu)}{M} \cdot \varepsilon^{\mu\nu\rho\sigma}K_{\mu\nu}{}^{ab}R_{\rho\sigma ab} + \text{(total derivatives)}}$$

with mass dimension $-1$ overall. 

### L.3 Renormalization and Physical Interpretation

The coefficient has the structure:

$$\frac{\alpha}{M} = \frac{g^2}{32\pi^2} \cdot \frac{\gamma}{M} \cdot \ln\left(\frac{\Lambda^2}{\mu^2}\right) + \delta_{\rm NY}(\mu)$$

where:
- $g$ is the axial-torsion coupling fixed by EC geometry
- $\Lambda$ is a UV scale (e.g., LQG area-gap mass)
- $\mu$ is the renormalization scale
- $\delta_{\rm NY}(\mu)$ is the finite Nieh-Yan counterterm

### L.4 Connection to Dark Energy

We fix the renormalized coefficient by requiring that the observed dark energy scale emerges after inflationary dilution:

$$\left(\frac{\alpha}{M}\right)_{\rm ren} \times \mathcal{D}_{\rm inf} = \Lambda_{\rm obs} \approx (2.3 \text{ meV})^4$$

where $\mathcal{D}_{\rm inf}$ accounts for the cumulative effect of cosmic expansion from the bounce through inflation to today.

### L.5 Important Clarifications

- Clarify **minimal vs non-minimal** fermion couplings (a non-minimal parameter can re-weight axial vs vector pieces)
- Keep $\gamma$ real to avoid unitarity pathologies
- In forecasts we treat $\alpha/M$ as a **phenomenological parameter** constrained by EB/spin data; the UV/RG discussion is contained in this appendix

### References

- Freidel, L., Minic, D. & Takeuchi, T. (2005), "Quantum gravity, torsion, parity violation and all that", Phys. Rev. D 72, 104002
- Mercuri, S. (2006), "Fermions in the Ashtekar-Barbero connection formalism for arbitrary values of the Immirzi parameter", Phys. Rev. D 73, 084016
- Magueijo, J. & Złośnik, T. (2019), "Parity violating Friedmann Universes", Phys. Rev. D 100, 084036
- Calcagni, G. & Mercuri, S. (2009), "The Barbero-Immirzi field in canonical formalism of pure gravity", Phys. Rev. D 79, 084004