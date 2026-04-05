import pcbnew
import sys
import os

# Set PYTHONPATH to include KiCad's python packages
sys.path.append('/usr/lib/python3/dist-packages')

try:
    board = pcbnew.NewBoard("555_timer.kicad_pcb")
    pcbnew.SaveBoard("555_timer.kicad_pcb", board)
    print("Successfully created a new board via pcbnew API")
except Exception as e:
    print(f"Error: {e}")
