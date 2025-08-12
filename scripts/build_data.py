import json, yaml, os, subprocess
from pathlib import Path
from datetime import datetime
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "data/figures"
OUT_JSON = ROOT / "public/data"
OUT_XLSX = ROOT / "public/downloads"


def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT).decode().strip()
    except Exception:
        return "unknown"


def validate(df: pd.DataFrame, panel: dict):
    # Required columns
    required = [c["name"] for c in panel["schema"]["columns"] if not c.get("optional")]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Type checks (best-effort)
    for col in panel["schema"]["columns"]:
        name = col["name"]
        typ = col.get("type")
        if name in df.columns and typ in {"number", "integer"}:
            try:
                df[name] = pd.to_numeric(df[name])
                if typ == "integer":
                    df[name] = df[name].astype("Int64")
            except Exception as e:
                raise ValueError(f"Column {name} not numeric: {e}")

    # Range / formula checks
    for chk in panel.get("checks", []):
        if chk["type"] == "range":
            col = chk["column"]
            if col in df.columns:
                if (df[col] < chk["min"]).any() or (df[col] > chk["max"]).any():
                    raise ValueError(f"Out-of-range values in {col}")
        if chk["type"] == "formula_combined_sigma":
            cmb, gal, comb = chk["cmb"], chk["gal"], chk["combined"]
            if all(c in df.columns for c in [cmb, gal, comb]):
                calc = (df[cmb] ** 2 + df[gal] ** 2) ** 0.5
                if (abs(calc - df[comb]) > 1e-6).any():
                    raise ValueError("Combined_Significance_sigma != sqrt(cmb^2+gal^2)")


def to_chart_json(df: pd.DataFrame):
    return json.loads(df.to_json(orient="records"))


def build_figure(fig_path: Path):
    meta = yaml.safe_load((fig_path / "meta.yml").read_text())
    fig_id = str(meta["figure_id"]).replace(" ", "")

    json_dir = OUT_JSON / f"figure_{fig_id}"
    json_dir.mkdir(parents=True, exist_ok=True)

    OUT_XLSX.mkdir(parents=True, exist_ok=True)
    xlsx_path = OUT_XLSX / f"figure_{fig_id}.xlsx"

    with pd.ExcelWriter(xlsx_path, engine="xlsxwriter") as writer:
        for p in meta["panels"]:
            df = pd.read_csv(fig_path / p["file"])  # trust CSV as UTF-8
            validate(df, p)

            payload = {
                "updated": datetime.utcnow().isoformat() + "Z",
                "commit": git_commit(),
                "data": to_chart_json(df),
            }
            json_text = json.dumps(payload)
            (json_dir / f"{p['id']}.json").write_text(json_text, encoding="utf-8")
            # JSONP-style JS for file:// preview fallback
            key = f"figure_{fig_id}_{p['id']}"
            js = (
                "window.__FIG_DATA__=window.__FIG_DATA__||{};" 
                f"window.__FIG_DATA__['{key}']={json_text};"
            )
            (json_dir / f"{p['id']}.js").write_text(js, encoding="utf-8")

            sheet = p["id"][:31]
            df.to_excel(writer, sheet_name=sheet, index=False)

        prov = pd.DataFrame([
            (meta.get("provenance", {}))
            | {"commit": git_commit(), "built_at_utc": datetime.utcnow().isoformat() + "Z"}
        ])
        prov.to_excel(writer, sheet_name="README", index=False)


def main():
    if not FIG_DIR.exists():
        print("No data/figures directory; nothing to build.")
        return
    for fig in sorted(FIG_DIR.iterdir()):
        if (fig / "meta.yml").exists():
            print(f"Building {fig}")
            build_figure(fig)


if __name__ == "__main__":
    main()


