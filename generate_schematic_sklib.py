from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

generate_schematic = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'NE555P', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'NE555P'}), 'ref_prefix':'U', 'fplist':['Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'Package_DIP:DIP-8_W7.62mm'], 'footprint':'Package_DIP:DIP-8_W7.62mm', 'keywords':'single timer 555', 'description':'Precision Timers, 555 compatible, PDIP-8', 'datasheet':'http://www.ti.com/lit/ds/symlink/ne555.pdf', 'pins':[
            Pin(num='1',name='GND',func=pin_types.PWRIN),
            Pin(num='8',name='VCC',func=pin_types.PWRIN),
            Pin(num='2',name='TRIG',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='OUT',func=pin_types.OUTPUT,unit=1),
            Pin(num='4',name='~{RST}',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='CONT',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='THRES',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='DISCH',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'R'}), 'ref_prefix':'R', 'fplist':[''], 'footprint':'Resistor_SMD:R_0805_2012Metric', 'keywords':'R res resistor', 'description':'Resistor', 'datasheet':'', 'pins':[
            Pin(num='1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'C_Polarized', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'C_Polarized'}), 'ref_prefix':'C', 'fplist':[''], 'footprint':'Capacitor_SMD:CP_Elec_4x5.4', 'keywords':'cap capacitor', 'description':'Polarized capacitor', 'datasheet':'', 'pins':[
            Pin(num='1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'C', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'C'}), 'ref_prefix':'C', 'fplist':[''], 'footprint':'Capacitor_SMD:C_0805_2012Metric', 'keywords':'cap capacitor', 'description':'Unpolarized capacitor', 'datasheet':'', 'pins':[
            Pin(num='1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LED', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LED'}), 'ref_prefix':'D', 'fplist':[''], 'footprint':'LED_SMD:LED_0805_2012Metric', 'keywords':'LED diode', 'description':'Light emitting diode', 'datasheet':'', 'pins':[
            Pin(num='1',name='K',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='A',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] })])