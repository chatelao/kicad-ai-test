# Failed Attempts

## SKiDL Schematic Generation (kicad6+)
- **Problem**: SKiDL `generate_schematic()` is not implemented for KiCad versions 6, 7, 8, or 9.
- **Symptom**: `WARNING: Schematic generation is not implemented for KiCad version X.`
- **Attempted**: Setting `set_default_tool()` to KICAD6, KICAD7, KICAD8, KICAD9.

## SKiDL Schematic Generation (kicad5)
- **Problem**: KiCad 5 uses `.lib` files while the environment only has `.kicad_sym` files.
- **Symptom**: `FileNotFoundError: Can't open file: Timer.` and other library errors.

## SKiDL Schematic Generation (Current)
- **Problem**: SKiDL `generate_schematic()` is not implemented for KiCad versions 6 through 9.
- **Result**: Netlist `555.net` successfully generated, but `555.kicad_sch` was not produced.
- **Workaround**: Proceed with PCB generation from netlist.
