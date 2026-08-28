"""Install configured dependencies and run a Python script.

The runner reads package requirements from ``dependencies.yaml`` using the
target script's filename as the lookup key. Missing PyYAML support is installed
automatically, and registered packages are installed before the target script
is launched with the current Python interpreter. Additional command-line
arguments are forwarded to the target script unchanged.

Usage:
    python run.py <script_name.py> [args for script...]

Date: 2026-08-27
Author: kimpro82
"""

import sys
import subprocess
import os
from pathlib import Path

def ensure_yaml_parser():
    """Install and import PyYAML when it is not available."""
    try:
        import yaml
    except ImportError:
        print("[+] PyYAML not found in environment. Installing PyYAML automatically...")
        subprocess.run([sys.executable, "-m", "pip", "install", "PyYAML"], check=True)
        import yaml
    return yaml

def load_dependencies(script_name: str, config_path: str = "dependencies.yaml") -> list:
    """Return packages configured for the specified script."""
    if not os.path.exists(config_path):
        return []

    yaml = ensure_yaml_parser()
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    # Look up the target script key while accounting for path normalization.
    script_key = Path(script_name).name

    # Try the filename first, then try the full script path.
    packages = config.get(script_key) or config.get(script_name, [])
    return packages

def main():
    """Install dependencies and run the target script with its arguments."""
    if len(sys.argv) < 2:
        print("Usage: python run.py <script_name.py> [args for script...]")
        sys.exit(1)

    target_script = sys.argv[1]
    script_args = sys.argv[2:]  # Additional arguments to pass to the script.

    if not os.path.exists(target_script):
        print(f"[-] Error: Target script '{target_script}' not found.")
        sys.exit(1)

    print(f"[*] Checking dependencies for '{target_script}'...")
    packages = load_dependencies(target_script)

    if packages:
        print(f"[+] Found required packages: {packages}")
        # Install the configured packages with pip.
        subprocess.run([sys.executable, "-m", "pip", "install"] + packages, check=True)
    else:
        print("[-] No specific dependencies registered in YAML. Proceeding...")

    print(f"--- Running '{target_script}' ---\n")
    # Run the target script with the current interpreter and forwarded arguments.
    result = subprocess.run([sys.executable, target_script] + script_args, check=False)

    # Return the target script's exit code unchanged.
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
