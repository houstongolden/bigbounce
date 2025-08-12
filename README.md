# BigBounce Data Pipeline (CSV → JSON → XLSX)

This repository serves a static scientific site (paper + figures) and now includes a safe, opt‑in data pipeline.

## Quick start

1) Install Python deps

```bash
pip3 install -r requirements.txt
```

2) Build data

```bash
npm run build:data
# or
python3 scripts/build_data.py
```

Outputs are written to:
- `public/data/figure_{id}/{panel}.json` (chart JSON)
- `public/downloads/figure_{id}.xlsx` (one sheet per panel + README)

The script never touches legacy folders:
- `public/images/previous`
- `public/spreadsheets/previous`

## Feature flag / Runtime switch

- Default remains legacy (images + old XLSX).
- To preview new pipeline data on interactive charts, append `?new=1` to URLs (e.g., `interactive-data.html?new=1`).
- You can also set `window.USE_NEW_DATA = true` in the browser console.
- On `index.html`, we show a small “New data preview” block below certain figures; those preview canvases render only when `?new=1` (or the flag) is enabled.

## Data layout

```
data/
  figures/
    figure_2/
      meta.yml
      panel_a.csv
    figure_3a/
      meta.yml
      panel_a.csv
    figure_3b/
      meta.yml
      panel_a.csv
    figure_6/
      meta.yml
      panel_c.csv
      panel_d.csv
    figure_7/
      meta.yml
      panel_c.csv
```

Each `meta.yml` defines panels, columns, and checks. Example (figure_2):

```yaml
figure_id: 2
panels:
  - id: panel_a
    file: panel_a.csv
    schema:
      columns:
        - {name: Survey, type: string}
        - {name: z_mean, type: number}
        - {name: N_gal, type: integer}
        - {name: Asymmetry_pred, type: number}
        - {name: Asymmetry_obs, type: number, optional: true}
    checks:
      - {type: range, column: Asymmetry_pred, min: -0.05, max: 0.05}
```

## CI

A GitHub Action builds JSON/XLSX on every push/PR and uploads the `public/data` and `public/downloads` directories as an artifact.

## Revert plan

- Remove `?new=1` (and/or set `window.USE_NEW_DATA=false`) to revert to legacy assets instantly.
- Old PNGs and XLSX remain available and unchanged.

## Hiding legacy figures

After you visually confirm the new previews, we can wrap the legacy figure blocks on `index.html` in a collapsible container (hidden by default). We will not delete legacy assets.



