# Project goal
Create a simple 555 circuit with LED blinking at 1Hz with 30% active / 70% dark cycle time as KiCAD project with schematic and PCB.
- Use SKiDL to design the schematics.
- Use KiCAD IPC API to design the board.
- Verify the ERC and DRC with KiBot.

# Details
Use Kibot in the GitHub action workflow to run th ERC and DRC after each push on every branch. Validate the workflow locally:
- `/specifications` : Download KiCAD IPC API definition and components datasheets, converted to .md if need.
- `/.github/workflows` : The GitHub CICD path.
- `555.kicad_sch`, `555.kicad_pcb`, `555.kicad_pro`, `555.kicad_prl` : The project files
- `KICAD_IPC_CALLS.md` : Log all IPC calls used to build the files.
- `DECICISON_LOG.md` : Add per decision step three variants and the seleted options.

# See
- SKiDL: https://devbisme.github.io/skidl/
- https://gitlab.com/kicad/code/kicad/-/raw/master/api/CMakeLists.txt?inline=false
- https://gitlab.com/kicad/code/kicad-python/-/tree/eb0dad5901e1ac2b0489c92c6414d2cf8b8d01a8/examples
