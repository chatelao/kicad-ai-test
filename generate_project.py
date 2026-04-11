import os
import sys
import time

# Use environment variables or relative paths if possible
KIPY_PATH = os.environ.get("PYTHONPATH", "/home/jules/.pyenv/versions/3.12.13/lib/python3.12/site-packages")
if KIPY_PATH not in sys.path:
    sys.path.append(KIPY_PATH)
if "/usr/lib/python3/dist-packages" not in sys.path:
    sys.path.append("/usr/lib/python3/dist-packages")

from kipy import KiCad
from kipy.board_types import (
    FootprintInstance, LibraryIdentifier, Vector2, BoardLayer, Track, Net
)
import pcbnew

def log_ipc(call_name, params=None):
    with open("KICAD_IPC_CALLS.md", "a") as f:
        f.write(f"- {call_name}({params if params else ''})\n")

def generate_project():
    print("Connecting to KiCad IPC...")
    kicad = KiCad()
    log_ipc("KiCad")

    # Retry connection as the server might be starting
    for _ in range(5):
        try:
            ver = kicad.get_version()
            print(f"Connected to KiCad {ver}")
            log_ipc("get_version", ver)
            break
        except Exception as e:
            print(f"Waiting for KiCad... ({e})")
            time.sleep(5)
    else:
        print("Failed to connect via IPC after retries.")
        with open("FAILD_ATTEMPTS.md", "a") as f:
            f.write("- IPC connection failed after retries.\n")

    # Board generation using pcbnew API
    print("Generating board using pcbnew API...")
    pcb = pcbnew.BOARD()

    # Set board outline
    outline = pcbnew.PCB_SHAPE(pcb)
    outline.SetShape(pcbnew.SHAPE_T_RECT)
    outline.SetFilled(False)
    outline.SetLayer(pcbnew.Edge_Cuts)
    outline.SetStart(pcbnew.VECTOR2I_MM(50, 50))
    outline.SetEnd(pcbnew.VECTOR2I_MM(150, 150))
    pcb.Add(outline)

    def pcbnew_add_footprint(library, footprint, reference, value, pos_mm):
        try:
            # Fix for KiCad 10.0 pcbnew API change or environment issue
            # FootprintLoad might not be directly available on the module
            plugin = pcbnew.PCB_IO_MGR.FindPlugin(pcbnew.PCB_IO_MGR.KICAD_SEXP)
            lib_path = os.path.join(os.environ.get('KICAD10_FOOTPRINT_DIR', '/usr/share/kicad/footprints'), library + ".pretty")
            fp = plugin.FootprintLoad(lib_path, footprint)

            if fp is None:
                raise ValueError(f"Could not load footprint {footprint} from {lib_path}")
            fp.SetReference(reference)
            fp.SetValue(value)
            fp.SetPosition(pcbnew.VECTOR2I_MM(pos_mm[0], pos_mm[1]))
            pcb.Add(fp)
            return fp
        except Exception as e:
            print(f"Error adding footprint {reference}: {e}")
            with open("FAILD_ATTEMPTS.md", "a") as f:
                f.write(f"- Failed to load footprint {footprint} from {library}: {e}\n")
            return None

    # Components for 555 Timer Blinking LED
    u1 = pcbnew_add_footprint("Package_DIP", "DIP-8_W7.62mm", "U1", "NE555P", (100, 100))
    r1 = pcbnew_add_footprint("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal", "R1", "1k", (120, 80))
    r2 = pcbnew_add_footprint("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal", "R2", "470k", (120, 90))
    c1 = pcbnew_add_footprint("Capacitor_THT", "C_Disc_D5.0mm_W2.5mm_P2.50mm", "C1", "1uF", (120, 100))
    led1 = pcbnew_add_footprint("LED_THT", "LED_D5.0mm", "D1", "LED", (140, 100))
    r_led = pcbnew_add_footprint("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal", "R_LED", "220", (140, 90))

    print("Saving board...")
    pcbnew.SaveBoard("project.kicad_pcb", pcb)

    # Schematic creation fallback
    print("Attempting schematic creation...")
    # Using a minimal valid schematic content instead of 'create' which doesn't exist
    with open("project.kicad_sch", "w") as f:
        f.write('(kicad_sch (version 20240108) (generator eeschema)\n'
                '  (paper "A4")\n'
                '  (title_block\n'
                '    (title "555 Timer Blinker")\n'
                '  )\n'
                '  (symbol (lib_id "Timer:NE555P") (at 100 100 0) (unit 1)\n'
                '    (in_bom yes) (on_board yes) (dnp no)\n'
                '    (fields\n'
                '      (field (name "Reference") "U1" (at 100 90 0))\n'
                '      (field (name "Value") "NE555P" (at 100 110 0))\n'
                '    )\n'
                '  )\n'
                ')\n')
    # For a real 555 schematic, we would need to add symbols programmatically.
    # Since the CLI is limited to creating empty ones, we will note this.
    with open("FAILD_ATTEMPTS.md", "a") as f:
        f.write("- Programmatic symbol placement in schematic not yet supported via CLI/IPC in this environment.\n")

    print("Project generation process complete.")

if __name__ == "__main__":
    generate_project()
