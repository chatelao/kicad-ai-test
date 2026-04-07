from skidl import *
import os

# Set environment variables for symbols
os.environ['KICAD_SYMBOL_DIR'] = '/usr/share/kicad/symbols'
# Defaulting to KICAD8 for netlist generation, as it is widely compatible
set_default_tool(KICAD8)

# Components
# NE555 timer
# To get 30% duty cycle, we use a diode across R2
# T_high = 0.693 * R1 * C
# T_low = 0.693 * R2 * C
# T = 1s, T_high = 0.3s, T_low = 0.7s
# C = 10uF => R1 = 43k, R2 = 100k

timer = Part('Timer', 'NE555P', footprint='Package_DIP:DIP-8_W7.62mm')
r1 = Part('Device', 'R', value='43k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
r2 = Part('Device', 'R', value='100k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
c1 = Part('Device', 'C_Polarized', value='10uF', footprint='Capacitor_THT:CP_Radial_D5.0mm_P2.00mm')
c2 = Part('Device', 'C', value='10nF', footprint='Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm') # Control voltage bypass
d1 = Part('Device', 'D', value='1N4148', footprint='Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal') # Across R2
led = Part('Device', 'LED', value='RED', footprint='LED_THT:LED_D5.0mm')
r_led = Part('Device', 'R', value='1k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
vcc_conn = Part('Connector', 'Conn_01x02_Pin', footprint='Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical')

vcc = Net('VCC')
gnd = Net('GND')

vcc_conn[1] += vcc
vcc_conn[2] += gnd

# 555 Connections
timer['VCC'] += vcc
timer['GND'] += gnd
timer['~{RST}'] += vcc
timer['CONT'] += c2[1]
c2[2] += gnd

discharge = Net('DISCHARGE')
threshold = Net('THRESHOLD')

vcc += r1[1]
r1[2] += discharge
discharge += r2[1]
r2[2] += threshold
discharge += d1[1] # Anode
d1[2] += threshold # Cathode
threshold += timer['THRES'], timer['TRIG'], c1[1]
discharge += timer['DISCH']
c1[2] += gnd

# Output LED
out = Net('OUT')
timer['OUT'] += out
out += r_led[1]
r_led[2] += led[1]
led[2] += gnd

# Try to generate schematic (expected to fail for newer KiCad versions)
try:
    generate_schematic(file_='555.kicad_sch')
except Exception as e:
    print(f"Schematic generation failed: {e}")

# Generate netlist (should work)
generate_netlist(file_='555.net')
