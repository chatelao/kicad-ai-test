# Project goal
Use the IPC-API of a KiCAD 9.0 patched for Autostart in a xvfb-run (no file manipulations) to create a simple 555 schematics and board with a blinking LED.

# Details
Use Kibot in the GitHub action workflow to run th ERC and DRC after each push on every branch. Validate the workflow locally:
- `/specifications` : Download KiCAD IPC API definition and components datasheets, converted to .md if need.
- `/.github/workflows` : The GitHub CICD path.
- `KICAD_IPC_CALLS.md` : Log all IPC calls used to build the files.
- `DECICISON_LOG.md` : Add per decision step three variants and the seleted options.

# See
- https://dev-docs.kicad.org/en/apis-and-binding/ipc-api
- https://docs.kicad.org/kicad-python-main/kicad.html
