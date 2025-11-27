!!! release
    This is a Beta Release.
    Any model configuration and related source code mentioned in this page might change before the full release.
    Limited support is currently provided for this model. Its usage is only recommended for testing by experienced users and collaborators.

# ACCESS‑ISSM

![ACCESS‑ISSM model](/assets/model-config-logos/configurations-without-titles/access-issm.png){: .img-contain .white-background .round-edges .with-padding .intro-img loading="lazy"}

The ACCESS Ice-Sheet and Sea-Level System Model (ACCESS‑ISSM) is a global ice‑sheet and ice‑shelf model based on the [ISSM](/models/model_components/ice-sheet) framework.  It supports standalone ice dynamics and optional coupling to ocean and atmospheric forcing.

## Configurations 
ACCESS-ISSM provides the following released configurations:

- [Marine Ice-Sheet Model Intercomparison Project (MISMIP)](#mismip)

### Marine Ice-Sheet Model Intercomparison Project (MISMIP) {: #mismip }
The _MISMIP_ configuration reproduces the Marine Ice‑Sheet Model Intercomparison Project benchmark in ACCESS‑ISSM. It is intended for code regression tests, parameter experiments and numerical‑scheme development.

### 1.1 Domain & Physics

- **Geometry**: 800 km × 80 km Cartesian slab; flat bed at –1500 m; ocean at the downstream end.
- **Boundary conditions**: Marine ice sheet with grounding line migration; zero inflow at upstream wall; periodic lateral boundaries (y‑direction).
- **Flow law**: Glen’s \(n = 3\) unless stated otherwise.
- **Thermodynamics**: Isothermal (268 K) in the benchmark script.
- **Available solvers**:
  - **SSA**: default transient spin‑up.
  - **HO / FS**: optional higher‑order checks (after 3‑D extrusion).

### 1.2 Mesh Options

| Nominal Δx (m) | Label in driver                  | Typical vertex count | Use‑case                  |
| -------------- | -------------------------------- | -------------------- | ------------------------- |
| 2000           | `2km_viscous` or `2km_coulomb`   |  ≈ 160 × 16 k        | Fast test runs            |
| 1000           | `1km_viscous` or `1km_coulomb`   |  ≈ 320 × 32 k        | Standard benchmark        |
| 500            | `500m_viscous` or `500m_coulomb` |  ≈ 640 × 64 k        | Convergence studies       |
| 200            | `200m_viscous` or `200m_coulomb` |  ≈ 1600 × 160 k      | High‑resolution reference |

**Basal friction law** options:

- **Viscous** (power‑law, \(m = 3\)): `*_viscous` labels.
- **Coulomb** (plastic till): `*_coulomb` labels, using \(\tau\_b = C_0 + C\_c |\sigma\_n|\).

### 1.3 Workflow Steps

The driver script (see `mismip_driver.py`) is orchestrated by an *organizer* object.  Key stages:

1. **Mesh\_generation** → BAMG generates unstructured triangular mesh at chosen resolution.
2. **Parameterization** → masks & initial geometry via `Mismip.py`.
3. **Transient\_Steadystate** → 200 kyr relaxation with SSA.
4. *(optional)* **Transient\_extrude** → extrude to 3‑D and switch to HO.
5. **GlenSSA / GlenMOLHO / GlenHO** → Glen‐law transient experiments.
6. **ESTARSSA / ESTARHO** → dual‐E (star) rheology experiments.
7. **analyse** → automatic velocity‑field comparison and summary plots.

To **run only the first comparison plot** on Gadi, adapt the example job script below (full listing in docs):

```bash
qsub run_mismip_first.sh   # runs steps 1–7 and stops
```
> **Warning**  
> ACCESS‑ISSM is in alpha.  Expect API changes and incomplete documentation.  Use for testing and development only.

More details, examples and forcing files are available on the [ACCESS‑ISSM GitHub](https://github.com/ACCESS-NRI/access-issm).

[Run ACCESS‑ISSM](/models/run-a-model/run_access-issm){: .text-card }