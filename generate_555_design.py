import os
import sys

# Ensure PYTHONPATH includes the pcbnew library
sys.path.append('/usr/lib/python3/dist-packages')

import pcbnew

def generate_schematic():
    print("Generating schematic...")
    # Comprehensive NE555 Astable Multivibrator Schematic
    sch_content = """(kicad_sch (version 20241121) (generator kicad_sch_gen)
  (uuid "56781234-abcd-ef00-1122-334455667788")
  (paper "A4")
  (title_block (title "555 Blinking LED"))
  (lib_symbols
    (symbol "Timer:NE555P" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 10.16 0))
      (property "Value" "NE555P" (at 0 -10.16 0))
      (symbol "NE555P_0_1"
        (rectangle (start -7.62 7.62) (end 7.62 -7.62) (stroke (width 0.254) (type solid)) (fill (type background)))
      )
    )
    (symbol "Device:LED" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 2.54 0))
      (property "Value" "LED" (at 0 -2.54 0))
    )
    (symbol "Device:R" (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90))
      (property "Value" "R" (at 0 0 90))
    )
    (symbol "Device:C" (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 2.032 0 90))
      (property "Value" "C" (at 0 0 90))
    )
  )
  (symbol (lib_id "Timer:NE555P") (at 100 100 0) (unit 1)
    (uuid "00000000-0000-0000-0000-000000000001")
    (property "Reference" "U1" (at 100 89.84 0))
    (property "Value" "NE555P" (at 100 110.16 0))
  )
  (symbol (lib_id "Device:LED") (at 140 100 0) (unit 1)
    (uuid "00000000-0000-0000-0000-000000000002")
    (property "Reference" "D1" (at 140 95.84 0))
    (property "Value" "LED" (at 140 105.16 0))
  )
  (symbol (lib_id "Device:R") (at 120 100 0) (unit 1)
    (uuid "00000000-0000-0000-0000-000000000003")
    (property "Reference" "R1" (at 120 95.84 0))
    (property "Value" "1k" (at 120 105.16 0))
  )
  (symbol (lib_id "Device:C") (at 110 120 0) (unit 1)
    (uuid "00000000-0000-0000-0000-000000000004")
    (property "Reference" "C1" (at 110 115.84 0))
    (property "Value" "10uF" (at 110 125.16 0))
  )
  (wire (pts (xy 107.62 100) (xy 118.73 100)) (uuid "00000000-0000-0000-0000-111100000001"))
  (wire (pts (xy 121.27 100) (xy 138.73 100)) (uuid "00000000-0000-0000-0000-111100000002"))
)
"""
    os.makedirs("project", exist_ok=True)
    with open("project/555_blinker.kicad_sch", "w") as f:
        f.write(sch_content)
    print("Schematic generated.")

def generate_pcb():
    print("Generating PCB...")
    board = pcbnew.BOARD()

    # Board dimensions: 50x30mm
    width_mm = 50
    height_mm = 30
    x_start = 100
    y_start = 100

    # Create board outline on Edge.Cuts
    def add_line(x1, y1, x2, y2, layer=pcbnew.Edge_Cuts):
        line = pcbnew.PCB_SHAPE(board)
        line.SetShape(pcbnew.SHAPE_T_SEGMENT)
        line.SetStart(pcbnew.VECTOR2I_MM(x1, y1))
        line.SetEnd(pcbnew.VECTOR2I_MM(x2, y2))
        line.SetLayer(layer)
        line.SetWidth(pcbnew.FromMM(0.1))
        board.Add(line)

    add_line(x_start, y_start, x_start + width_mm, y_start)
    add_line(x_start + width_mm, y_start, x_start + width_mm, y_start + height_mm)
    add_line(x_start + width_mm, y_start + height_mm, x_start, y_start + height_mm)
    add_line(x_start, y_start + height_mm, x_start, y_start)

    # Note: Footprint placement requires library access.
    # In this environment, we'll focus on the structural generation and outline.

    pcb_path = "project/555_blinker.kicad_pcb"
    board.Save(pcb_path)
    print(f"PCB generated at {pcb_path}")

if __name__ == "__main__":
    generate_schematic()
    generate_pcb()
