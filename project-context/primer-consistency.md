# primer-consistency.md

*(Master primer for reviewers — complete theory summary + consistency checklist. No new naming conventions introduced in the main text.)*

---

## 0) Purpose

* Give a **single, authoritative overview** of the paper’s theory, equations, assumptions, predictions, and datasets.
* Enable a reviewer/agent to **audit every `/paper/*.md` section** for consistency (notation, units, definitions, figures, and data).
* **Do not** introduce any new names in the body text (keep the current symbols and phrasing). Any optional naming appears only in the **Discussion/Glossary** sections.

---

## 1) Conventions & Assumptions

**Units & constants**

* Natural units: $c=\hbar=1$.
* $G$ = Newton’s constant; $M_{\rm Pl} = 1/\sqrt{8\pi G}$.
* Energy-density units stated in **eV$^4$** or **eV$^2$** where appropriate (be explicit).

**Geometry & indices**

* Metric signature: $(-+++) $.
* Levi-Civita: $\varepsilon^{0123}=+1$.
* Curvature: $R^\rho{}_{\sigma\mu\nu}$, torsion $T^\lambda{}_{\mu\nu}$, contortion $K_{\mu\nu}{}^\lambda$.
* Barbero–Immirzi parameter: $\gamma$.

**Background & averaging**

* Homogeneous/isotropic background with **small global vorticity** $\omega$ (1+3 covariant or Bianchi-type small-anisotropy limit).
* Spatial averaging restores effective isotropy at background level; vorticity terms enter to **second order** in small quantities where required.

---

## 2) Core Theory (first principles → effective Λ)

### 2.1 Einstein–Cartan–Holst setup

* Start with EC–Holst action; torsion couples algebraically to fermionic spin.
* Eliminating torsion yields the axial–axial contact term:

$$
\mathcal L_{AA}
= -\frac{3\pi G}{2}\,\frac{\gamma^2}{\gamma^2+1}\,J_A^2,
\quad J_A^\mu = \bar\psi \gamma^\mu \gamma^5 \psi .
$$

### 2.2 Parity-odd one-loop term

* Radiative corrections generate a **dimension-five parity-odd** operator:

$$
\mathcal L_{\rm odd} \;=\; \frac{\alpha}{M}\,
\varepsilon^{\mu\nu\rho\sigma} K_{\mu\nu}{}^{ab} R_{\rho\sigma ab}.
$$

* **Regularization note**: use a regulator-transparent derivation (dim-reg) and clarify treatment of **Nieh–Yan** counterterms to keep the finite piece explicit.
* Dimensional analysis: $\alpha$ dimensionless; overall coefficient has mass dimension $-1$.

### 2.3 Inflationary dilution

* Early-time parity-odd effects are **diluted by inflation**.
* Define the **dilution factor** $\mathcal D_{\rm inf}$ (function of e-folds $N$, reheating history, and relevant scaling power).
* The constant part left over today is:

$$
\left(\frac{\alpha}{M}\right)\mathcal D_{\rm inf}.
$$

### 2.4 Rotating background contribution

* In 1+3 covariant dynamics with small vorticity, the **effective acceleration** acquires a term proportional to $\omega^2$.
* At background level this is captured as:

$$
\Lambda_{\rm eff} = \Lambda + 3\,\omega^2,
$$

after isotropic averaging and to leading order in $\omega$.

### 2.5 Effective cosmological constant (final)

* Combine rotation and loop-dilution:

$$
\boxed{\;\Lambda_{\rm eff} \;=\; 3\,\omega^2 \;+\; \Big(\frac{\alpha}{M}\Big)\mathcal D_{\rm inf}\;}
$$

* **Interpretation**: today’s dark-energy scale arises from a tiny rotational energy plus a residual loop-induced constant that survived inflationary dilution. No hand-tuned bare Λ is required.

---

## 3) Derived Dynamics & Parameterizations

### 3.1 Background expansion and distances

* Use FLRW background with $\Lambda_{\rm eff}$ above.
* Distances and $H(z)$ follow standard integrals with $\Lambda \to \Lambda_{\rm eff}$.
* **Sign expectations**: a small positive $\omega^2$ **increases** $H_0$; the loop piece shifts late-time distances slightly.

### 3.2 Growth of structure

* Linear growth $D(a)$ and $f\sigma_8(z)$ modified via the changed background $H(z)$; for small changes, first-order response suffices.
* Expect **slightly lower** $\sigma_8$ relative to Planck ΛCDM if $H_0$ is raised (helps with the S$_8$ tension).

### 3.3 Vorticity energy fraction

* Define $\Omega_\omega(z)$ = rotational energy density / critical density.
* Parameterize a slowly varying trajectory with $\Omega_{\omega,0} \sim 0.02$ (tunable; keep a single calibrated curve across paper).

### 3.4 Galaxy spin-handedness prediction

* Redshift dependence:

$$
A(z) \;\approx\; 0.003\,(1+z)^{-0.5}\,e^{-z/2}.
$$

* This is the **model prediction** to compare with SDSS / Pan-STARRS / JWST / LSST.

### 3.5 CMB EB correlations

* Parity-odd term sources a **low-$\ell$ EB amplitude**.
* Forecast significance combined with galaxy spins:

$$
\sigma_{\rm combined} \;=\;
\sqrt{\sigma_{\rm CMB}^2 + \sigma_{\rm galaxy}^2}.
$$

---

## 4) Central Numerical Targets (used throughout)

These are the **current working values** used across figures/tables; keep them consistent unless we update them globally:

* $H_0 \approx 69.2 \pm 0.8\;{\rm km\,s^{-1}\,Mpc^{-1}}$.
* $\sigma_8 \approx 0.785 \pm 0.016$.
* $\Omega_{\omega,0} \approx 0.02$ (illustrative; ensure the same curve is used in all plots).
* $A(z)$ as above.

*(If any of these change, update every dependent figure/table and the text wherever quoted.)*

---

## 5) Observational Predictions & Tests

* **Hubble & growth tensions**: simultaneous **reduction** of H$_0$ and S$_8$ tensions relative to Planck ΛCDM via small $\omega^2$ and adjusted late-time background.
* **Spin-handedness**: statistically small but increasing detectability with LSST depth and area.
* **CMB EB**: low-$\ell$ EB amplitude detectable by LiteBIRD / CMB-S4 if parity-odd loop term is present.
* **Early UMPMBHs / early galaxies**: torsion-supported early-time dynamics + bounce-like behavior (if included) make early structure formation less fine-tuned.

---

## 6) Naturalness & Fine-Tuning

* Compare **observed** vs **natural** scales across models:

  * ΛCDM bare Λ → extreme fine-tuning ($\sim10^{120}$).
  * Quintessence → improved but still tuned.
  * This model → residual loop constant $(\alpha/M)\mathcal D_{\rm inf}$ + tiny rotation; **significantly less tuning**.
* Maintain one **fine-tuning score** definition across the paper:

$$
{\rm Score} \;=\; \frac{\rm Natural\ scale}{\rm Observed\ value}.
$$

---

## 7) Falsification Criteria (hard tests)

* **Null EB** at low-$\ell$ inconsistent with forecast sensitivity.
* **No spin-handedness** excess at LSST depth within predicted $A(z)$ band.
* **Incompatible H$_0$/$\sigma_8$** posteriors when fitting the same $\Omega_\omega(z)$ across probes.
* **Rotation constraints** that drive $\Omega_{\omega,0}\to 0$ while preserving our $H_0$ and $\sigma_8$ shifts → model tension.

---

## 8) Figures, Data & File-Level Consistency

**Figures on site** (ensure these sync with spreadsheets and text):

* **Fig 1 (Holst / torsion activation / parity evolution)**

  * Caption must state the exact 4-fermion prefactor.
  * No numeric recalc needed unless the prefactor changed.

* **Fig 2 (Galaxy spin analysis)**

  * Replace the *prediction* series with $A(z)$ above.
  * Keep observational points; recompute significance.

* **Fig 3A (Tension overview)**

  * Update entries to $H_0=69.2$, $\sigma_8=0.785$ for the spin–torsion row.

* **Fig 3B (Detailed validation)**

  * Ensure $H(z)$ and $f\sigma_8(z)$ curves reflect the same parameters as Fig 3A.

* **Fig 6 (Parameter naturalness)**

  * Panel C: show $\Omega_\omega(z)$ trajectory (rising to $\sim0.02$ today).
  * Panel D: update fine-tuning row for this model with low score.

* **Fig 7 (Detection timeline)**

  * Keep combined significance formula; ensure CMB + galaxy values are consistent with forecasts.

**Data checks to enforce in build/CI**

* Presence/format of required columns per figure.
* **Formula checks** (e.g., combined significance).
* Monotonic or range checks where applicable (e.g., $0 \le A(z)\le 0.05$).
* Single source of truth for $H_0, \sigma_8, \Omega_{\omega,0}$.

---

## 9) Notation Reference (must be identical across all files)

| Symbol                 | Meaning                                        |
| ---------------------- | ---------------------------------------------- |
| $\Lambda_{\rm eff}$    | Effective cosmological constant today.         |
| $\omega$               | Global vorticity (background, small).          |
| $\Omega_\omega(z)$     | Rotation-energy fraction.                      |
| $\alpha/M$             | Loop coefficient of parity-odd term.           |
| $\mathcal D_{\rm inf}$ | Inflationary dilution factor.                  |
| $\mathcal L_{AA}$      | Axial–axial contact interaction from EC–Holst. |
| $\mathcal L_{\rm odd}$ | Parity-odd torsion–curvature operator.         |
| $A(z)$                 | Galaxy spin-handedness asymmetry vs redshift.  |
| $H_0,\, \sigma_8$      | Standard cosmological parameters.              |

*(Keep symbol shapes: calligraphic $\mathcal{D}$, roman $\Lambda_{\rm eff}$, etc.)*

---

## 10) Section-by-Section Audit Tasks

For each `/paper/*.md` file:

1. **00-abstract.md**

   * Claims match numerical targets (H$_0$, $\sigma_8$, detectability).
   * No symbol introduced without definition later.

2. **01-introduction.md**

   * Motivation (tensions, early structures) aligns with predictions.
   * No premature claims beyond results.

3. **02-theoretical-framework.md**

   * EC–Holst setup, torsion elimination, $\mathcal L_{AA}$ correct.
   * $\mathcal L_{\rm odd}$ stated with correct dimensions and regularization note.
   * Define $\mathcal D_{\rm inf}$; show how the constant piece arises.
   * Conclude with $\Lambda_{\rm eff}=3\omega^2+(\alpha/M)\mathcal D_{\rm inf}$.

4. **03-observational-predictions.md**

   * Present $A(z)$, EB expectations, and parameter shifts (H$_0$, $\sigma_8$).
   * Forecasts correspond to Fig 2 and Fig 7.

5. **04-enhanced-derivations.md**

   * Show torsion elimination detail; list assumptions.
   * 1+3 covariant derivation giving $+3\omega^2$ term; clarify ordering and averaging.

6. **05-systematic-analysis.md**

   * Enumerate systematics (spin classification bias, shear calibration, EB leakage, foregrounds).
   * Explain mitigation and how pre-registration avoids p-hacking.

7. **06-model-comparison.md**

   * Head-to-head with ΛCDM/quintessence/mod-gravity; keep the **same fine-tuning score** definition.

8. **07-detection-timeline.md**

   * Timeline values = spreadsheet; combined significance formula enforced.

9. **08-falsification-criteria.md**

   * Itemize the hard falsifiers above; keep thresholds.

10. **09-theoretical-implications.md**

    * Discuss early structure, UMPMBHs, bounce-like behavior (if included) consistently with the framework.

11. **09a-discussion.md**

    * Summarize mechanism, scale-setting, and practical implications.
    * If any optional naming is included, keep it **here only**; do not propagate upstream.

12. **10-conclusions.md**

    * Quantitative summary; no new symbols.

13. **11-acknowledgments.md**

    * N/A.

14. **12-glossary.md**

    * Ensure every symbol above appears with a concise definition; mark novelty subtly.

---

## 11) Reviewer Output Requirements

* **Per-file issue list** with: file, line (if possible), issue type (notation/units/definition/data/claim), suggested fix.
* **Global consistency report** summarizing counts, themes, and a short patch plan.
* **Figure/data sync report**: which spreadsheets/JSONs were inconsistent; proposed corrections.

---

## 12) Audit Prompt (paste into your agent)

```
You are auditing the cosmology paper in `/paper`. Use `primer-consistency.md` as the single source of truth.

Do the following:
1) Read all files (`00-abstract.md` … `12-glossary.md`).
2) Verify exact consistency with Sections 1–10 of `primer-consistency.md`:
   - Symbols: Λ_eff, ω, Ω_ω(z), α/M, 𝒟_inf, A(z), etc.
   - Core equations: L_AA, L_odd, Λ_eff form.
   - Targets: H0=69.2±0.8, σ8=0.785±0.016, Ω_ω0≈0.02, A(z) model.
   - Figures: captions/text match spreadsheets and formulas.
   - Naturalness/fine-tuning definition is identical across sections.
3) Produce:
   a) Per-section bullet list of inconsistencies (file + line if possible) with exact fix suggestions.
   b) A “Global Consistency Report” summarizing issues and a batch-fix plan.
   c) A “Figure/Data Sync Report” listing any data mismatches and required spreadsheet updates.
4) Do not introduce new naming conventions into the main text. If any optional names appear, ensure they are restricted to Discussion/Glossary only.
```

---

**End of primer-consistency.md**
