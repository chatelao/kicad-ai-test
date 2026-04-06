import os
import time
import sys
from kipy.board import Board
from kipy.kicad import KiCad
import pcbnew

# Define IPC log function
def log_ipc(call):
    with open("KICAD_IPC_CALLS.md", "a") as f:
        f.write(f"- {call}\n")

def generate_design():
    board_file = "555_blinker.kicad_pcb"
    sch_file = "555_blinker.kicad_sch"

    # 1. Create the files using pcbnew
    board = pcbnew.CreateEmptyBoard()

    # Add Board Outline (50x50mm)
    corners = [
        pcbnew.VECTOR2I_MM(0, 0),
        pcbnew.VECTOR2I_MM(50, 0),
        pcbnew.VECTOR2I_MM(50, 50),
        pcbnew.VECTOR2I_MM(0, 50),
        pcbnew.VECTOR2I_MM(0, 0)
    ]
    for i in range(len(corners) - 1):
        s = pcbnew.PCB_SHAPE(board)
        s.SetShape(pcbnew.SHAPE_T_SEGMENT)
        s.SetLayer(pcbnew.Edge_Cuts)
        s.SetStart(corners[i])
        s.SetEnd(corners[i+1])
        s.SetWidth(int(0.15 * 1000000))
        board.Add(s)

    board.Save(board_file)
    print(f"PCB file created: {board_file}")

    with open(sch_file, "w") as f:
        f.write("(kicad_sch (version 20231120) (generator \"manual\")\n(uuid \"00000000-0000-0000-0000-000000000000\")\n(paper \"A4\")\n)\n")
    print(f"Schematic file created: {sch_file}")

    # 2. Connect via IPC to demonstrate its usage
    socket_path = os.environ.get("KICAD_API_SOCKET", "ipc:///tmp/kicad/api.sock")
    try:
        # We assume KiCad is already running with xvfb-run
        kicad = KiCad(socket_path)
        log_ipc(f"Connect to KiCad at {socket_path}")

        # Try a few times to ping
        for i in range(3):
            try:
                kicad.ping()
                log_ipc("kicad.ping()")
                print("IPC Ping successful")
                break
            except Exception as e:
                print(f"Retry {i+1}: {e}")
                time.sleep(2)

    except Exception as e:
        print(f"IPC Error: {e}")
        with open("FAILD_ATTEMPTS.md", "a") as f:
            f.write(f"- IPC call failed: {e}\n")

    print("Design files generated/initialized.")

if __name__ == "__main__":
    generate_design()
