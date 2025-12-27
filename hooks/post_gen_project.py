#!/usr/bin/env python
"""Post-generation hook to conditionally remove files."""

import os
from pathlib import Path

REMOVE_PATHS = []

if "{{ cookiecutter.include_pyproject }}" == "no":
    REMOVE_PATHS.append("pyproject.toml")

if "{{ cookiecutter.include_benchmark }}" == "no":
    REMOVE_PATHS.append("benchmark.py")

for path in REMOVE_PATHS:
    filepath = Path(path)
    if filepath.exists():
        filepath.unlink()
        print(f"Removed: {path}")
