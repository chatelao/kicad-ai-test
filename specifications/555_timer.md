# NE555 Timer Specifications

## Pinout
1. GND
2. TRIG
3. OUT
4. RESET
5. CONT
6. THRES
7. DISCH
8. VCC

## Astable Multivibrator Configuration
Frequency $f = \frac{1.44}{(R_1 + 2R_2)C}$
Duty Cycle $D = \frac{R_1 + R_2}{R_1 + 2R_2}$ (for high output)

To get 1Hz with 30% active (high) and 70% dark (low):
Standard 555 astable has $D > 50\%$.
To get $D < 50\%$, we can use a diode across $R_2$ or invert the output.
Alternatively, use the 555 to drive the LED such that it's ON when output is LOW.
If LED is ON when output is LOW:
Active cycle (LED ON) = Low time
Dark cycle (LED OFF) = High time
Target: Low time = 0.3s, High time = 0.7s (Total 1s -> 1Hz)
$t_{high} = 0.693 \cdot (R_1 + R_2) \cdot C = 0.7$
$t_{low} = 0.693 \cdot R_2 \cdot C = 0.3$

$R_2 \cdot C = 0.3 / 0.693 \approx 0.433$
$(R_1 + R_2) \cdot C = 0.7 / 0.693 \approx 1.010$
$R_1 \cdot C = 1.010 - 0.433 = 0.577$

If $C = 10\mu F = 10^{-5} F$:
$R_2 = 0.433 / 10^{-5} = 43.3 k\Omega$ (Use 43k or 47k)
$R_1 = 0.577 / 10^{-5} = 57.7 k\Omega$ (Use 56k or 62k)

Let's use $R_1 = 56k$, $R_2 = 43k$, $C = 10\mu F$.
$t_{low} = 0.693 \cdot 43000 \cdot 10^{-5} = 0.298s$
$t_{high} = 0.693 \cdot (56000 + 43000) \cdot 10^{-5} = 0.686s$
Total period $\approx 0.984s$ ($\approx 1.02 Hz$)
Duty cycle (low) $\approx 0.302$ ($\approx 30\%$)

Components:
- U1: NE555
- C1: 10uF (Timing)
- C2: 10nF (Control voltage bypass)
- R1: 56k
- R2: 43k
- R3: 1k (LED current limit)
- D1: LED
- VCC: 5V
- GND
