import hou

def hex_to_hue_color(hex_color):
    """
    Convert a hex color string to a hou.color object.
    """
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return hou.Color(r, g, b)

def set_selected_node_color(hex_color):
    """
    Set the color of all selected nodes
    """
    color = hex_to_hue_color(hex_color)
    nodes = hou.selectedNodes()
    if nodes:
        for node in nodes:
            node.setColor(color)