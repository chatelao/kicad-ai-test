# NE555 Timer Datasheet Summary

## Pinout
1. **GND**: Ground (0V)
2. **TRIGGER**: Input to start timing. Active when voltage < 1/3 VCC.
3. **OUTPUT**: Output signal.
4. **RESET**: Resets the timer. Active low. Usually connected to VCC if not used.
5. **CONTROL VOLTAGE**: Access to internal voltage divider (2/3 VCC). Usually bypassed with 10nF cap to GND.
6. **THRESHOLD**: Input to end timing. Active when voltage > 2/3 VCC.
7. **DISCHARGE**: Open collector output to discharge the timing capacitor.
8. **VCC**: Supply voltage (typically 5V to 15V).

## Astable Multivibrator Circuit
- R1 between VCC and Pin 7.
- R2 between Pin 7 and Pin 6/2.
- C between Pin 6/2 and GND.

### Formulas
- $T_{high} = 0.693 \times (R1 + R2) \times C$
- $T_{low} = 0.693 \times R2 \times C$
- $T_{total} = T_{high} + T_{low} = 0.693 \times (R1 + 2R2) \times C$
- $Frequency = \frac{1}{T_{total}}$
- $Duty Cycle (High) = \frac{R1 + R2}{R1 + 2R2}$

### LED Blinking 1Hz, 30% Active / 70% Dark
To achieve 30% active time with a standard 555 (where $T_{high} > T_{low}$), we connect the LED between VCC and Pin 3 (Active LOW).
- $T_{low} = 0.3s$ (Active/ON)
- $T_{high} = 0.7s$ (Dark/OFF)

Using $C = 10\mu F$:
- $R2 = \frac{0.3}{0.693 \times 10^{-5}} \approx 43.3k\Omega$
- $R1 + R2 = \frac{0.7}{0.693 \times 10^{-5}} \approx 101k\Omega \implies R1 \approx 57.7k\Omega$

Selected values:
- $R1 = 56k\Omega$
- $R2 = 43k\Omega$
- $C = 10\mu F$
