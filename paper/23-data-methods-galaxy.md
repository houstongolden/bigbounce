## Data & Methods — Galaxy Spin Pipeline

### Datasets

**Current Analysis**:
- SDSS DR16: 823,752 spiral galaxies, $z < 0.25$, $r < 17.77$
- HST COSMOS: 42,186 galaxies, $0.2 < z < 1.2$, HST/ACS imaging
- JWST JADES: 2,200 galaxies, $1.0 < z < 3.0$, NIRCam deep fields
- JWST CEERS: 1,847 galaxies, $0.5 < z < 2.5$, NIRCam/MIRI

**Future Surveys**:
- LSST (2025+): Expected $10^8$ spiral galaxies to $z \sim 1$
- Euclid (ongoing): $\sim 10^7$ resolved galaxies
- Roman (2027+): High-resolution NIR imaging

### Morphological Classification

**Method**: Convolutional Neural Network (CNN) with human validation
1. **Architecture**: ResNet-50 backbone, trained on Galaxy Zoo labels
2. **Augmentation**: Rotation (8-fold), flip, noise injection
3. **Spiral identification**: 
   - S-index > 0.5 (spiral probability)
   - Ellipticity 0.1 < e < 0.8
   - No merger flags

**Spin direction determination**:
1. Spiral arm tracing using phase-angle method
2. Pitch angle sign determines handedness
3. Ambiguous cases (~15%) excluded

**Human-in-the-loop checkpointing**:
- 5% random sample verified by 3 experts
- Disagreement cases reviewed and excluded
- Periodic retraining with corrected labels

### Debiasing Strategy

**PSF and Inclination Corrections**:
```python
# Ellipticity debiasing
e_true = (e_obs - e_psf) / (1 - e_obs * e_psf)
inclination = arccos(sqrt(1 - e_true))
weight_incl = 1 / cos(inclination)  # up-weight edge-on
```

**Brightness and Size Cuts**:
- Magnitude limit: survey-specific completeness threshold
- Size cut: >5 pixels FWHM (resolution limit)
- S/N > 10 in spiral arms

**Sky Position Covariates**:
- Galactic latitude |b| > 20° (extinction)
- Ecliptic latitude correction for JWST
- Field-dependent systematics modeled

### Statistical Model

**Label-Noise Modeling**:
- Confusion matrix from validation set
- Asymmetric misclassification rates
- Survey-specific $\epsilon^{(s)}$ parameters

**Hierarchical Likelihood**:
```
Galaxy i in survey s:
P(CW|z,ψ) = 1/2[1 + δ_s + b_s(z)·A(z)·cos(ψ)]

Where:
- A(z) = A_0(1+z)^(-p)exp(-qz)
- δ_s ~ N(0, σ_δ²): survey offset
- b_s(z): selection efficiency
- ψ: angle from dipole axis
```

### Pre-registration

**Analysis Plan**: Registered at [OSF.io/xxxxx] before unblinding
- Primary: Dipole amplitude and axis
- Secondary: Redshift evolution parameters
- Null tests: Hemisphere splits, magnitude bins

**Version Control**:
- Code: Git SHA [`abc123...`]
- Data: Zenodo DOI [10.5281/zenodo.xxxxx]
- Pipeline: Docker image [`project/galaxy-spin:v1.0`]

### Systematic Tests

1. **Null Tests**:
   - Random rotation of galaxy positions
   - North/South Galactic hemisphere split
   - Even/odd RA split
   - Bright/faint magnitude split

2. **Injection-Recovery**:
   - Inject known asymmetry signal
   - Recover with pipeline
   - Validate error estimates

3. **Cross-Survey Validation**:
   - Overlapping sky regions
   - Consistent dipole axis
   - Compatible amplitudes after debiasing

### Data Products

**Per-Galaxy Catalog** (FITS format):
```
RA, Dec, z, z_err, spin_dir, spin_prob, 
morph_type, S_index, inclination, magnitude,
survey_id, quality_flag
```

**Binned Summary** (CSV format):
```
z_bin_center, z_bin_width, N_cw, N_ccw, 
survey_id, debias_weight, psf_quality_flag
```

All data products available at [Project repository URL] with full documentation.