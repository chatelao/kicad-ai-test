# Summary: KiCad IPC Plugin Development by Otto Strydom (KiCon 2024)

## Overview
Otto Strydom, an embedded software developer, discusses the major architectural shift in KiCad's plugin system introduced in KiCad 9 and 10. The core change is the transition from a tightly coupled internal Python interpreter to a decoupled Inter-Process Communication (IPC) architecture using gRPC and Protocol Buffers (Protobuf).

## Old vs. New Architecture

### The Old Way (Pre-KiCad 9)
- **Tightly Coupled:** Plugins made direct calls into KiCad's internal code.
- **Version Fragility:** Changes in KiCad's internal C++ code often broke the plugin API between versions.
- **Embedded Interpreter:** KiCad ran a custom, internal Python interpreter that had to be recompiled for every release.

### The New Way (IPC-API)
- **Decoupled:** The plugin and KiCad run as two completely independent processes.
- **Communication:** They communicate via sockets using gRPC and Protobuf messages.
- **System Python:** Plugins run on the user's system Python (or any other language/interpreter), allowing developers to use their own tools and virtual environments.
- **Language Agnostic:** While Otto focuses on Python, the IPC nature allows plugins to be written in other languages.

## Technical Workflow

### 1. Connection and Reference
- **Import:** The library is installed as `kipy-python` but imported as `kipy`.
- **API Reference:** The plugin must first establish a connection to a running KiCad instance and get a reference to the active PCB.

### 2. Data Manipulation
- **Queries:** Footprints, tracks, and pads can be retrieved from the board.
- **Coordinates:** KiCad uses a coordinate system where (0,0) is at the top-left, meaning the Y-axis increases downward.
- **Units:** Internal units are nanometers; the API provides conversion helpers for millimeters.

### 3. Commit-Based Updates (The Git-like Flow)
The new API uses a "Commit" protocol to ensure data consistency:
1. **Begin Commit:** Initialize a change set.
2. **Operations:** Add, update, or remove items in the set.
3. **Push Commit:** Send the changes to KiCad's event queue.
- **Benefits:** Multiple changes are grouped into a single Undo step for the user.

## Installation and Development

### Requirements
- A `plugin.json` file to describe the plugin (name, identifier, entry point, etc.).
- An icon file.
- The Python script(s).
- A `requirements.txt` file for dependencies.

### Installation Path
Plugins are placed in the KiCad plugins folder (e.g., `~/.local/share/kicad/plugins/` on Linux).

### Debugging
- Users must explicitly enable the IPC API in KiCad's options.
- Environment variables like `KICAD_IPC_DEBUG` can be set to see more information in the terminal.

## Key Takeaways from Q&A
- **Virtual Environments:** Each plugin can theoretically run in its own virtual environment with different Python versions, though this puts more responsibility on the user.
- **Schematic Support:** Currently, the IPC API only supports the PCB editor. Schematic support has been "planned" for years and is expected eventually.
- **Consistency:** The commit-push model helps maintain consistency by interacting with KiCad's internal event queue, handling cases where items might be deleted by the user while the plugin is running.
- **DRC Integration:** While you can't directly "raise" a native DRC error via IPC yet, you can run `kicad-cli` via the terminal and combine those results with your plugin logic.
