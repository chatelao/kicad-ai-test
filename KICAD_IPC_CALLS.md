# KiCad IPC Calls Log

Note: Due to `kipy` / IPC server unavailability in this environment, `pcbnew` Python API was used as a fallback for board generation.

| Call | Arguments | Description |
| --- | --- | --- |
| `pcbnew.BOARD()` | None | Initialize new board object |
| `pcbnew.FootprintLoad(path, name)` | lib_path, fp_name | Load footprint from library |
| `board.Add(fp)` | Footprint | Add footprint to board |
| `fp.SetPosition(vector)` | VECTOR2I | Position footprint |
| `pcbnew.PCB_SHAPE(board)` | Board | Create new shape (segment) |
| `shape.SetShape(SHAPE_T_SEGMENT)` | Enum | Set shape type to segment |
| `pcbnew.SaveBoard(filename, board)` | path, board | Save board to file |
