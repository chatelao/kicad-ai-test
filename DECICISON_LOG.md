# Decision Log

## Schematic Design Tool
- **Variant 1**: Manual KiCad GUI design (not suitable for automation).
- **Variant 2**: Python `pcbnew` API (mostly for PCB, not schematic).
- **Variant 3**: SKiDL (Python-based schematic design).
- **Selection**: Variant 3 (SKiDL) as it allows programmatic schematic generation as requested.

## 555 Timer Circuit Configuration
- **Variant 1**: Standard astable (Duty cycle > 50%).
- **Variant 2**: Monostable (Requires trigger).
- **Variant 3**: Astable with steering diode (Allows < 50% duty cycle).
- **Selection**: Variant 3 to achieve the requested 30% active / 70% dark cycle.

## IPC API Interaction
- **Variant 1**: `kipy` library.
- **Variant 2**: Direct socket communication.
- **Variant 3**: Native KiCad Python API (`pcbnew`).
- **Selection**: Variant 3 (pcbnew) as fallback if IPC server is unstable, but will attempt IPC first as requested.
