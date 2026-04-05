import pcbnew
import sys
import os

sys.path.append('/usr/lib/python3/dist-packages')

def create_555_pcb():
    board = pcbnew.NewBoard("555_timer.kicad_pcb")

    # Add NE555 (SOIC-8)
    # Note: In a real script we would load from a library,
    # but here we'll simulate the creation or placement if possible.
    # KiCad 9.0 pcbnew API has FootprintLoad

    # Save the empty board for now as a placeholder
    pcbnew.SaveBoard("555_timer.kicad_pcb", board)
    print("Created 555_timer.kicad_pcb")

if __name__ == "__main__":
    create_555_pcb()
