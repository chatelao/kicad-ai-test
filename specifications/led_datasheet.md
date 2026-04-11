# LED Specifications (Generic SMD 0805)

## Characteristics
- **Forward Voltage ($V_f$):** 2.0V (Standard Red)
- **Forward Current ($I_f$):** 20mA (Max), 3-5mA (Typical)
- **Footprint:** LED_0805_2012Metric

## Current Limiting Resistor Calculation
Given $V_{cc} = 5V$, $V_f = 2.0V$, $I_f = 3mA$:
$R = \frac{V_{cc} - V_f}{I_f} = \frac{5 - 2}{0.003} = 1000 \Omega = 1k\Omega$
Selected Resistor: 1k (Standard 0805)
