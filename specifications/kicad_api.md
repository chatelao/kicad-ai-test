# KiCad IPC API Specifications
Derived from: https://gitlab.com/kicad/code/kicad/-/raw/master/api/CMakeLists.txt?inline=false

## Overview
The KiCad IPC API is based on Protobuf and gRPC, allowing external applications to control KiCad via a Unix domain socket.

## Proto Files
- `common/envelope.proto`
- `common/types/base_types.proto`
- `common/types/enums.proto`
- `common/types/jobs.proto`
- `common/types/project_settings.proto`
- `common/types/wizards.proto`
- `common/commands/base_commands.proto`
- `common/commands/editor_commands.proto`
- `common/commands/project_commands.proto`
- `board/board.proto`
- `board/board_commands.proto`
- `board/board_jobs.proto`
- `board/board_types.proto`
- `schematic/schematic_types.proto`
- `schematic/schematic_commands.proto`
- `schematic/schematic_jobs.proto`
