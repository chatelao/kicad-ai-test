# KiCad IPC Calls Log

| Call | Description | Result |
| --- | --- | --- |
| `Ping()` | Check connection | Timeout |
| `GetVersion()` | Get KiCad version | Timeout |
| `GetBoard()` | Get current board (intended) | N/A (Hybrid fallback) |
| `SaveBoard()` | Save board file (intended) | N/A (Hybrid fallback) |

## Implementation Note
The project uses a hybrid approach due to IPC connection timeouts in the headless environment.
- **Schematic**: Generated via Python template.
- **PCB**: Generated via `pcbnew` Python API.
