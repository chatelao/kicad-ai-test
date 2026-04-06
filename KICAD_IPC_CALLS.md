# KiCad IPC Calls
pcbnew.BOARD()
pcbnew.FootprintLoad('/usr/share/kicad/footprints/Package_SO.pretty', 'SOIC-8_3.9x4.9mm_P1.27mm')
board.Add(module)
board.Save('board.kicad_pcb')
