from skidl import *
import os

# Set environment variables for KiCad symbol libraries
KICAD_SYMBOL_DIR = "/usr/share/kicad/symbols"
os.environ["KICAD_SYMBOL_DIR"] = KICAD_SYMBOL_DIR
os.environ["KICAD6_SYMBOL_DIR"] = KICAD_SYMBOL_DIR
os.environ["KICAD7_SYMBOL_DIR"] = KICAD_SYMBOL_DIR
os.environ["KICAD8_SYMBOL_DIR"] = KICAD_SYMBOL_DIR
os.environ["KICAD9_SYMBOL_DIR"] = KICAD_SYMBOL_DIR

# Also set directly in skidl
lib_search_paths[KICAD] = [KICAD_SYMBOL_DIR]

# Define the 555 timer astable circuit
# Target: 1Hz, 30% Active (LED ON when output LOW)
# R1 = 56k, R2 = 43k, C1 = 10uF

# Nets
vcc = Net('VCC')
gnd = Net('GND')
out = Net('OUT')
trig_thres = Net('TRIG_THRES')
disch = Net('DISCH')
ctrl = Net('CTRL')

# Components
# Use parts from Timer, Device, LED, and Power libraries
u1 = Part('Timer', 'NE555P', footprint='Package_DIP:DIP-8_W7.62mm')
r1 = Part('Device', 'R', value='56k', footprint='Resistor_SMD:R_0805_2012Metric')
r2 = Part('Device', 'R', value='43k', footprint='Resistor_SMD:R_0805_2012Metric')
r3 = Part('Device', 'R', value='1k', footprint='Resistor_SMD:R_0805_2012Metric')
c1 = Part('Device', 'C_Polarized', value='10uF', footprint='Capacitor_SMD:CP_Elec_4x5.4')
c2 = Part('Device', 'C', value='10nF', footprint='Capacitor_SMD:C_0805_2012Metric')
d1 = Part('Device', 'LED', value='RED', footprint='LED_SMD:LED_0805_2012Metric')

# Connections
# VCC/GND to U1
vcc += u1['VCC'], u1['~{RST}']
gnd += u1['GND']

# Timing network
vcc += r1[1]
r1[2] += disch, r2[1]
r2[2] += trig_thres, c1[1]
gnd += c1[2]

# Connect U1 timing pins
u1['DISCH'] += disch
u1['TRIG'] += trig_thres
u1['THRES'] += trig_thres

# Bypass capacitor for control voltage
u1['CONT'] += ctrl
ctrl += c2[1]
gnd += c2[2]

# Output LED circuit (Active Low)
u1['OUT'] += out
out += d1['K']
d1['A'] += r3[1]
r3[2] += vcc

# ERC and Generate
# generate_schematic is not implemented for KiCad 9 in skidl 2.2.0
# We use generate_netlist which works and can be used to import into PCB
generate_netlist(file_='555.net')
