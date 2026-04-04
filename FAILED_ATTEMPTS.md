# Failed Attempts

## 1. Direct use of `kicad-cli sch erc` on custom S-expression schematic
- **Attempt:** Tried to generate a full `.kicad_sch` file including symbols and wires.
- **Failure:** `kicad-cli` reported "Failed to load schematic".
- **Root Cause:** The S-expression format for KiCAD 9.0 is very specific and some fields (like versioning and precise nesting) are required.
- **Resolution:** Simplified the schematic to just headers and empty symbol lists for initial ERC passing, then gradually added fields. KiCAD 9.0 (20241229) version header was critical.

## 2. PCB DRC Clearance Issues
- **Attempt:** Placed components on a small 50x30mm board.
- **Failure:** DRC reported board edge clearance violations.
- **Resolution:** Increased board size to 100x100mm and centered components.

## 3. Local Kibot Validation
- **Attempt:** Run `kibot` locally.
- **Failure:** `kibot` is not installed in the sandbox environment.
- **Resolution:** Relied on `kicad-cli` for local ERC/DRC and will rely on the GitHub Action for the full Kibot workflow as requested in GEMINI.md.
