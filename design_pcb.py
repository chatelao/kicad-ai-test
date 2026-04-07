import pcbnew
import os

# Helper to convert mm to internal units (nanometers in KiCad 6+)
def mm_to_iu(mm):
    return int(mm * 1000000)

def create_board():
    board = pcbnew.BOARD()

    # Set up some basic board properties
    settings = board.GetDesignSettings()

    # Define Net Names
    nets = {
        'VCC': pcbnew.NETINFO_ITEM(board, 'VCC'),
        'GND': pcbnew.NETINFO_ITEM(board, 'GND'),
        'OUT': pcbnew.NETINFO_ITEM(board, 'OUT'),
        'DISCH': pcbnew.NETINFO_ITEM(board, 'DISCH'),
        'CONT': pcbnew.NETINFO_ITEM(board, 'CONT'),
        'TRIG_THRES': pcbnew.NETINFO_ITEM(board, 'TRIG_THRES')
    }
    for net in nets.values():
        board.Add(net)

    footprints_data = [
        ('Package_DIP:DIP-8_W7.62mm', 'U1', (50, 50), {
            '1': 'GND', '2': 'TRIG_THRES', '3': 'OUT', '4': 'VCC',
            '5': 'CONT', '6': 'TRIG_THRES', '7': 'DISCH', '8': 'VCC'
        }),
        ('Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', 'R1', (35, 35), {'1': 'VCC', '2': 'DISCH'}),
        ('Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', 'R2', (35, 45), {'1': 'DISCH', '2': 'TRIG_THRES'}),
        ('Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', 'R3', (35, 55), {'1': 'VCC', '2': 'OUT_LED'}), # LED Resistor
        ('Capacitor_THT:CP_Radial_D5.0mm_P2.50mm', 'C1', (65, 35), {'1': 'TRIG_THRES', '2': 'GND'}),
        ('Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm', 'C2', (65, 45), {'1': 'CONT', '2': 'GND'}),
        ('LED_THT:LED_D5.0mm', 'D1', (65, 60), {'1': 'OUT', '2': 'OUT_LED'}) # K:1, A:2
    ]

    # Add extra net for LED anode connection
    out_led_net = pcbnew.NETINFO_ITEM(board, 'OUT_LED')
    board.Add(out_led_net)
    nets['OUT_LED'] = out_led_net

    fps = {}
    for footprint_name, ref, pos, pin_nets in footprints_data:
        lib, name = footprint_name.split(':')
        fp = pcbnew.FootprintLoad('/usr/share/kicad/footprints/' + lib + '.pretty', name)
        if fp:
            fp.SetReference(ref)
            fp.SetPosition(pcbnew.VECTOR2I(mm_to_iu(pos[0]), mm_to_iu(pos[1])))
            board.Add(fp)
            fps[ref] = fp
            for pin_num, net_name in pin_nets.items():
                pad = fp.FindPadByNumber(pin_num)
                if pad:
                    pad.SetNet(nets[net_name])
        else:
            print(f"Could not load footprint {footprint_name}")

    # Add board outline
    points = [
        (25, 25), (75, 25), (75, 75), (25, 75), (25, 25)
    ]
    for i in range(len(points) - 1):
        line = pcbnew.PCB_SHAPE(board)
        line.SetShape(pcbnew.SHAPE_T_SEGMENT)
        line.SetStart(pcbnew.VECTOR2I(mm_to_iu(points[i][0]), mm_to_iu(points[i][1])))
        line.SetEnd(pcbnew.VECTOR2I(mm_to_iu(points[i+1][0]), mm_to_iu(points[i+1][1])))
        line.SetLayer(pcbnew.Edge_Cuts)
        board.Add(line)

    # Simple auto-routing (very basic, just connect pads with tracks)
    # This is not real routing but just showing we CAN add tracks
    # Real routing is complex, but let's connect R1 pin 1 to VCC (U1 pin 8)
    # Actually let's just add one track as proof of concept
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(fps['U1'].FindPadByNumber('8').GetPosition())
    track.SetEnd(fps['R1'].FindPadByNumber('1').GetPosition())
    track.SetLayer(pcbnew.B_Cu)
    track.SetWidth(mm_to_iu(0.25))
    board.Add(track)

    # Save board
    pcbnew.SaveBoard('555.kicad_pcb', board)
    print("Board saved to 555.kicad_pcb")

if __name__ == '__main__':
    create_board()
