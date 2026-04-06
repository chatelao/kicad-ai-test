import sys
import os

# Try to find pcbnew in typical locations
pcbnew_paths = [
    '/usr/lib/python3/dist-packages',
    '/usr/lib/python3.12/dist-packages',
    '/usr/lib/kicad/plugins/python'
]
for p in pcbnew_paths:
    if os.path.exists(p) and p not in sys.path:
        sys.path.append(p)

try:
    import pcbnew
except ImportError:
    print("pcbnew not found. Please ensure KiCad's Python scripting is available.")
    sys.exit(1)

def mm_to_iu(mm):
    return int(mm * 1000000)

def create_board():
    board = pcbnew.BOARD()

    # Use environment variables or default for footprint search
    fp_base_path = os.environ.get('KICAD_FOOTPRINT_DIR', '/usr/share/kicad/footprints')

    # Footprints to load
    # (ref, lib_path, fp_name, pos_x, pos_y)
    footprints_to_load = [
        ("U1", "Package_SO", "SOIC-8_3.9x4.9mm_P1.27mm", 50, 50),
        ("R1", "Resistor_SMD", "R_0805_2012Metric", 35, 35),
        ("R2", "Resistor_SMD", "R_0805_2012Metric", 45, 35),
        ("C1", "Capacitor_SMD", "C_0805_2012Metric", 35, 65),
        ("C2", "Capacitor_SMD", "C_0805_2012Metric", 65, 35),
        ("D1", "Diode_SMD", "D_SOD-123", 45, 45),
        ("LED1", "LED_SMD", "LED_0805_2012Metric", 65, 65),
        ("R_LED", "Resistor_SMD", "R_0805_2012Metric", 65, 55),
        ("P1", "Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical", 15, 50),
    ]

    modules = {}
    for ref, lib, fp, x, y in footprints_to_load:
        lib_full_path = os.path.join(fp_base_path, lib + ".pretty")
        module = pcbnew.FootprintLoad(lib_full_path, fp)
        if not module:
            print(f"Failed to load footprint {fp} from {lib_full_path}")
            continue

        module.SetReference(ref)
        module.SetPosition(pcbnew.VECTOR2I(mm_to_iu(x), mm_to_iu(y)))
        board.Add(module)
        modules[ref] = module
        print(f"Added {ref} at {x}, {y}")

    # Add some tracks (routing)
    # Simple routing example: Connect P1-1 to VCC (U1-8, R1-1, U1-4)
    # This is manual routing via API as a proof of concept

    def add_track(start_module, start_pad, end_module, end_pad, layer="F.Cu"):
        s_pad = start_module.FindPadByNumber(start_pad)
        e_pad = end_module.FindPadByNumber(end_pad)
        if s_pad and e_pad:
            track = pcbnew.PCB_TRACK(board)
            track.SetStart(s_pad.GetPosition())
            track.SetEnd(e_pad.GetPosition())
            track.SetLayer(board.GetLayerID(layer))
            track.SetWidth(mm_to_iu(0.25))
            board.Add(track)

    # Simplified routing (just a few tracks for demonstration)
    if "P1" in modules and "U1" in modules:
        add_track(modules["P1"], "1", modules["U1"], "8") # P1-1 to VCC (U1-8)
        add_track(modules["P1"], "2", modules["U1"], "1") # P1-2 to GND (U1-1)
        add_track(modules["U1"], "3", modules["R_LED"], "1") # U1-3 to R_LED-1

    # Set edge cuts (simple rectangle)
    edge_cuts = board.GetLayerID("Edge.Cuts")
    points = [(0,0), (80,0), (80,80), (0,80), (0,0)]
    for i in range(len(points)-1):
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(pcbnew.VECTOR2I(mm_to_iu(points[i][0]), mm_to_iu(points[i][1])))
        seg.SetEnd(pcbnew.VECTOR2I(mm_to_iu(points[i+1][0]), mm_to_iu(points[i+1][1])))
        seg.SetLayer(edge_cuts)
        board.Add(seg)

    # Save the board
    board.Save("board.kicad_pcb")
    print("Saved board.kicad_pcb with basic routing")

if __name__ == "__main__":
    create_board()
