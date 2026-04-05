# Project goal
Use the KiCAD 9.0 with patched for IPC Autostart in a xvfb-run (no file manipulations) to create a simple 555 board from schematics with a blinking LED.

# Details
Use Kibot in the GitHub action workflow to run th ERC and DRC after each push on every branch. Validate the workflow locally:
- `/specifications` : Download KiCAD IPC API definition and components datasheets, converted to .md if need.
- `KICAD_IPC_CALLS.md` : Log all IPC calls used to build the files.
- `DECICISON_LOG.md` : Add per decision step three variants and the seleted options.
- `FAILD_ATTEMPTS.md` : Record failed attempts.
