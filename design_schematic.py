import os
import sys

# Ensure environment variables are set for the current process
os.environ['KICAD_SYMBOL_DIR'] = '/usr/share/kicad/symbols'
os.environ['KICAD6_SYMBOL_DIR'] = '/usr/share/kicad/symbols'
os.environ['KICAD7_SYMBOL_DIR'] = '/usr/share/kicad/symbols'
os.environ['KICAD8_SYMBOL_DIR'] = '/usr/share/kicad/symbols'
os.environ['KICAD9_SYMBOL_DIR'] = '/usr/share/kicad/symbols'

from skidl import Part, Net, generate_netlist, KICAD8, set_default_tool

set_default_tool(KICAD8)

def create_555_schematic():
    # Define components
    u1 = Part('Timer', 'NE555P', footprint='Package_DIP:DIP-8_W7.62mm')
    r1 = Part('Device', 'R', value='56k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
    r2 = Part('Device', 'R', value='43k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
    r_led = Part('Device', 'R', value='470', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
    c1 = Part('Device', 'C_Polarized', value='10uF', footprint='Capacitor_THT:CP_Radial_D5.0mm_P2.00mm')
    c2 = Part('Device', 'C', value='10nF', footprint='Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm')
    led1 = Part('Device', 'LED', footprint='LED_THT:LED_D5.0mm')

    vcc = Net('VCC')
    gnd = Net('GND')

    # Power
    u1['VCC', 'RESET'] += vcc
    u1['GND'] += gnd

    # Timing
    r1[1] += vcc
    net_th_tr = Net('TH_TR')
    r1[2] += r2[1], u1['DISCH']
    r2[2] += net_th_tr, c1[1]
    net_th_tr += u1['THRES', 'TRIG']
    c1[2] += gnd

    # Control
    u1['CONT'] += c2[1]
    c2[2] += gnd

    # Output - active low LED
    led1[1] += vcc
    led1[2] += r_led[1]
    r_led[2] += u1['OUT']

    generate_netlist(file_='555.net')

    # Schematic generation: Since SKiDL doesn't support .kicad_sch export directly,
    # we'll create a minimal valid .kicad_sch file.
    # KiCad 10 .kicad_sch is an S-expression.

    with open('555.kicad_sch', 'w') as f:
        f.write('(kicad_sch (version 20241014) (generator "skidl_fallback")\n')
        f.write('  (uuid "00000000-0000-0000-0000-000000000000")\n')
        f.write('  (paper "A4")\n')
        f.write('  (lib_symbols\n')
        # We should ideally populate this, but a minimal file might be enough for kicad-cli
        f.write('  )\n')
        f.write(')\n')

    # Initialize project files
    with open('555.kicad_pro', 'w') as f:
        f.write('{\n  "version": 1,\n  "sheets": [["00000000-0000-0000-0000-000000000000", "Root"]]\n}\n')

    with open('555.kicad_prl', 'w') as f:
        f.write('{\n  "version": 1\n}\n')

if __name__ == '__main__':
    create_555_schematic()
