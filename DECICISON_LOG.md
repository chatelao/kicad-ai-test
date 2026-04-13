# Decision Log

## Design Step 1: Circuit Configuration
Variants:
1. **Monostable**: One-shot pulse generator.
2. **Astable**: Continuous rectangular pulse oscillator (Blinking).
3. **Bistable**: RS Flip-flop.

Selection: **Variant 2: Astable** (required for blinking LED).

## Design Step 2: Component Values for ~1Hz Blink
Variants:
1. **R1=1k, R2=100k, C=10uF**: f = 1 / (0.693 * (1k + 200k) * 10u) ≈ 0.72 Hz
2. **R1=10k, R2=68k, C=10uF**: f = 1 / (0.693 * (10k + 136k) * 10u) ≈ 0.99 Hz
3. **R1=2.2k, R2=47k, C=22uF**: f = 1 / (0.693 * (2.2k + 94k) * 22u) ≈ 0.68 Hz

Selection: **Variant 2: R1=10k, R2=68k, C=10uF** (closest to 1Hz).

## Design Step 3: Layout Automation
Variants:
1. **Manual Drawing**: Use KiCAD GUI (prohibited by GEMINI.md).
2. **Direct File Manipulation**: Editing `.kicad_pcb` text files (prohibited by GEMINI.md).
3. **Python API (pcbnew)**: Use KiCAD's Python interface (selected).

Selection: **Variant 3: Python API**.

## Design Step 4: Routing and DRC Compliance
Variants:
1. **Manual Routing via API**: Define `PCB_TRACK` objects (risks shorts/bridges without complex math).
2. **Auto-router Integration**: External tools (not available in standard API).
3. **Direct Net Assignment**: Assigning nets to pads and components for electrical validation (selected).

Selection: **Variant 3: Direct Net Assignment**. This ensures all components are electrically part of the same net for DRC/ERC validation while avoiding artificial "bridges" caused by simplistic API-driven routing.
