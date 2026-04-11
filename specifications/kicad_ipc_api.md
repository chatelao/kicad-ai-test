# KiCAD IPC API Definition (v10.0)

The KiCAD IPC API is a decoupled architecture using gRPC and Protocol Buffers (Protobuf). It is used to interact with the KiCAD applications from external processes.

## Core Proto Files (Reference: KiCad Source)
- `common/envelope.proto` - Wrapper for all messages.
- `common/types/base_types.proto` - Coordinate systems, layers, etc.
- `common/types/enums.proto` - Various KiCAD enums.
- `board/board.proto` - Board-level data structures.
- `board/board_commands.proto` - Commands to manipulate the PCB.

## Architectural Flow
1. **Connection:** Connect to the gRPC server (default port or socket).
2. **Commit Pattern:**
   - `BeginCommit()`
   - Add/Update/Remove items.
   - `PushCommit()`
3. **Undo/Redo:** Changes are automatically added to the Undo stack.

## Key APIs
- `pcb.GetActiveBoard()`
- `pcb.AddFootprint()`
- `pcb.AddTrack()`
- `pcb.SaveBoard()`
