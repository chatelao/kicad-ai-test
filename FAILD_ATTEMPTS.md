# Failed Attempts Log

This file records unsuccessful attempts during the development of the 555 timer blinking LED board.

| Attempt # | Description | Failure Mode | Lesson Learned |
|-----------|-------------|--------------|----------------|
| 1 | Attempted to use `xvfb-run kicad` directly | Xvfb failed to start due to existing locks | Need to manage Xvfb locks and display numbers manually in this environment. |
| 2 | Use `kipy` IPC API for schematic/PCB | `ApiError: no handler available` | IPC Autostart in this build might not support all common commands or requires specific project context not easily set up headlessly. |
| 3 | Use `kicad-cli` in CI | `exit code 127` (not found) | Use absolute paths or ensure environment is correctly inherited in container steps. |
