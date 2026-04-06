# Project goal
Use the new IPC-API of a KiCAD 10.0 patched for Autostart in a xvfb-run (no file manipulations) to create a simple 555 schematics and board with a blinking LED.

# Details
Use Kibot in the GitHub action workflow to run th ERC and DRC after each push on every branch. Validate the workflow locally:
- `/specifications` : Download KiCAD IPC API definition and components datasheets, converted to .md if need.
- `/.github/workflows` : The GitHub CICD path.
- `KICAD_IPC_CALLS.md` : Log all IPC calls used to build the files.
- `DECICISON_LOG.md` : Add per decision step three variants and the seleted options.

# See
- https://gitlab.com/kicad/code/kicad/-/raw/master/api/CMakeLists.txt?inline=false
- https://gitlab.com/kicad/code/kicad-python/-/tree/eb0dad5901e1ac2b0489c92c6414d2cf8b8d01a8/examples
