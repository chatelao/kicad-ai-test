# Decision Log

## Design Step 1: 555 Timer Oscillation Frequency
- **Variant 1 (Slow Blink):** R1=1k, R2=1M, C1=1uF (~0.7s ON, ~0.7s OFF)
- **Variant 2 (Fast Blink):** R1=1k, R2=100k, C1=1uF (~0.07s ON, ~0.07s OFF)
- **Variant 3 (Standard):** R1=1k, R2=470k, C1=1uF (~0.3s ON, ~0.3s OFF)
- **Selected Option:** Variant 3 (Standard)

## Design Step 2: PCB Layout Strategy
- **Variant 1 (Single Sided):** All traces on the bottom layer, components on top.
- **Variant 2 (Double Sided):** Ground plane on bottom, traces on top.
- **Variant 3 (Minimalist):** Compact layout with minimal trace lengths.
- **Selected Option:** Variant 1 (Single Sided) for ease of DIY fabrication simulation.

## Design Step 3: LED Driving Configuration
- **Variant 1 (Sinking):** LED connected between VCC and Output (Low to turn ON).
- **Variant 2 (Sourcing):** LED connected between Output and GND (High to turn ON).
- **Variant 3 (Bipolar):** Two LEDs in opposite directions (Toggle between colors).
- **Selected Option:** Variant 2 (Sourcing) for simplicity.
