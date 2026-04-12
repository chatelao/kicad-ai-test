# NE555 Precision Timer Datasheet

The NE555 is a precision timing circuit capable of producing accurate time delays or oscillation.

## Features
- Timing from microseconds to hours.
- Operates in both astable and monostable modes.
- Adjustable duty cycle.
- Output can source or sink 200 mA.

## Pinout
1. GND (Ground)
2. TRIG (Trigger)
3. OUT (Output)
4. RESET (Reset)
5. CONT (Control)
6. THRES (Threshold)
7. DISCH (Discharge)
8. VCC (Supply Voltage)

## Astable Operation (Blinking LED)
For an astable multivibrator:
- $t_{high} = 0.693 \times (R_A + R_B) \times C$
- $t_{low} = 0.693 \times R_B \times C$
- $f = 1.44 / ((R_A + 2 \times R_B) \times C)$
