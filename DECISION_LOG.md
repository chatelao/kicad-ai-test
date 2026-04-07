# Decision Log

## Design Step 1: 555 Timer Oscillation Parameters
- **Option 1**:  = 0.3s, T_L = 0.7s$ (LED from OUT to GND). Duty cycle 30% on OUT.
- **Option 2**:  = 0.7s, T_L = 0.3s$ (LED from VCC to OUT). Duty cycle 30% LED ON time.
- **Option 3**:  = 0.5s, T_L = 0.5s$ (Standard 50% duty cycle).
- **Selected**: **Option 2**. Achieves 30% active LED time at 1Hz using standard astable configuration and connecting LED to sink current from OUT.

## Design Step 2: Component Values for 1Hz, 30% LED ON
- **Option 1**:  = 1 \mu F, R1 = 560k \Omega, R2 = 430k \Omega$.
- **Option 2**:  = 10 \mu F, R1 = 56k \Omega, R2 = 43k \Omega$.
- **Option 3**:  = 100 \mu F, R1 = 5.6k \Omega, R2 = 4.3k \Omega$.
- **Selected**: **Option 2**. Good balance between capacitor size and leakage current/resistor stability.

## Design Step 3: PCB Generation Method
- **Option 1**: Manual layout in KiCad.
- **Option 2**: `pcbnew` Python API.
- **Option 3**: KiCad IPC API.
- **Selected**: **Option 2**. While Option 3 was preferred, the IPC API (`kipy`) was not available in the environment, necessitating a fallback to the robust `pcbnew` Python API.
