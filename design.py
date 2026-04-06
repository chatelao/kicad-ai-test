from skidl import *

# 555 Timer Blinking LED @ 1Hz, 30% Active cycle
# T_high = 0.7s (Dark/OFF)
# T_low = 0.3s (Active/ON)
# LED connected between VCC and OUT (Pin 3)

# Components
vcc = Net('VCC')
gnd = Net('GND')

u1 = Part('Timer', 'NE555P', footprint='Package_DIP:DIP-8_W7.62mm')
r1 = Part('Device', 'R', value='56k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
r2 = Part('Device', 'R', value='43k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
c1 = Part('Device', 'C_Polarized', value='10uF', footprint='Capacitor_THT:CP_Radial_D5.0mm_P2.00mm')
c2 = Part('Device', 'C', value='10nF', footprint='Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm')
led1 = Part('Device', 'LED', footprint='LED_THT:LED_D5.0mm')
r_led = Part('Device', 'R', value='1k', footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal')
j1 = Part('Connector', 'Conn_01x02_Pin', footprint='Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical')

# Connections
j1[1] += vcc
j1[2] += gnd

# 555 Power
u1['VCC'] += vcc
u1['GND'] += gnd
u1['~{RST}'] += vcc

# Timing circuit
u1['DISCH'] += r1[1]
r1[2] += vcc
u1['DISCH'] += r2[1]
r2[2] += u1['THRES'], u1['TRIG']
u1['THRES'] += c1[1]
c1[2] += gnd
u1['CONT'] += c2[1]
c2[2] += gnd

# LED circuit (Active LOW)
led1['K'] += u1['OUT']
led1['A'] += r_led[1]
r_led[2] += vcc

# Output netlist
generate_netlist(filename='blink_555.net')
generate_pcb(filename='blink_555.kicad_pcb')
