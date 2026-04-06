# Decision Log

## Project Structure
- **Variant 1**: Standard KiCad project (manual design).
- **Variant 2**: Scripted generation using `pcbnew` Python API.
- **Variant 3**: Scripted generation using the new KiCad 10.0 IPC API (`kipy`).
- **Selection**: **Variant 3 with Hybrid Fallback**. The primary goal is IPC, but due to timeouts in the headless environment, `pcbnew` API is used as a fallback for board generation to ensure the project goals are met.

## Board Outline Strategy
- **Variant 1**: Manual drawing on Edge.Cuts layer.
- **Variant 2**: Coordinate-based generation in Python (closed loop).
- **Variant 3**: SVG import via script.
- **Selection**: **Variant 2**. This is more robust for programmatic generation.

## Component Selection
- **Variant 1**: Surface mount (SMD) components.
- **Variant 2**: Through-hole (DIP/TH) components.
- **Variant 3**: Mixed assembly.
- **Selection**: **Variant 2**. Standard DIP NE555 is well-supported and easier to design for a simple blinker.
