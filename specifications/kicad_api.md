# KiCad IPC API Plugin Schema (v1)

Derived from `/usr/share/kicad/schemas/api.v1.schema.json`

## Plugin Object
- **identifier**: String (pattern: ^[a-zA-Z][-_a-zA-Z0-9.]{0,98}[a-zA-Z0-9]$)
- **name**: Human-readable name (max 200 chars)
- **description**: Long-form description (max 500 chars)
- **runtime**: Object
    - **type**: "python" or "exec"
    - **min_version**: Minimum Python version (optional)
- **actions**: Array of Action objects

## Action Object
- **identifier**: Unique within plugin (pattern: ^[a-zA-Z][-_a-zA-Z0-9.]{0,48}[a-zA-Z0-9]$)
- **name**: Human-readable name
- **description**: Human-readable description
- **show-button**: Boolean (default toolbar visibility)
- **scopes**: Array of ["pcb", "schematic", "footprint", "symbol", "project_manager"]
- **entrypoint**: Path to script or executable
- **icons-light**: Array of PNG paths
- **icons-dark**: Array of PNG paths
