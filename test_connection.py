import kipy
import sys

try:
    kicad = kipy.KiCad()
    print(f"Connected to KiCad version: {kicad.get_version()}")
except Exception as e:
    print(f"Failed to connect: {e}")
    sys.exit(1)
