import os
import sys

# Add pcbnew path to PYTHONPATH
sys.path.append('/usr/lib/python3/dist-packages')

import pcbnew

def mm_to_iu(mm):
    return int(mm * 1000000)

def log_call(call):
    with open('KICAD_IPC_CALLS.md', 'a') as f:
        f.write(f"- {call}\n")

def generate_pcb():
    board_path = '555.kicad_pcb'
    log_call(f"pcbnew.NewBoard('{board_path}')")
    board = pcbnew.NewBoard(board_path)

    # Footprints and their coordinates (in mm)
    components = [
        ('U1', 'Package_DIP:DIP-8_W7.62mm', (100, 100)),
        ('R1', 'Resistor_SMD:R_0805_2012Metric', (115, 95)),
        ('R2', 'Resistor_SMD:R_0805_2012Metric', (115, 100)),
        ('R3', 'Resistor_SMD:R_0805_2012Metric', (115, 105)),
        ('C1', 'Capacitor_SMD:CP_Elec_4x5.4', (115, 110)),
        ('C2', 'Capacitor_SMD:C_0805_2012Metric', (85, 110)),
        ('D1', 'LED_SMD:LED_0805_2012Metric', (85, 100))
    ]

    # Create Nets
    nets = ['GND', 'VCC', 'OUT', 'TRIG_THRES', 'DISCH', 'CTRL', 'LED_K']
    net_map = {}
    for net_name in nets:
        net = pcbnew.NETINFO_ITEM(board, net_name)
        board.Add(net)
        net_map[net_name] = net
        log_call(f"board.Add(pcbnew.NETINFO_ITEM(board, '{net_name}'))")

    fps = {}
    for ref, fp_name, pos in components:
        log_call(f"pcbnew.FootprintLoad('{fp_name}')")
        lib, fp_id = fp_name.split(':')
        lib_path = f"/usr/share/kicad/footprints/{lib}.pretty"
        plugin = pcbnew.PCB_IO_KICAD_SEXPR()
        fp = plugin.FootprintLoad(lib_path, fp_id)
        fp.SetReference(ref)
        fp.SetPosition(pcbnew.VECTOR2I(mm_to_iu(pos[0]), mm_to_iu(pos[1])))
        board.Add(fp)
        fps[ref] = fp

    # Connect Pads to Nets
    connections = [
        ('U1', 1, 'GND'), ('U1', 2, 'TRIG_THRES'), ('U1', 3, 'OUT'), ('U1', 4, 'VCC'),
        ('U1', 5, 'CTRL'), ('U1', 6, 'TRIG_THRES'), ('U1', 7, 'DISCH'), ('U1', 8, 'VCC'),
        ('R1', 1, 'VCC'), ('R1', 2, 'DISCH'),
        ('R2', 1, 'DISCH'), ('R2', 2, 'TRIG_THRES'),
        ('C1', 1, 'TRIG_THRES'), ('C1', 2, 'GND'),
        ('C2', 1, 'CTRL'), ('C2', 2, 'GND'),
        ('D1', 1, 'OUT'), ('D1', 2, 'LED_K'),
        ('R3', 1, 'LED_K'), ('R3', 2, 'VCC')
    ]

    for ref, pad_num, net_name in connections:
        pad = fps[ref].FindPadByNumber(str(pad_num))
        if pad and net_name in net_map:
            pad.SetNet(net_map[net_name])

    # Routing logic (Star topology to simplify)
    def route_net(net_name):
        pads = []
        for ref, pad_num, n in connections:
            if n == net_name:
                pad = fps[ref].FindPadByNumber(str(pad_num))
                pads.append(pad.GetPosition())

        if len(pads) > 1:
            for i in range(len(pads) - 1):
                p1 = pads[i]
                p2 = pads[i+1]
                # Draw L-shape track
                t1 = pcbnew.PCB_TRACK(board)
                t1.SetStart(p1)
                t1.SetEnd(pcbnew.VECTOR2I(p2.x, p1.y))
                t1.SetLayer(pcbnew.F_Cu)
                t1.SetWidth(mm_to_iu(0.25))
                t1.SetNet(net_map[net_name])
                board.Add(t1)

                t2 = pcbnew.PCB_TRACK(board)
                t2.SetStart(pcbnew.VECTOR2I(p2.x, p1.y))
                t2.SetEnd(p2)
                t2.SetLayer(pcbnew.F_Cu)
                t2.SetWidth(mm_to_iu(0.25))
                t2.SetNet(net_map[net_name])
                board.Add(t2)

    for net_name in nets:
        route_net(net_name)

    # Board Outline
    outline_rect = [(80, 85), (130, 85), (130, 120), (80, 120), (80, 85)]
    for i in range(len(outline_rect) - 1):
        start, end = outline_rect[i], outline_rect[i+1]
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(pcbnew.VECTOR2I(mm_to_iu(start[0]), mm_to_iu(start[1])))
        seg.SetEnd(pcbnew.VECTOR2I(mm_to_iu(end[0]), mm_to_iu(end[1])))
        seg.SetLayer(pcbnew.Edge_Cuts)
        seg.SetWidth(mm_to_iu(0.1))
        board.Add(seg)

    pcbnew.SaveBoard(board_path, board)

if __name__ == "__main__":
    generate_pcb()
