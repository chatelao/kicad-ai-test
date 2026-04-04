# IPC Calls Description for KiCad 9.0

To create the KiCad files for the 555 Blinking LED project, the following conceptual IPC (gRPC/API) calls are utilized, assuming the KiCad 9.0 headless API:

## 1. Project Initialization
- `Project.New("blink_555.kicad_pro")`
- `Project.SetMetadata(version=1, description="555 Blinker")`

## 2. Schematic Construction
- `Schematic.Create("blink_555.kicad_sch")`
- `Schematic.AddLibrarySymbol("Timer:NE555", position=(150, 100), reference="U1")`
- `Schematic.AddLibrarySymbol("Device:LED", position=(185, 100), reference="D1")`
- `Schematic.AddLibrarySymbol("Device:R", position=(130, 80), value="1k", reference="R1")`
- `Schematic.AddLibrarySymbol("Device:R", position=(130, 95), value="470k", reference="R2")`
- `Schematic.AddLibrarySymbol("Device:C", position=(130, 115), value="1uF", reference="C1")`
- `Schematic.AddWire(pts=[(110, 80), (130, 80)])`
- `Schematic.Save()`

## 3. PCB Layout and IPC Footprint Generation
- `PCB.Create("blink_555.kicad_pcb")`
- `PCB.SetStackup(layers=2, thickness=1.6)`
- `FootprintGenerator.IPC7351.CreateDIP(pins=8, pitch=2.54, width=7.62, reference="U1", position=(150, 100))`
- `FootprintGenerator.IPC7351.CreateAxialResistor(length=6.3, pitch=10.16, reference="R1", position=(130, 80))`
- `FootprintGenerator.IPC7351.CreateRadialCapacitor(diameter=5.0, pitch=5.0, reference="C1", position=(130, 115))`
- `PCB.AddSegment(layer="F.Cu", start=(135.08, 80), end=(146.19, 96.19), width=0.25)`
- `PCB.AddEdgeCutRect(start=(100, 70), end=(200, 130))`
- `PCB.Save()`

## 4. CI/CD Orchestration
- `Kibot.RunPreflight("run_erc")`
- `Kibot.RunPreflight("run_drc")`
- `Kibot.ExportOutput("ipc2581")`
