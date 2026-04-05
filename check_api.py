from kipy.kicad import KiCad
import sys

try:
    kicad = KiCad()
    version = kicad.get_version()
    print(f"Connected to KiCad: {version.major}.{version.minor}.{version.patch}")
    board = kicad.get_board()
    print(f"Current board: {board.name if board else 'None'}")
except Exception as e:
    print(f"Error: {e}")
