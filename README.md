
# TNT Color Palette for Houdini

## About

The **TNT Color Palette** is a custom UI tool developed for Houdini using Python and PySide2. It allows artists to quickly assign consistent, vibrant colors to nodes, network boxes, sticky notes, and more. The tool integrates into Houdini's main menu, node context menu, and supports customizable hotkeys.

---

## Features

- PySide2-based UI docked in Houdini
- Includes grayscale, warm, cool, and vibrant color gradients
- One-click color assignment to all selected items
- Remembers last picked custom color
- Double-click to open Houdini’s color picker
- Fully embedded in:
  - Main menu under `tnt script`
  - Node right-click context menu (at the bottom)
  - Keyboard shortcut system (customizable)

---

## Installation

1. Copy the full folder and file structure into your Houdini preferences directory:

2. Confirm that:
- `tntScripts` is located in `Documents/houdini20.5/scripts/python`
- `tntIcons` is located in `Documents/houdini20.5/scripts/python`
- `MainMenuCommon.xml` is in `Documents/houdini20.5/`
- `OPmenu.xml` is also in `Documents/houdini20.5/`

3. Restart Houdini.

---

## Assigning a Hotkey

### Option 1: Right-Click Shortcut Binding (Recommended)

1. In Houdini, right-click any node in the Network Editor.
2. Go to: `TNT Scripts → TNT Color Palette`
3. Hold `Ctrl + Shift + Alt` and **left-click** on the menu item.
4. Houdini will open the Hotkey Editor with the action pre-selected.
5. Assign a hotkey like `C`, or any free combination.
6. Save and close.

> Note: Assigning to just `C` will override Houdini’s default color palette shortcut, which is fine if you're using this tool as a replacement.

### Option 2: Right-Click Shortcut Binding (Recommended)

1. In Houdini, Main menu.
2. Go to: `TNT Scripts → TNT Color Palette`
3. Hold `Ctrl + Shift + Alt` and **left-click** on the menu item.
4. Houdini will open the Hotkey Editor with the action pre-selected.
5. Assign a hotkey like `Ctrl + Shift + Alt + c`, or any free combination.
6. Save and close.
---

## Contact

Created by **Thrinethra MS**   
[https://www.linkedin.com/in/ms3nethra/]

---


