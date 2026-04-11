# KiCAD IPC API Proto Summary

## common/envelope.proto
- Defines the main envelope for all IPC messages, including status codes and error messages.

## board/board_commands.proto
- **GetVersion**: Returns KiCad version.
- **GetBoard**: Retrieves the current board state.
- **SaveBoard**: Saves the board to a file.
- **CreateItems**: Creates new board items (footprints, tracks, etc.).
- **RemoveItems**: Deletes items from the board.

## schematic/schematic_commands.proto
- **GetSchematic**: Retrieves the current schematic state.
- **AddSymbol**: (Hypothetical) Adds a symbol to the schematic.
