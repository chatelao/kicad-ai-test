# KiCad IPC API Technical Summary

## Overview
The KiCad IPC (Inter-Process Communication) API allows external applications to communicate with the KiCad PCB editor. It uses gRPC and Protocol Buffers for communication.

## Core Concepts
- **Connection**: Established via a socket (default: `ipc:///tmp/kicad/api.sock`).
- **Commit Protocol**: Changes are batched and pushed to the editor's event queue.
- **Coordinates**: Internal units are nanometers (1 mm = 1,000,000 nm).
- **Undo/Redo**: Supported by grouping operations into a single "push".

## Python Library: `kipy`
- **Installation**: `pip install kipy-python`
- **Main Entry Point**: `kipy.KiCad()`
- **PCB Access**: `kicad.board.active_board()`

## Example Usage
```python
import kipy
from kipy.board import Board

kicad = kipy.KiCad()
board = kicad.board.active_board()

# Create a new track
with board.commit() as commit:
    track = board.add_track(
        start=(0, 0),
        end=(1000000, 1000000), # 1mm, 1mm
        width=250000,           # 0.25mm
        layer="F.Cu"
    )
    commit.add(track)
```

## Supported Operations
- Retrieval of board items (footprints, pads, tracks, vias).
- Modification of item properties (position, rotation, etc.).
- Addition and deletion of items.
- Drawing graphics (lines, circles, etc.) on any layer.
- Managing nets and netclasses.
