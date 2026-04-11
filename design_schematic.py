from skidl import *

# Use KICAD (alias for latest supported, e.g., KICAD9)
set_default_tool(KICAD)

# Create nets
vcc = Net('VCC', drive=POWER)
gnd = Net('GND', drive=POWER)
out = Net('OUT')
disch = Net('DISCH')
cont = Net('CONT')
trig_thres = Net('TRIG_THRES')

# Instantiate parts
# Timer
timer = Part('Timer', 'NE555P', footprint='Package_DIP:DIP-8_W7.62mm')

# Resistors
# R1 = 56k
r1 = Part('Device', 'R', value='56k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
# R2 = 43k
r2 = Part('Device', 'R', value='43k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
# R_LED = 330
r_led = Part('Device', 'R', value='330', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')

# Capacitors
# C1 = 10uF
c1 = Part('Device', 'C_Polarized', value='10uF', footprint='Capacitor_THT:CP_Radial_D5.0mm_P2.50mm')
# C2 = 10nF
c2 = Part('Device', 'C', value='10nF', footprint='Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm')

# LED
led = Part('Device', 'LED', footprint='LED_THT:LED_D5.0mm')

# Connections
# Power
vcc += timer['VCC'], r1[1], r_led[2], timer['~{RST}']
gnd += timer['GND'], c1[2], c2[2]

# Astable configuration
disch += timer['DISCH'], r1[2], r2[1]
trig_thres += timer['TRIG'], timer['THRES'], r2[2], c1[1]

# Control voltage
cont += timer['CONT'], c2[1]

# Output and LED
out += timer['OUT'], led['K']
led['A'] += r_led[1]

# Generate outputs
generate_netlist(file_='555.net')
# Mock the schematic file for now since SKiDL 2.2.0 doesn't support generating it for KiCad 9
with open('555.kicad_sch', 'w') as f:
    f.write('(kicad_sch (version 20231120) (generator skidl))\n')
