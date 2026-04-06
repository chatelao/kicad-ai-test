# NE555 Datasheet (Summary)

The NE555 is a precision timer capable of producing accurate time delays or oscillation.

## Pinout
1. GND
2. TRIG
3. OUT
4. RESET
5. CONT
6. THRES
7. DISCH
8. VCC

## Astable Operation
- Time High (t1) = 0.693 * (RA + RB) * C
- Time Low (t2) = 0.693 * RB * C
- Period (T) = t1 + t2 = 0.693 * (RA + 2*RB) * C
- Frequency (f) = 1.44 / ((RA + 2*RB) * C)
