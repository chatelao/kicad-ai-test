# Failed Attempts

## Environment Setup
- **Attempt 1**: Run `xvfb-run kicad --api-server`.
  - **Result**: `xvfb-run: error: Xvfb failed to start`.
- **Attempt 2**: Run `pip install kipy`.
  - **Result**: `ERROR: Could not find a version that satisfies the requirement kipy`.
  - **Correction**: `kipy` is already installed in the environment's site-packages.
