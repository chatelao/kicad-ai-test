from skidl import *

# Define nets
vcc = Net('VCC')
gnd = Net('GND')

# Components
# NE555 Timer
# Pins: 1:GND, 2:TRIG, 3:OUT, 4:RESET, 5:CTRL, 6:THRESH, 7:DISCH, 8:VCC
u1 = Part('Timer', 'NE555P', footprint='Package_SO:SOIC-8_3.9x4.9mm_P1.27mm')

# Timing components: f=1Hz, D=30%
# R1=43k, R2=100k, C1=10uF, Diode across R2
r1 = Part('Device', 'R', value='43k', footprint='Resistor_SMD:R_0805_2012Metric')
r2 = Part('Device', 'R', value='100k', footprint='Resistor_SMD:R_0805_2012Metric')
c1 = Part('Device', 'C', value='10uF', footprint='Capacitor_SMD:C_0805_2012Metric')
c2 = Part('Device', 'C', value='10nF', footprint='Capacitor_SMD:C_0805_2012Metric')
d1 = Part('Device', 'D', value='1N4148', footprint='Diode_SMD:D_SOD-123')

# Output
led = Part('Device', 'LED', value='GREEN', footprint='LED_SMD:LED_0805_2012Metric')
r_led = Part('Device', 'R', value='330', footprint='Resistor_SMD:R_0805_2012Metric')

# Power connector
p1 = Part('Connector', 'Conn_01x02_Pin', footprint='Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical')

# Connections
p1[1] += vcc
p1[2] += gnd

u1[1] += gnd # GND
u1[8] += vcc # VCC
u1[4] += vcc # RESET
u1[5] += c2[1] # CTRL
c2[2] += gnd

# Astable configuration with diode for <50% duty cycle
# Th = 0.693 * R1 * C1 (Charge)
# Tl = 0.693 * R2 * C1 (Discharge)
r1[1] += vcc
r1[2] += u1[7], r2[1], d1[1] # DISCH, R2_start, Diode_Anode
d1[2] += r2[2], c1[1], u1[6], u1[2] # Diode_Cathode, R2_end, C1_pos, THRESH, TRIG
c1[2] += gnd

# Output LED
u1[3] += r_led[1] # OUT
r_led[2] += led[1] # LED Anode (pin 1 for Device:LED usually)
led[2] += gnd     # LED Cathode

generate_netlist(filename='circuit.net')
