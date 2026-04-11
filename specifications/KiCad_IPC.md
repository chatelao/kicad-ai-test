# KiCad IPC API

The KiCad IPC API allows programmatic interaction with KiCad over a socket (typically `ipc:///tmp/kicad/api.sock`).

## Key Concepts
- **Connection**: Established via a client library (e.g., `kipy`).
- **Commands**: Send JSON-RPC or similar messages to perform actions like adding footprints, routing, etc.
- **Automatic Server**: KiCad 10.0 starts the server automatically if configured in `kicad_common.json`.

## Common Actions
- `board.add_footprint(name, lib)`
- `board.add_track(start, end, layer, width)`
- `project.load(path)`
