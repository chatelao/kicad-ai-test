# KiCad IPC and API Calls Log

## Automated PCB Generation (pcbnew API fallback)
- `pcbnew.BOARD()`: Initialized a new board object.
- `pcbnew.FootprintLoad(fp_path, fp_name)`: Loaded footprints for NE555, Resistors, Capacitors, and LED.
- `board.Add(footprint)`: Added components to the board.
- `footprint.SetPosition(pcbnew.VECTOR2I(x, y))`: Placed components at specific coordinates.
- `pcbnew.PCB_TRACK(board)`: Created a track object.
- `track.SetStart(pcbnew.VECTOR2I(x, y))`: Defined track start point.
- `track.SetEnd(pcbnew.VECTOR2I(x, y))`: Defined track end point.
- `pcbnew.SaveBoard('555.kicad_pcb', board)`: Saved the board to a file.

## IPC API (Intent and Simulated/Attempted)
- `kipy.KiCad()`: Connect to the KiCad IPC server.
- `kicad.board.active_board()`: Get reference to the active board.
- `board.commit()`: Start a batch of operations.
- `commit.add(item)`: Add items to the commit batch.
- `commit.push()`: Push the changes to KiCad.

*Note: Due to headless environment constraints and IPC server timeout issues, the pcbnew Python API was used as a reliable fallback to ensure the project files were generated correctly.*
