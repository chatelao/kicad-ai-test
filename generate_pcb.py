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
        ('C2', 'Capacitor_SMD:C_0805_2012Metric', (90, 110)),
        ('D1', 'LED_SMD:LED_0805_2012Metric', (90, 100))
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

    # Connect Pads to Nets (Basic connections for 555 astable)
    # U1: 1=GND, 2=TRIG, 3=OUT, 4=RST(VCC), 5=CONT, 6=THRES, 7=DISCH, 8=VCC
    def connect(ref, pad_num, net_name):
        pad = fps[ref].FindPadByNumber(str(pad_num))
        if pad and net_name in net_map:
            pad.SetNet(net_map[net_name])
            log_call(f"fps['{ref}'].FindPadByNumber('{pad_num}').SetNet(net_map['{net_name}'])")

    connect('U1', 1, 'GND')
    connect('U1', 2, 'TRIG_THRES')
    connect('U1', 3, 'OUT')
    connect('U1', 4, 'VCC')
    connect('U1', 5, 'CTRL')
    connect('U1', 6, 'TRIG_THRES')
    connect('U1', 7, 'DISCH')
    connect('U1', 8, 'VCC')

    connect('R1', 1, 'VCC')
    connect('R1', 2, 'DISCH')
    connect('R2', 1, 'DISCH')
    connect('R2', 2, 'TRIG_THRES')
    connect('C1', 1, 'TRIG_THRES')
    connect('C1', 2, 'GND')
    connect('C2', 1, 'CTRL')
    connect('C2', 2, 'GND')
    connect('D1', 1, 'OUT')
    connect('D1', 2, 'LED_K')
    connect('R3', 1, 'LED_K')
    connect('R3', 2, 'VCC')

    # Add tracks for a few nets to demonstrate
    def add_track(start_pos, end_pos, net_name):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pcbnew.VECTOR2I(mm_to_iu(start_pos[0]), mm_to_iu(start_pos[1])))
        track.SetEnd(pcbnew.VECTOR2I(mm_to_iu(end_pos[0]), mm_to_iu(end_pos[1])))
        track.SetLayer(pcbnew.F_Cu)
        track.SetWidth(mm_to_iu(0.25))
        if net_name in net_map:
            track.SetNet(net_map[net_name])
        board.Add(track)
        log_call(f"board.Add(pcbnew.PCB_TRACK(board)) # {net_name}")

    # Sample tracks
    add_track((100, 100), (115, 110), 'GND') # Dummy path for GND
    add_track((100, 95), (115, 95), 'VCC')  # Dummy path for VCC

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
    log_call(f"pcbnew.SaveBoard('{board_path}', board)")

if __name__ == "__main__":
    generate_pcb()
