# KiCad IPC API Definitions

The KiCad IPC API uses Protocol Buffers for message serialization and NNG for transport over UNIX sockets.

## Sockets
- Default: `/tmp/kicad/api.sock`
- Multiple instances: `/tmp/kicad/api-<PID>.sock`

## Protocol Buffers
The API surface is defined in several protobuf files:
- `base_types.proto`: Common data types (KIID, Vector2, Distance, etc.)
- `board_types.proto`: PCB-related types
- `schematic_types.proto`: Schematic-related types
- `*_commands.proto`: Command messages

## Units
All physical distances are 64-bit integer nanometer values.
Angles are in 1/10th of a degree (or radians depending on the context, but nanometers are for distances). Actually, the docs say physical distances are nanometers.

## Library
Official Python bindings: `kicad-python` (package `kipy`).
