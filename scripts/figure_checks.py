#!/usr/bin/env python3
"""
CI Figure Validation Checks
Ensures data integrity and proper analysis methods
"""

import sys
import json
import yaml
import pandas as pd
import numpy as np
import pathlib
import re

def require_cols(df, cols, name):
    """Check required columns exist."""
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise SystemExit(f"[FAIL] {name}: missing columns {missing}")

def check_spin_data():
    """Validate galaxy spin data format and values."""
    print("Checking galaxy spin data...")
    
    try:
        spins = pd.read_csv("data/galaxy_spin_bins.csv")
    except FileNotFoundError:
        print("[WARN] galaxy_spin_bins.csv not found - skipping spin checks")
        return
    
    # Required columns
    require_cols(spins, ["z_bin_center", "N_cw", "N_ccw", "survey_id", "b_weight"], 
                 "galaxy_spin_bins")
    
    # Value checks
    if (spins[["N_cw", "N_ccw"]] < 0).any().any():
        raise SystemExit("[FAIL] galaxy_spin_bins: negative counts detected")
    
    if not ((spins["b_weight"] >= 0) & (spins["b_weight"] <= 1)).all():
        raise SystemExit("[FAIL] galaxy_spin_bins: b_weight outside [0,1]")
    
    if (spins["z_bin_center"] < 0).any():
        raise SystemExit("[FAIL] galaxy_spin_bins: negative redshifts")
    
    # Check for reasonable values
    total_galaxies = (spins["N_cw"] + spins["N_ccw"]).sum()
    if total_galaxies < 100:
        print(f"[WARN] Very small sample: {total_galaxies} galaxies total")
    
    print("✓ Galaxy spin data passed")

def check_cmb_data():
    """Validate CMB forecast input data."""
    print("Checking CMB forecast data...")
    
    # Check theory spectrum
    try:
        cls = pd.read_csv("data/cls_EE_theory.csv")
        require_cols(cls, ["ell", "C_ell_EE"], "cls_EE_theory")
        
        if (cls["ell"] < 2).any():
            raise SystemExit("[FAIL] cls_EE_theory: ell < 2 not allowed")
        
        if (cls["C_ell_EE"] < 0).any():
            raise SystemExit("[FAIL] cls_EE_theory: negative power spectrum")
            
    except FileNotFoundError:
        print("[WARN] cls_EE_theory.csv not found - using default")
    
    # Check instrument specs
    try:
        inst = pd.read_csv("data/instrument_specs.csv")
        require_cols(inst, ["ell", "N_ell_EE"], "instrument_specs")
        
        if (inst["N_ell_EE"] < 0).any():
            raise SystemExit("[FAIL] instrument_specs: negative noise")
            
    except FileNotFoundError:
        print("[WARN] instrument_specs.csv not found - using default")
    
    print("✓ CMB data passed")

def check_config_consistency():
    """Check configuration files for consistency."""
    print("Checking configuration consistency...")
    
    # Load main config
    try:
        with open("config/params.yml", 'r') as f:
            cfg = yaml.safe_load(f)
    except FileNotFoundError:
        print("[WARN] params.yml not found - using defaults")
        return
    
    # Check rho correlation values
    if "rho_grid" in cfg:
        if not all(isinstance(r, (int, float)) and -1 <= r <= 1 
                  for r in cfg["rho_grid"]):
            raise SystemExit("[FAIL] params.yml: rho_grid contains invalid correlations")
        
        if not any(r in [0.0, 0.3, 0.5] for r in cfg["rho_grid"]):
            print("[WARN] params.yml: rho_grid missing standard values [0, 0.3, 0.5]")
    else:
        print("[WARN] params.yml: no rho_grid set")
    
    # Check c_omega convention
    if "conventions" in cfg:
        if cfg["conventions"].get("c_omega") != -1:
            raise SystemExit("[FAIL] params.yml: c_omega must be -1 for this framework")
    
    print("✓ Configuration passed")

def check_correlation_implementation():
    """Ensure joint analysis uses proper correlation."""
    print("Checking correlation implementation...")
    
    # Search for Python files with Z-combination
    bad_files = []
    
    for p in pathlib.Path("scripts").rglob("*.py"):
        if not p.is_file():
            continue
            
        content = p.read_text()
        
        # Look for quadrature-only combination without rho
        if re.search(r"sqrt\s*\(\s*Z1\s*\*\*\s*2\s*\+\s*Z2\s*\*\*\s*2\s*\)", content):
            if "rho" not in content and "correlation" not in content.lower():
                bad_files.append(str(p))
        
        # Look for simple addition of significances
        if re.search(r"significance.*=.*sig1.*\+.*sig2", content, re.IGNORECASE):
            if "weight" not in content.lower():
                bad_files.append(str(p))
    
    if bad_files:
        raise SystemExit(f"[FAIL] Found quadrature-only combiner without correlation in: {bad_files}")
    
    print("✓ Correlation implementation passed")

def check_output_reproducibility():
    """Check that outputs can be reproduced."""
    print("Checking output reproducibility...")
    
    # Check for random seeds
    seed_files = []
    for p in pathlib.Path("scripts").rglob("*.py"):
        if p.is_file() and "random" in p.read_text() and "seed" not in p.read_text():
            seed_files.append(str(p))
    
    if seed_files:
        print(f"[WARN] Files using random without seed: {seed_files}")
    
    # Check for version info
    if not pathlib.Path("requirements.txt").exists() and not pathlib.Path("environment.yml").exists():
        print("[WARN] No requirements.txt or environment.yml found")
    
    print("✓ Reproducibility checks passed")

def check_figure_data_sync():
    """Ensure figures match their source data."""
    print("Checking figure-data synchronization...")
    
    # Check that each figure has corresponding data
    figure_dir = pathlib.Path("public/images")
    data_dir = pathlib.Path("public/spreadsheets")
    
    if figure_dir.exists():
        figures = list(figure_dir.glob("figure*.png"))
        
        for fig in figures:
            # Extract figure number
            match = re.search(r"figure(\d+)", fig.stem)
            if match:
                fig_num = match.group(1)
                # Look for corresponding data file
                data_files = list(data_dir.glob(f"*figure*{fig_num}*"))
                if not data_files:
                    print(f"[WARN] No data file found for {fig.name}")
    
    print("✓ Figure-data sync passed")

def check_units_consistency():
    """Check for unit consistency across files."""
    print("Checking units consistency...")
    
    # Common unit issues to check
    issues = []
    
    # Check for mixed unit conventions
    for p in pathlib.Path("paper").rglob("*.md"):
        if not p.is_file():
            continue
            
        content = p.read_text()
        
        # Check for both GeV and eV in same file
        if "GeV" in content and " eV" in content and "MeV" not in content:
            issues.append(f"{p.name}: Mixed GeV/eV units")
        
        # Check for both Mpc and pc
        if "Mpc" in content and " pc" in content and "kpc" not in content:
            issues.append(f"{p.name}: Mixed Mpc/pc units")
    
    if issues:
        print(f"[WARN] Unit consistency issues: {issues}")
    
    print("✓ Units consistency passed")

def main():
    """Run all validation checks."""
    print("="*60)
    print("Figure and Data Validation Checks")
    print("="*60)
    
    checks = [
        check_spin_data,
        check_cmb_data,
        check_config_consistency,
        check_correlation_implementation,
        check_output_reproducibility,
        check_figure_data_sync,
        check_units_consistency
    ]
    
    failed = False
    
    for check in checks:
        try:
            check()
        except SystemExit as e:
            print(str(e))
            failed = True
        except Exception as e:
            print(f"[ERROR] {check.__name__}: {e}")
            failed = True
        print()
    
    if failed:
        print("="*60)
        print("[FAIL] Some checks failed - see above")
        sys.exit(1)
    else:
        print("="*60)
        print("[OK] All checks passed! ✓")
        sys.exit(0)

if __name__ == "__main__":
    main()