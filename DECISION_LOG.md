# Decision Log

## Decision 1: Circuit Topology
### Variants
1. **Astable Multivibrator**: Continuously oscillates, suitable for a blinking LED.
2. **Monostable Multivibrator**: Single pulse upon trigger, requires external input to blink.
3. **Bistable Multivibrator**: Two stable states, toggles on input, not suitable for automatic blinking.

### Selected Option
- **Astable Multivibrator**: Best fit for the goal of a simple blinking LED.

---

## Decision 2: Component Package Types
### Variants
1. **DIP-8 (Through-Hole)**: Easy to hand-solder, good for prototyping.
2. **SOIC-8 (SMD)**: Smaller footprint, industry standard for compact designs.
3. **TSSOP-8 (SMD)**: Extremely small, challenging to hand-solder without specialized equipment.

### Selected Option
- **SOIC-8 (SMD)**: Provides a modern, compact design while remaining relatively easy to assemble.

---

## Decision 3: PCB Manufacturer
### Variants
1. **JLCPCB**: Low cost, fast turnaround, popular for hobbyist projects.
2. **PCBWay**: High quality, wide range of specialized services.
3. **OSHPark**: Excellent quality, focused on open-source community, distinct purple mask.

### Selected Option
- **JLCPCB**: Selected for its cost-effectiveness and rapid prototyping capabilities.
