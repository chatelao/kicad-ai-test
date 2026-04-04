# Decision Log

## Decision 1: Circuit Topology
- **Variant 1:** NE555 in Monostable mode (single pulse)
- **Variant 2:** NE555 in Astable mode (continuous blinking)
- **Variant 3:** Discrete transistor multivibrator
- **Selected Option:** Variant 2 (Astable mode) because it meets the "blinking LED" requirement with minimal components.

## Decision 2: Power Source
- **Variant 1:** 9V Battery clip
- **Variant 2:** USB-C connector (5V)
- **Variant 3:** 2-pin Pin Header (5V-12V)
- **Selected Option:** Variant 3 (Pin Header) for simplicity and breadboard compatibility.

## Decision 3: Component Packages
- **Variant 1:** All Through-Hole (THT)
- **Variant 2:** All Surface-Mount (SMD) 0805
- **Variant 3:** Mixed THT and SMD
- **Selected Option:** Variant 1 (THT) to make it easy for beginners to solder.
