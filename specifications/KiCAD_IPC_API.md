# KiCAD IPC API Specification Summary

The KiCAD IPC API is based on gRPC/Protobuf. The server communicates via a socket, typically `ipc:///tmp/kicad/api.sock`.

## Core Concepts
- **DocumentSpecifier**: Reference to a board, schematic, or other KiCad file.
- **KIID**: Unique identifier for every item in a KiCad document.
- **API Server**: Must be enabled in `kicad_common.json` with `"api": { "enable_server": true }`.

## Common Commands
- `GetNets`: Retrieves nets for a given board.
- `GetItemsByNet`: Retrieves copper items for a given net.
- `RefillZones`: Recomputes zone pours.
- `GetVisibleLayers`: Returns enabled layers.
- `SetActiveLayer`: Selects the layer for manual or scripted routing.

## Board Management
- `GetBoardStackup`: Returns layer and material properties.
- `SetBoardEnabledLayers`: Configures which layers are active in the stackup.
- `GetBoardDesignRules`: Retrieves DRC settings.

## Editor Commands (Interactive)
- `InteractiveMoveItems`: Starts a manual move operation via the API.
- `SetActiveLayer`: Changes the layer being viewed/edited.
