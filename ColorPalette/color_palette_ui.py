import os
import json
import hou
import sys
from PySide2 import QtCore
from PySide2.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QScrollArea, QGroupBox,
    QGridLayout, QPushButton, QMessageBox, QFrame, QLabel, QSizePolicy
    )

class TNTColorPalette(QWidget):
    def __init__(self, parent=None):
        super(TNTColorPalette, self).__init__(parent)
        self.setWindowTitle("TNT Color Palette")
        self.resize(400, 400)
        self.init_ui()

    def init_ui(self):
        # get the script directory and load the JSON file
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
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
        
        # --- Top Row: "Pick Color" Button ---
        top_hlayout = QHBoxLayout()
        top_hlayout.setSpacing(0)
        top_hlayout.setContentsMargins(0, 0, 0, 0)

        self.pic_color_btn = QPushButton()
        self.pic_color_btn.setStyleSheet("background-color: #E6E6E6; border: 1px solid #333;")
        self.pic_color_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        top_hlayout.addWidget(self.pic_color_btn)
        main_layout.addLayout(top_hlayout, 1)

        # --- Thick Separation Line ---
        sep_line = QFrame()
        sep_line.setFrameShape(QFrame.HLine)
        sep_line.setFrameShadow(QFrame.Sunken)
        sep_line.setLineWidth(5)
        main_layout.addWidget(sep_line, 1)

        # --- Color Swatches: Each category is a row ---
        for category, colors in self.color_data.items():
            row_layout = QHBoxLayout()
            row_layout.setSpacing(0)
            row_layout.setContentsMargins(0, 0, 0, 0)

            for color_name, hex_value in colors.items():
                btn = self.create_color_button(color_name, hex_value)
                row_layout.addWidget(btn)

            main_layout.addLayout(row_layout, 1)

    def create_color_button(self, color_name, hex_value):
        btn = QPushButton()
        btn.setToolTip(f"{color_name}: {hex_value}")
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        btn.setStyleSheet(
            f"QPushButton {{background-color: {hex_value}; border: 1px solid #333;}}"
        )

        btn.clicked.connect(lambda: self.color_clicked(color_name, hex_value))
        return btn

    def color_clicked(self, name, hex_code):
        print(f"Clicked Color: {name} -> {hex_code}")

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