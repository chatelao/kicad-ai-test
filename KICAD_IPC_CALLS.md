# KiCAD IPC Calls Log

## 2024-04-04: Initial Board Setup
- `pcbnew.NewBoard("timer.kicad_pcb")`: Create a new PCB file.
- `pcbnew.PCB_SHAPE(board)`: Create a board outline shape.
- `edge.SetShape(1)` (SHAPE_T_RECT): Set the outline to rectangular.
- `edge.SetStart(pcbnew.VECTOR2I(0, 0))`: Set the top-left corner of the outline.
- `edge.SetEnd(pcbnew.VECTOR2I(100000000, 100000000))`: Set the bottom-right corner of the outline (100mm x 100mm).
- `edge.SetLayer(pcbnew.Edge_Cuts)`: Assign the shape to the Edge_Cuts layer.
- `board.Add(edge)`: Add the outline to the board.
- `pcbnew.SaveBoard("timer.kicad_pcb", board)`: Save the PCB file.
- `write("timer.kicad_sch", ...)`: Programmatically generate the schematic S-expression file.

## 2024-04-04: Refined Circuit and PCB
- `pcbnew.NETINFO_ITEM(board, name)`: Create net definitions for GND, VCC, TRIGGER, OUT, DISCH, and LED_A.
- `board.Add(net_info)`: Register nets with the board.
- `pcbnew.FootprintLoad(path, name)`: Load component footprints from standard KiCAD libraries.
- `fp.SetReference(ref)`: Set designator (U1, R1, R2, R3, C1, D1).
- `fp.SetPosition(pcbnew.VECTOR2I(x, y))`: Position components on the board.
- `pad.SetNet(board.FindNet(net_name))`: Assign pads to nets for DRC connectivity.
- `pcbnew.PCB_TRACK(board)`: Create conductive traces between components.
- `track.SetStart(...)`, `track.SetEnd(...)`: Define trace path between component pads.
- `track.SetWidth(...)`: Set trace width to 0.25mm.
- `track.SetNet(...)`: Assign track to a net.
- `board.Add(track)`: Add the track to the layout.
