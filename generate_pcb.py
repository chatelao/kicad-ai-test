import pcbnew
import sys
sys.path.append('/usr/lib/python3/dist-packages')

def mm_to_iu(mm):
    return int(mm * 1000000)

def create_board():
    board = pcbnew.NewBoard('555_timer.kicad_pcb')

    # Add outline
    edge_cuts = board.GetLayerID('Edge.Cuts')
    points = [(0, 0), (50, 0), (50, 50), (0, 50), (0, 0)]
    for i in range(len(points) - 1):
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(pcbnew.VECTOR2I(mm_to_iu(points[i][0]), mm_to_iu(points[i][1])))
        seg.SetEnd(pcbnew.VECTOR2I(mm_to_iu(points[i+1][0]), mm_to_iu(points[i+1][1])))
        seg.SetLayer(edge_cuts)
        seg.SetWidth(mm_to_iu(0.1))
        board.Add(seg)

    # Footprints
    u1 = pcbnew.FootprintLoad('/usr/share/kicad/footprints/Package_SO.pretty', 'SOIC-8_3.9x4.9mm_P1.27mm')
    u1.SetReference('U1')
    u1.SetPosition(pcbnew.VECTOR2I(mm_to_iu(25), mm_to_iu(25)))
    board.Add(u1)

    passives = [
        ('R1', 'Resistor_SMD.pretty', 'R_0805_2012Metric', (15, 20)),
        ('R2', 'Resistor_SMD.pretty', 'R_0805_2012Metric', (15, 30)),
        ('R3', 'Resistor_SMD.pretty', 'R_0805_2012Metric', (35, 20)),
        ('C1', 'Capacitor_SMD.pretty', 'C_0805_2012Metric', (15, 40)),
        ('C2', 'Capacitor_SMD.pretty', 'C_0805_2012Metric', (25, 40)),
        ('D1', 'LED_SMD.pretty', 'LED_0805_2012Metric', (35, 30)),
    ]

    for ref, lib, fp, pos in passives:
        f = pcbnew.FootprintLoad('/usr/share/kicad/footprints/' + lib, fp)
        f.SetReference(ref)
        f.SetPosition(pcbnew.VECTOR2I(mm_to_iu(pos[0]), mm_to_iu(pos[1])))
        board.Add(f)

    pcbnew.SaveBoard('555_timer.kicad_pcb', board)

    # Downgrade version in file to match Kibot's older KiCad
    with open('555_timer.kicad_pcb', 'r') as f:
        content = f.read()
    content = content.replace('(version 20241229)', '(version 20240108)')
    with open('555_timer.kicad_pcb', 'w') as f:
        f.write(content)

    print("Generated 555_timer.kicad_pcb and downgraded version")

if __name__ == "__main__":
    create_board()
