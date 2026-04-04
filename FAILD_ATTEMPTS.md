1. Attempted to run `kicad-cli` and `kibot` locally, but KiCad is not installed in the environment, and `pcbnew` module is missing.
2. Attempted to pull `setsoft/kicad_auto:latest` docker image to run tests, but hit the unauthenticated pull rate limit.
3. Searched for KiCad 9.0 documentation and S-expression examples; results were sparse, indicating the version is extremely new.
4. Inspected Kibot source code for KiCad 9 support; found references to IPC-2581 requiring KiCad 9+, but no explicit `KICAD_9_VER` constant yet.
