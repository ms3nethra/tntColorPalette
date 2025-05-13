import hou
import os
import json

def hex_to_hue_color(hex_color):
    """
    Convert a hex color string to a hou.color object.
    """
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return hou.Color(r, g, b)

def hou_color_to_hex(hou_color):
    """Convert a hou.Color to a hex string using the .rgb() method."""
    # hou_color.rgb() returns a tuple of three floats (r, g, b)
    r, g, b = hou_color.rgb()
    return f"#{int(r * 255):02X}{int(g * 255):02X}{int(b * 255):02X}"

def set_selected_item_color(hex_color):
    """
    Set the color of *all* selected items in the active Network Editor:
    nodes, subnet inputs, sticky notes, backdrops, network boxes, etc.
    """
    color = hex_to_hue_color(hex_color)
    
    # Get all selected items across ALL network editors
    selected_items = hou.selectedItems()

    for item in selected_items:
        try:
            item.setColor(color)
        except AttributeError:
            pass

def pick_color(initial_color=None):
    """
    Launch Houdini's color picker with an optional initial color (hou.Color).
    Returns the chosen hou.Color or None if cancelled.
    """
    if initial_color:
        return hou.ui.selectColor(initial_color=initial_color)
    else:
        return hou.ui.selectColor()
    
def load_pic_color():
    """
    Load the pick color value from 'pick_color.json'.
    Returns the stored hex string (e.g. "#7F7F7F") or the default if not available.
    """
    try:
        path = os.path.join(os.path.dirname(__file__), "pick_color.json")
        with open(path, "r") as f:
            data = json.load(f)
        return data["pic_color"]["gray"]
    except Exception:
        return "#7F7F7F"

def save_pic_color(hex_color):
    """
    Save the given hex color (e.g. "#FF0000") to 'pick_color.json'.
    """
    try:
        path = os.path.join(os.path.dirname(__file__), "pick_color.json")
        with open(path, "w") as f:
            json.dump({"pic_color": {"gray": hex_color}}, f)
    except Exception as e:
        print("Error saving pick_color.json:", e)
