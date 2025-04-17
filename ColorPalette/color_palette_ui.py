import os
import json
import hou
import sys
from PySide2 import QtCore
from PySide2.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QScrollArea, QGroupBox,
    QGridLayout, QPushButton, QMessageBox, QFrame, QLabel, QSizePolicy
    )

from .color_logic import (
    set_selected_node_color, pick_color, load_pic_color, save_pic_color,
    hex_to_hue_color, hou_color_to_hex
)

def load_pic_color():
    """Load the pick color value from pick_color.json; default to "#7F7F7F" if not available."""
    try:
        path = os.path.join(os.path.dirname(__file__), "pick_color.json")
        with open(path, "r") as f:
            data = json.load(f)
        return data["pic_color"]["gray"]
    except Exception:
        return "#7F7F7F"

def save_pic_color(hex_color):
    """Save the pick color value to pick_color.json."""
    try:
        path = os.path.join(os.path.dirname(__file__), "pick_color.json")
        with open(path, "w") as f:
            json.dump({"pic_color": {"gray": hex_color}}, f)
    except Exception as e:
        print("Error saving pick_color.json:", e)

# Custom button subclass for the Pick Color Button.
class PicColorButton(QPushButton):
    def __init__(self, initial_color, parent=None):
        super(PicColorButton, self).__init__("Pick Color", parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(0, 0)
        self.pic_color = initial_color  # Stored as a hex string.
        self.update_button_color()
        # Connect the single click (the clicked signal).
        self.clicked.connect(self.single_click_action)
    
    def update_button_color(self):
        self.setStyleSheet(f"background-color: {self.pic_color}; border: 1px solid #333; padding: 0; margin: 0;")
    
    def single_click_action(self):
        # Single click: assign the current pic_color to selected nodes.
        set_selected_node_color(self.pic_color)
    
    def mouseDoubleClickEvent(self, event):
        """
        Double click: Open the Houdini color picker with the current button color as initial.
        If a new color is selected, update the button, save the new color, and assign it to selected nodes.
        """
        initial_hou_color = hex_to_hue_color(self.pic_color)
        new_color = pick_color(initial_color=initial_hou_color)
        if new_color:
            new_hex = hou_color_to_hex(new_color)
            self.pic_color = new_hex
            self.update_button_color()
            save_pic_color(new_hex)
            set_selected_node_color(new_hex)
        # Pass the event up.
        super(PicColorButton, self).mouseDoubleClickEvent(event)

class TNTColorPalette(QWidget):
    def __init__(self, parent=None):
        super(TNTColorPalette, self).__init__(parent)
        self.setWindowTitle("TNT Color Palette")
        size_mult = 10
        self.setMinimumSize(3*size_mult, 1.8*size_mult)
        self.init_ui()
        resize_mult = 140
        self.resize(3*resize_mult, 1.8*resize_mult)
        
    def init_ui(self):
        # Load swatch palette from JSON (color_palette.json)
        script_path = os.path.dirname(__file__)
        json_file = os.path.join(script_path, "color_palette.json")
        try:
            with open(json_file, "r") as file:
                self.color_data = json.load(file)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load color_palette.json:\n{e}")
            self.color_data = {}

        # --- Main Layout (vertical) ---
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(4, 4, 4, 4)
        self.setLayout(main_layout)
        
        # --- Top Row: "Pick Color" Button ---
        top_hlayout = QHBoxLayout()
        top_hlayout.setSpacing(0)
        top_hlayout.setContentsMargins(0, 0, 0, 0)

        default_pic_color = load_pic_color()
        self.pic_color_btn = PicColorButton(default_pic_color)

        top_hlayout.addWidget(self.pic_color_btn)
        main_layout.addLayout(top_hlayout)

        # --- Thick Separation Line ---
        sep_line = QFrame()
        sep_line.setFrameShape(QFrame.HLine)
        sep_line.setFrameShadow(QFrame.Sunken)
        sep_line.setLineWidth(5)
        main_layout.addWidget(sep_line)

        # --- Color Swatches: Each category is a row ---
        for category, colors in self.color_data.items():
            row_layout = QHBoxLayout()
            row_layout.setSpacing(0)
            row_layout.setContentsMargins(0, 0, 0, 0)

            for color_name, hex_value in colors.items():
                btn = self.create_color_button(color_name, hex_value)
                row_layout.addWidget(btn)

            main_layout.addLayout(row_layout)

    def create_color_button(self, color_name, hex_value):
        btn = QPushButton()
        r, g, b = self.hex_to_rgb(hex_value)
        hou_color = hou.Color((r, g, b))
        color_str = f"({r:.2f}, {g:.2f}, {b:.2f} )"
        btn.setToolTip(f"{color_name}: {hex_value} {color_str}")
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn.setMinimumSize(0, 0)
        btn.setStyleSheet(
            f"QPushButton {{background-color: {hex_value}; border: 1px solid #333;}}"
        )

        btn.clicked.connect(lambda: self.color_clicked(color_name, hex_value))
        return btn

    def color_clicked(self, name, hex_code):
        # print(f"Clicked Color: {name} -> {hex_code}")
        set_selected_node_color(hex_code)

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip('#')
        return tuple(int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def show_tnt_color_palette():
    parent = hou.qt.floatingPanelWindow(None)
    dialog = TNTColorPalette(parent=parent)
    dialog.setWindowFlags(QtCore.Qt.Window)  # Set as independent window
    dialog.show()
    return dialog

# For standalone testing outside Houdini.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TNTColorPalette()
    window.show()
    sys.exit(app.exec())