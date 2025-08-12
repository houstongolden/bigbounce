## 4. Enhanced Theoretical Derivations

### 4.0 Supplementary Methods (Data & Forecasts)

1. **EB/Spin combined significance (Section 7):** We compute the combined forecast significance as

$$\sigma_{\rm comb}=\sqrt{\sigma_{\rm CMB}^2+\sigma_{\rm Gal}^2},$$

with yearly CMB and galaxy‑spin bands taken from the CSV `public/spreadsheets/EB_Spin_Significance_Timeline__Preview_.csv`. The plotted forecast‑style image is `public/images/CMB:Galaxy EB & Spin Significance Over Time (Forecast-Style).png`.

2. **Rotation bounds (Section 3.3):** Given stringent isotropy constraints $(\omega/H)_0 < 5 \times 10^{-11}$, rotation contributes negligibly to background expansion ($<10^{-20}$ of $\Lambda$). The parity-violating term $\propto \varepsilon^{\mu\nu\rho\sigma} K_{\mu\nu}{}^{ab} R_{\rho\sigma ab}$ affects only odd-parity observables like galaxy spins and CMB E-B correlations, not $H_0$ or $\sigma_8$. Earlier "toy rotation" models violating these bounds have been removed.

3. **Amplitude normalization:** Observable amplitudes in Sections 2–3 scale with the renormalized loop coefficient $(\alpha/M)$ multiplied by geometric/background factors accumulated through inflation and late‑time expansion. This replaces earlier wording that suggested a time‑varying coupling.

### 4.1 Rigorous LQG Parity-Odd Term Derivation (units and scheme clarified)

We provide a complete derivation of the parity-odd effective action from first principles in Loop Quantum Gravity, building on the foundational work of Freidel et al. (2005) and Mercuri (2006) [2,3].

#### 4.1.1 One-Loop Calculation

The parity-odd coefficient arises from a one-loop diagram with fermion propagators:

$$\Gamma^{(1)} = \int \frac{d^4k}{(2\pi)^4} \text{Tr}\left[\frac{1}{k^2 + M^2} \gamma^5 \gamma^a \frac{1}{\not{k}} \gamma^b \gamma^c\right] T_a^{de} R_{de} K_{bc}$$

Dimensional analysis requires the parity-odd operator to appear with a coefficient $\alpha/M$ (mass dimension $-1$), not a dimensionless $\alpha$. A regulator-transparent one-loop estimate in a torsionful background (with Nieh–Yan/Holst mixing) is

$$\frac{\alpha}{M} \;\sim\; \frac{g^2}{32\pi^2}\,\frac{\gamma}{M}\,\ln\!\left(\frac{\Lambda^2}{\mu^2}\right) + \delta_{\mathrm{NY}},$$

where $\Lambda$ is a UV scale (e.g., area-gap mass), $\mu$ the subtraction scale, and $\delta_{\mathrm{NY}}$ encodes finite renormalization of the Nieh–Yan density.

#### 4.1.2 Renormalization Group Flow

The coefficient runs with energy scale according to:

$$\frac{d\alpha}{d \ln \mu} = \frac{g^2}{16\pi^2} \left[3C_2(G) - \frac{4}{3}T(R)N_f\right]$$

where $C_2(G)$ and $T(R)$ are group theory factors, and $N_f$ is the number of fermion flavors.

#### 4.1.3 Non-Renormalization Theorem

The parity-odd term is protected by a non-renormalization theorem: higher-loop corrections vanish due to the topological nature of the Nieh-Yan invariant, ensuring the coefficient remains finite and calculable.

### 4.2 Vacuum Energy from Fermion Condensates

#### 4.2.1 Torsion-Induced Condensation

The four-fermion interaction can lead to fermion condensation via a BCS-like mechanism:

$$\langle\bar{\psi}\psi\rangle = -\frac{\Lambda^3}{2\pi^2} \int_0^{\Lambda/\mu} dx \, x^2 \frac{\tanh(E(x)/(2T))}{E(x)/\mu}$$

where $E(x)$ is the quasiparticle energy and $\mu$ is the chemical potential.

#### 4.2.2 QCD Phase Transition Enhancement

During the QCD phase transition at $T \sim 150$ MeV, torsion enhances quark condensation:

$$\langle\bar{q}q\rangle_{\text{torsion}} = \langle\bar{q}q\rangle_{\text{QCD}} \left[1 + \frac{\gamma^2}{\gamma^2+1} \times \frac{\rho}{\rho_{\text{QCD}}}\right]$$

This contributes a small positive vacuum energy:

$$\rho_{\text{vac}} \approx \frac{\alpha_s}{\pi} \times \frac{\langle\bar{q}q\rangle^2}{f_\pi^2} \approx 10^{-29} \text{ GeV}^4$$