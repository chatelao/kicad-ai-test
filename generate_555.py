import pcbnew
import sys
import os

def log_ipc(call_str):
    with open("KICAD_IPC_CALLS.md", "a") as f:
        f.write(call_str + "\n")

def mm_to_iu(mm):
    return int(mm * 1000000)

def create_555_pcb():
    board = pcbnew.BOARD()
    log_ipc("board = pcbnew.BOARD()")

    # Define Nets
    nets = ["GND", "VCC", "OUT", "TR_TH", "DIS", "LED_K"]
    net_objs = {}
    for n in nets:
        net = pcbnew.NETINFO_ITEM(board, n)
        board.Add(net)
        net_objs[n] = net

    # Footprint Paths
    fp_root = "/usr/share/kicad/footprints/"
    ic_path = fp_root + "Package_DIP.pretty"
    r_path = fp_root + "Resistor_THT.pretty"
    c_path = fp_root + "Capacitor_THT.pretty"
    led_path = fp_root + "LED_THT.pretty"

    # U1: 555 IC (DIP-8) at (60, 60)
    u1 = pcbnew.FootprintLoad(ic_path, "DIP-8_W7.62mm")
    u1.SetPosition(pcbnew.VECTOR2I_MM(60, 60))
    u1.SetReference("U1")
    board.Add(u1)
    # Pins: 1:GND, 2:TRIG, 3:OUT, 4:RESET, 5:CTRL, 6:THRESH, 7:DISCH, 8:VCC
    u1.FindPadByNumber("1").SetNet(net_objs["GND"])
    u1.FindPadByNumber("2").SetNet(net_objs["TR_TH"])
    u1.FindPadByNumber("3").SetNet(net_objs["OUT"])
    u1.FindPadByNumber("4").SetNet(net_objs["VCC"])
    u1.FindPadByNumber("6").SetNet(net_objs["TR_TH"])
    u1.FindPadByNumber("7").SetNet(net_objs["DIS"])
    u1.FindPadByNumber("8").SetNet(net_objs["VCC"])

    # R1: 10k (VCC -> DIS)
    r1 = pcbnew.FootprintLoad(r_path, "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")
    r1.SetPosition(pcbnew.VECTOR2I_MM(60, 30))
    r1.SetReference("R1")
    board.Add(r1)
    r1.FindPadByNumber("1").SetNet(net_objs["VCC"])
    r1.FindPadByNumber("2").SetNet(net_objs["DIS"])

    # R2: 68k (DIS -> TR_TH)
    r2 = pcbnew.FootprintLoad(r_path, "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")
    r2.SetPosition(pcbnew.VECTOR2I_MM(100, 60))
    r2.SetOrientation(pcbnew.EDA_ANGLE(90, pcbnew.DEGREES_T))
    r2.SetReference("R2")
    board.Add(r2)
    r2.FindPadByNumber("1").SetNet(net_objs["DIS"])
    r2.FindPadByNumber("2").SetNet(net_objs["TR_TH"])

    # C1: 10uF (TR_TH -> GND)
    c1 = pcbnew.FootprintLoad(c_path, "CP_Radial_D5.0mm_P2.00mm")
    c1.SetPosition(pcbnew.VECTOR2I_MM(60, 90))
    c1.SetReference("C1")
    board.Add(c1)
    c1.FindPadByNumber("1").SetNet(net_objs["TR_TH"])
    c1.FindPadByNumber("2").SetNet(net_objs["GND"])

    # D1: LED (OUT -> LED_K)
    led = pcbnew.FootprintLoad(led_path, "LED_D5.0mm")
    led.SetPosition(pcbnew.VECTOR2I_MM(20, 60))
    led.SetReference("D1")
    board.Add(led)
    led.FindPadByNumber("1").SetNet(net_objs["OUT"])
    led.FindPadByNumber("2").SetNet(net_objs["LED_K"])

    # R3: 1k (LED_K -> GND)
    r3 = pcbnew.FootprintLoad(r_path, "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")
    r3.SetPosition(pcbnew.VECTOR2I_MM(20, 90))
    r3.SetOrientation(pcbnew.EDA_ANGLE(90, pcbnew.DEGREES_T))
    r3.SetReference("R3")
    board.Add(r3)
    r3.FindPadByNumber("1").SetNet(net_objs["GND"])
    r3.FindPadByNumber("2").SetNet(net_objs["LED_K"])

    # Board Outline (Edge.Cuts)
    edge_layer = board.GetLayerID("Edge.Cuts")
    def add_line(x1, y1, x2, y2):
        s = pcbnew.PCB_SHAPE(board)
        s.SetShape(pcbnew.SHAPE_T_SEGMENT)
        s.SetStart(pcbnew.VECTOR2I_MM(x1, y1))
        s.SetEnd(pcbnew.VECTOR2I_MM(x2, y2))
        s.SetLayer(edge_layer)
        s.SetWidth(mm_to_iu(0.1))
        board.Add(s)

    add_line(10, 10, 130, 10)
    add_line(130, 10, 130, 130)
    add_line(130, 130, 10, 130)
    add_line(10, 130, 10, 10)

    board.Save("555_blinker.kicad_pcb")
    log_ipc("board.Save('555_blinker.kicad_pcb')")

if __name__ == "__main__":
    create_555_pcb()
