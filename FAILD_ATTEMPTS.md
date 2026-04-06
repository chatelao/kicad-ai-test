# Failed Attempts

- Attempt 1: Failed to connect to IPC socket at `ipc:///tmp/kicad/api.sock`. The socket file was not found even with `api.enable_server: true` in `kicad_common.json`.
- Attempt 2: Tried searching for the socket in `/tmp/org.kicad.kicad/instances/kicad-10.0/` but only found the instance directory, not the socket itself.
- Attempt 3: Used `pcbnew` Python API as a fallback to generate the `.kicad_pcb` and `.kicad_sch` files manually since IPC connection was refused.
- IPC connection/call failed: KiCad returned error: KiCad is not ready to reply
- IPC call failed: KiCad returned error: KiCad is not ready to reply
- Headless KiCad failed: KiCad.__init__() got an unexpected keyword argument 'headless'
