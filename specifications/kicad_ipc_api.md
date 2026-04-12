# KiCad IPC API Definition

The KiCad IPC API is an interface that can be used to remotely control a running instance of KiCad.
The API is implemented using Protocol Buffers and NNG.

Detailed info: https://dev-docs.kicad.org/en/apis-and-binding/ipc-api

## Core Concepts
- Uses NNG to transport messages.
- Protobuf definitions for API calls.
- `api.sock` socket path.
- `KICAD_API_TOKEN` for session identification.

## Python Bindings
- Official library: `kicad-python` (pypi).
- Documentation: https://docs.kicad.org/kicad-python-main/
