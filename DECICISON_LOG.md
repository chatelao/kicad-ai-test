# Decision Log

## Step 1: 555 Timer Circuit Configuration
- **Variant 1: Standard Astable Multivibrator (Output Low for Active Cycle)**
  - Logic: LED is connected between VCC and Output (via resistor). LED is ON when Output is LOW.
  - Pros: Simple, no extra components like diodes needed to achieve < 50% duty cycle.
  - Cons: Output sinking current instead of sourcing.
- **Variant 2: Astable Multivibrator with Steering Diode**
  - Logic: Diode across R2 allows charging C through R1 only.
  - Pros: Can achieve any duty cycle; LED can be connected to GND.
  - Cons: Requires an extra diode (e.g., 1N4148).
- **Variant 3: 555 Timer as PWM Generator with Control Voltage**
  - Logic: Use an external voltage to set duty cycle.
  - Pros: Adjustable.
  - Cons: Overly complex for a fixed 1Hz/30% cycle.
- **Selected: Variant 1**
  - Reason: Most efficient use of components to meet the 30% active / 70% dark requirement.

## Step 2: Component Values for 1Hz, 30% Active
- **Variant 1: C = 10uF, R1 = 56k, R2 = 43k**
  - $t_{low} \approx 0.3s$ (Active), $t_{high} \approx 0.7s$ (Dark). Total $\approx 1s$ (1Hz).
- **Variant 2: C = 1uF, R1 = 560k, R2 = 430k**
  - Pros: Smaller capacitor.
  - Cons: High resistor values sensitive to leakage/noise.
- **Variant 3: C = 100uF, R1 = 5.6k, R2 = 4.3k**
  - Pros: Low resistor values.
  - Cons: Large capacitor size.
- **Selected: Variant 1**
  - Reason: Balanced values using common components.

## Step 3: PCB Generation Method
- **Variant 1: KiCAD IPC API (kipy)**
  - Pros: Decoupled, modern approach as requested.
  - Cons: Known stability issues in headless environments.
- **Variant 2: pcbnew Python API**
  - Pros: Very stable, direct access.
  - Cons: Legacy/Tightly coupled.
- **Variant 3: Manual S-expression Generation**
  - Pros: No dependencies.
  - Cons: Extremely tedious and error-prone.
- **Selected: Variant 1 (with Variant 2 as fallback)**
  - Reason: Adhering to project requirements while maintaining a robust fallback.

## Step 4: Footprint Selection
- **Variant 1: Through-hole only**
  - Pros: Easier to hand solder.
  - Cons: Larger PCB size.
- **Variant 2: SMD 0805 for resistors/capacitors/LEDs**
  - Pros: Compact, industry standard.
  - Cons: Slightly harder to hand solder.
- **Variant 3: Mix of DIP and SMD**
  - Pros: Use DIP for the IC (easy to swap) and SMD for passives (compact).
- **Selected: Variant 3**
  - U1: Package_DIP:DIP-8_W7.62mm
  - R1, R2, R3: Resistor_SMD:R_0805_2012Metric
  - C1: Capacitor_SMD:CP_Elec_4x5.4 (Electrolytic SMD)
  - C2: Capacitor_SMD:C_0805_2012Metric
  - D1: LED_SMD:LED_0805_2012Metric
