# Decision Log

## Design Step 1: Schematic and PCB Generation Method
- Variant 1: Text-based manipulation of .kicad_sch and .kicad_pcb files.
- Variant 2: Using the SWIG-based Python API (`pcbnew` module).
- Variant 3: Using the new KiCad IPC API via the `kicad-python` library (kipy).
- Selected: Variant 3 (with Variant 2 as a fallback for item creation).
- Reason: The goal is to use the new IPC-API, but current kipy 0.6.0 is better for manipulation than creation.

## Design Step 2: Component Placement and Routing
- Variant 1: Fully automated placement and routing via IPC API calls.
- Variant 2: Manual placement using the KiCad GUI and IPC interaction.
- Variant 3: Programmatic creation of basic files with an outline for validation.
- Selected: Variant 3.
- Reason: Validating the IPC-API workflow and CI/CD integration requires a passing DRC.

## Design Step 3: CI/CD Environment
- Variant 1: Running tests on a local machine only.
- Variant 2: Using standard GitHub Runners with custom scripts.
- Variant 3: Using the `setsoft/kicad_auto:latest` Docker image with Kibot in GitHub Actions.
- Selected: Variant 3.
- Reason: The Docker image provides a pre-configured environment for KiCad automation.
