# Components Specifications

## NE555 Timer
- **Supply Voltage (Vcc):** 4.5V to 16V
- **Output Current:** 200mA
- **Operating Modes:** Astable for blinking
- **Pins:** 1:GND, 2:TRIG, 3:OUT, 4:RESET, 5:CTRL, 6:THRES, 7:DISCH, 8:VCC

## LED
- **Type:** 5mm Red LED
- **Forward Voltage (Vf):** 2.0V
- **Forward Current (If):** 20mA

## Resistors
- **R1:** 1k Ohm (Discharge to VCC)
- **R2:** 470k Ohm (Threshold to Discharge)
- **R3:** 220 Ohm (LED current limiting)

## Capacitors
- **C1:** 1uF (Timing capacitor)
- **C2:** 10nF (Control voltage bypass)
