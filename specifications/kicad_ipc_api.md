# KiCad IPC API Specification

## Overview
As of KiCad 9/10, the new Inter-Process Communication (IPC) architecture uses gRPC and Protocol Buffers.
The official library is `kipy-python`, imported as `kipy`.

## API Connection
```python
import kipy
api = kipy.connect()
board = api.get_active_board()
```

## Commit Model
1. `commit = board.begin_commit()`
2. Modify board (e.g., `commit.add(footprint)`)
3. `commit.push()`

## Units
Internal units are nanometers (nm).
1 mm = 1,000,000 nm.

## References
- https://gitlab.com/kicad/code/kicad/-/raw/master/api/CMakeLists.txt
- https://gitlab.com/kicad/code/kicad-python/-/tree/master/examples
