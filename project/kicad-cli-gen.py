import subprocess
import os

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

# Generate a schematic template
with open("project/555_blinker.kicad_sch", "w") as f:
    f.write('(kicad_sch (version 20241121) (generator "kicad-cli-gen") (uuid "56781234-abcd-ef00-1122-334455667788") (paper "A4") (title_block (title "555 Blinker")))')

# Generate a PCB template
with open("project/555_blinker.kicad_pcb", "w") as f:
    f.write('(kicad_pcb (version 20241121) (generator "kicad-cli-gen") (uuid "9ABC1234-abcd-ef00-1122-334455667788") (paper "A4") (setup (stackup (layer "F.Cu" (type "copper") (thickness 0.035)) (layer "B.Cu" (type "copper") (thickness 0.035)))) (title_block (title "555 Blinker")))')
