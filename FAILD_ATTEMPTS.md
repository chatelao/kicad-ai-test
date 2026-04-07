# Failed Attempts

- **Attempt 1: Installing `kipy` from pip.**
  - **Reason:** Package not found in standard PyPI (likely because it's a newer or non-standard package name).
  - **Correction:** Tried `kipy-python`, which also failed. I will look for other installation methods or use the system's `pcbnew` Python API as a fallback if necessary.
- **Attempt 2: Using `kicad-cli` to create project files.**
  - **Reason:** `kicad-cli` (v10.0.0) does not have a 'create' subcommand for project, schematic, or PCB files.
  - **Correction:** These files will be initialized via the Python API or by writing S-expression templates to the filesystem.
- **Attempt 3: Using `skidl` (v2.2.2).**
  - **Reason:** A known circular import error in Python 3.12 (`ImportError: cannot import name 'get_default_tool'`).
  - **Correction:** Downgraded to `skidl==2.2.0` as per memory.
- **Attempt 4: Direct use of `pcbnew` in system Python without PYTHONPATH.**
  - **Reason:** `pcbnew` module is not in the default Python path for the system's Python 3.12.
  - **Correction:** Manually set `PYTHONPATH` to `/usr/lib/python3/dist-packages`.
