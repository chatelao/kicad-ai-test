import pcbnew
import os

MM_TO_IU = 1000000

def create_board():
    # New PCB
    board = pcbnew.NewBoard('555.kicad_pcb')

    # Create edge cuts (simple rectangle 50x50mm)
    edge_cuts = board.GetLayerID('Edge.Cuts')
    rect = pcbnew.PCB_SHAPE(board)
    rect.SetShape(pcbnew.SHAPE_T_RECT)
    rect.SetStart(pcbnew.VECTOR2I(0, 0))
    rect.SetEnd(pcbnew.VECTOR2I(50 * MM_TO_IU, 50 * MM_TO_IU))
    rect.SetLayer(edge_cuts)
    board.Add(rect)

    # Footprints and placement
    footprints = [
        ('U1', 'Package_DIP.pretty', 'DIP-8_W7.62mm', (25, 25)),
        ('R1', 'Resistor_THT.pretty', 'R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', (10, 10)),
        ('R2', 'Resistor_THT.pretty', 'R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', (10, 20)),
        ('C1', 'Capacitor_THT.pretty', 'CP_Radial_D5.0mm_P2.00mm', (10, 30)),
        ('C2', 'Capacitor_THT.pretty', 'C_Disc_D3.0mm_W1.6mm_P2.50mm', (10, 40)),
        ('D1', 'Diode_THT.pretty', 'D_DO-35_SOD27_P7.62mm_Horizontal', (40, 10)),
        ('D2', 'LED_THT.pretty', 'LED_D5.0mm', (40, 25)),
        ('R3', 'Resistor_THT.pretty', 'R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', (40, 40)),
        ('J1', 'Connector_PinHeader_2.54mm.pretty', 'PinHeader_1x02_P2.54mm_Vertical', (25, 5)),
    ]

    for ref, lib, name, pos in footprints:
        fp_path = os.path.join('/usr/share/kicad/footprints', lib)
        fp = pcbnew.FootprintLoad(fp_path, name)
        if not fp:
            print(f"Failed to load footprint: {lib}/{name}")
            continue
        fp.SetPosition(pcbnew.VECTOR2I(int(pos[0] * MM_TO_IU), int(pos[1] * MM_TO_IU)))
        fp.SetReference(ref)
        board.Add(fp)

    # Simple track generation
    def add_track(start_pos, end_pos, layer='F.Cu'):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pcbnew.VECTOR2I(int(start_pos[0] * MM_TO_IU), int(start_pos[1] * MM_TO_IU)))
        track.SetEnd(pcbnew.VECTOR2I(int(end_pos[0] * MM_TO_IU), int(end_pos[1] * MM_TO_IU)))
        track.SetLayer(board.GetLayerID(layer))
        track.SetWidth(int(0.25 * MM_TO_IU))
        board.Add(track)

    # J1.1 to R1.1
    add_track((25, 5), (10, 10))
    # U1.8 to R1.1
    add_track((21, 21), (10, 10))

    # Save board
    board.Save('555.kicad_pcb')
    print("PCB generated successfully: 555.kicad_pcb")

if __name__ == '__main__':
    create_board()
