# Failed Attempts Log

## Attempt 1: Using `pcbnew.from_mm()`
- **Error**: `module 'pcbnew' has no attribute 'from_mm'`.
- **Reason**: `from_mm` is not available in the KiCAD 9.0 Python API version in the Ubuntu distribution.
- **Solution**: Defined a custom `mm_to_iu(mm)` function multiplying by `1,000,000`.

## Attempt 2: PCB Outline (Edge.Cuts)
- **Error**: `[invalid_outline]: Board has malformed outline (no edges found on Edge.Cuts layer)`.
- **Reason**: Initial board creation did not include `PCB_SHAPE` objects on the `Edge.Cuts` layer.
- **Solution**: Added four `PCB_SHAPE` segments (type `SHAPE_T_SEGMENT`) on the `Edge.Cuts` layer to define a 60x60mm rectangle.

## Attempt 3: Loading Footprints from Standard Library
- **Error**: Potential failure to find footprints without explicit library paths.
- **Reason**: The script assumes footprints exist at `/usr/share/kicad/footprints/`.
- **Solution**: Verified path and used `FootprintLoad` with the absolute path to the `.pretty` directory.
