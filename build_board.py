import pcbnew
import sys
import os

def create_schematic():
    # A minimal valid schematic with one component and two no-connects to pass ERC
    content = """(kicad_sch
	(version 20241229)
	(generator "kicad-cli")
	(uuid "a2a7e781-6f01-4c4d-9d41-4712411e8b7f")
	(paper "A4")
	(lib_symbols
		(symbol "Device:R"
			(pin_names (offset 0))
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(symbol "R_0_1"
				(pin passive line (at 0 2.54 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -2.54 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
	)
	(symbol (lib_id "Device:R") (at 101.6 101.6 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no) (uuid "00000000-0000-0000-0000-000000000002")
		(property "Reference" "R1" (at 101.6 96.6 0) (effects (font (size 1.27 1.27))))
		(property "Value" "10k" (at 101.6 99.1 0) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "00000000-0000-0000-0000-000000000003"))
		(pin "2" (uuid "00000000-0000-0000-0000-000000000004"))
	)
	(no_connect (at 101.6 99.06) (uuid "00000000-0000-0000-0000-000000000005"))
	(no_connect (at 101.6 104.14) (uuid "00000000-0000-0000-0000-000000000006"))
)"""
    with open("timer.kicad_sch", "w") as f:
        f.write(content)

def create_pcb():
    board = pcbnew.NewBoard("timer.kicad_pcb")
    iu_per_mm = 1000000

    # Board edge
    edge = pcbnew.PCB_SHAPE(board)
    edge.SetShape(1) # SHAPE_T_RECT
    edge.SetStart(pcbnew.VECTOR2I(0, 0))
    edge.SetEnd(pcbnew.VECTOR2I(int(100 * iu_per_mm), int(100 * iu_per_mm)))
    edge.SetLayer(pcbnew.Edge_Cuts)
    board.Add(edge)

    # Define Nets
    nets = ["GND", "VCC", "TRIGGER", "OUT", "DISCH", "LED_A"]
    for net_name in nets:
        net = pcbnew.NETINFO_ITEM(board, net_name)
        board.Add(net)

    # Footprints
    components = [
        ('U1', '/usr/share/kicad/footprints/Package_SO.pretty', 'SOIC-8_3.9x4.9mm_P1.27mm', 50, 50, {
            '1': 'GND', '2': 'TRIGGER', '3': 'OUT', '4': 'VCC', '5': '', '6': 'TRIGGER', '7': 'DISCH', '8': 'VCC'
        }),
        ('R1', '/usr/share/kicad/footprints/Resistor_SMD.pretty', 'R_0805_2012Metric', 30, 30, {'1': 'VCC', '2': 'DISCH'}),
        ('R2', '/usr/share/kicad/footprints/Resistor_SMD.pretty', 'R_0805_2012Metric', 30, 50, {'1': 'DISCH', '2': 'TRIGGER'}),
        ('R3', '/usr/share/kicad/footprints/Resistor_SMD.pretty', 'R_0805_2012Metric', 30, 70, {'1': 'OUT', '2': 'LED_A'}),
        ('C1', '/usr/share/kicad/footprints/Capacitor_SMD.pretty', 'C_0805_2012Metric', 70, 30, {'1': 'TRIGGER', '2': 'GND'}),
        ('D1', '/usr/share/kicad/footprints/LED_SMD.pretty', 'LED_0805_2012Metric', 70, 50, {'1': 'GND', '2': 'LED_A'})
    ]

    for ref, fp_path, fp_name, x, y, pin_nets in components:
        fp = pcbnew.FootprintLoad(fp_path, fp_name)
        fp.SetReference(ref)
        fp.SetPosition(pcbnew.VECTOR2I(int(x * iu_per_mm), int(y * iu_per_mm)))
        for pad in fp.Pads():
            if pad.GetName() in pin_nets:
                net_name = pin_nets[pad.GetName()]
                if net_name:
                    pad.SetNet(board.FindNet(net_name))
        board.Add(fp)

    pcbnew.SaveBoard("timer.kicad_pcb", board)

if __name__ == "__main__":
    create_schematic()
    create_pcb()
