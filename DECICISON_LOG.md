# Decision Log

## Circuit Design: Timing Components
1. **Variant 1:** R1=43k, R2=100k, C1=10uF, Diode across R2. Duty cycle ~30%. (Selected)
2. **Variant 2:** R1=100k, R2=43k, C1=10uF. Standard astable (D > 50%).
3. **Variant 3:** PWM with 555 and potentiometer. More complex.

## PCB Tooling
1. **Variant 1:** SKiDL and pcbnew Python API. Robust and flexible in headless environments. (Selected)
2. **Variant 2:** KiCad IPC API. Currently unstable in this environment due to socket timeouts.
3. **Variant 3:** Manual KiCad GUI design. Impossible in headless sandbox.

## Documentation format
1. **Variant 1:** Markdown summary of datasheets. Easy to read and searchable. (Selected)
2. **Variant 2:** Raw PDF files. Not searchable or readable by all LLMs.
3. **Variant 3:** HTML to Markdown conversion. Hard to maintain.
