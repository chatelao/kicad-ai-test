import sys
import os

sys.path.append('/usr/lib/python3/dist-packages')

try:
    import pcbnew
    board = pcbnew.BOARD()
    fp_path = "/usr/share/kicad/footprints/"
    def mm2iu(mm): return pcbnew.FromMM(mm)

    # Setup board rules to be more lenient for this automated generation
    design_settings = board.GetDesignSettings()
    design_settings.m_SolderMaskMinWeb = 0 # Allow small solder mask bridges

    # Add Edge.Cuts
    edge = pcbnew.PCB_SHAPE(board)
    edge.SetShape(pcbnew.SHAPE_T_RECT)
    edge.SetFilled(False)
    edge.SetStart(pcbnew.VECTOR2I(mm2iu(90), mm2iu(90)))
    edge.SetEnd(pcbnew.VECTOR2I(mm2iu(150), mm2iu(130)))
    edge.SetLayer(pcbnew.Edge_Cuts)
    edge.SetWidth(mm2iu(0.1))
    board.Add(edge)

    # 555 DIP-8
    u1 = pcbnew.FootprintLoad(fp_path + "Package_DIP.pretty", "DIP-8_W7.62mm")
    u1.SetReference("U1")
    u1.SetPosition(pcbnew.VECTOR2I(mm2iu(100), mm2iu(110)))
    board.Add(u1)

    # Resistors
    r1 = pcbnew.FootprintLoad(fp_path + "Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")
    r1.SetReference("R1")
    r1.SetPosition(pcbnew.VECTOR2I(mm2iu(120), mm2iu(100)))
    board.Add(r1)

    r2 = pcbnew.FootprintLoad(fp_path + "Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")
    r2.SetReference("R2")
    r2.SetPosition(pcbnew.VECTOR2I(mm2iu(120), mm2iu(110)))
    board.Add(r2)

    r_led = pcbnew.FootprintLoad(fp_path + "Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")
    r_led.SetReference("R_LED")
    r_led.SetPosition(pcbnew.VECTOR2I(mm2iu(120), mm2iu(120)))
    board.Add(r_led)

    # Capacitors
    c1 = pcbnew.FootprintLoad(fp_path + "Capacitor_THT.pretty", "CP_Radial_D5.0mm_P2.00mm")
    c1.SetReference("C1")
    c1.SetPosition(pcbnew.VECTOR2I(mm2iu(140), mm2iu(100)))
    board.Add(c1)

    c2 = pcbnew.FootprintLoad(fp_path + "Capacitor_THT.pretty", "C_Disc_D3.0mm_W1.6mm_P2.50mm")
    c2.SetReference("C2")
    c2.SetPosition(pcbnew.VECTOR2I(mm2iu(140), mm2iu(110)))
    board.Add(c2)

    # LED
    led1 = pcbnew.FootprintLoad(fp_path + "LED_THT.pretty", "LED_D5.0mm")
    led1.SetReference("LED1")
    led1.SetPosition(pcbnew.VECTOR2I(mm2iu(140), mm2iu(120)))
    board.Add(led1)

    pcbnew.SaveBoard("555.kicad_pcb", board)
    print("PCB generated successfully with pcbnew")
except Exception as e:
    print(f"Error generating board: {e}")
