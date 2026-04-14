# KiCad IPC Calls Log

This file logs all IPC/API calls used to programmatically generate the KiCad project files.

| Call Type | Method/Command | Parameters | Status |
|-----------|----------------|------------|--------|
| Python API (pcbnew) | NewBoard | "555_timer.kicad_pcb" | Success |
| Python API (pcbnew) | PCB_SHAPE | board, SHAPE_T_SEGMENT | Success |
| Python API (pcbnew) | SaveBoard | "555_timer.kicad_pcb", board | Success |
| Python (text) | write | "555_timer.kicad_sch" | Success |
