# Failed Attempts

## Environment Setup
- **Attempt 1**: Run `xvfb-run kicad --api-server`.
  - **Result**: `xvfb-run: error: Xvfb failed to start`.
- **Attempt 2**: Run `pip install kipy`.
  - **Result**: `ERROR: Could not find a version that satisfies the requirement kipy`.
  - **Correction**: `kipy` is already installed in the environment's site-packages.
- **Attempt 3**: Start KiCad and connect via `kipy`.
  - **Result**: `kipy.errors.ConnectionError: Failed to send command to KiCad: Timed out`.
  - **Details**: KiCad starts and creates `/tmp/kicad/api.sock`, but all requests (including `ping` and `get_version`) time out, even with a 30s timeout. This may be due to KiCad being in a modal dialog or not fully initialized in the headless environment.
