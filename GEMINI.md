# Project goal
Use the KiCAD 9.0 IPC only (no file manipulations) to create a simple 555 board with a blinking LED.

# Details
Use Kibot in the GitHub action workflow to run th ERC and DRC, validate the workflow locally:
- `/specifications` : Downloaded datasheets converted to .md if need.
- `KICAD_IPC_CALLS.md` : Log all IPC calls used to build the files.
- `DECICISON_LOG.md` : Add per decision step three variants and the seleted options.
- `FAILD_ATTEMPTS.md` : Record failed attempts.
