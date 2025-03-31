import os
import json
import hou
import sys
from PySide2 import QtCore
from PySide2.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QScrollArea, QGroupBox,
    QGridLayout, QPushButton, QMessageBox, QLabel
    )

class TNTColorPalette(QWidget):
    def __init__(self, parent=None):
        super(TNTColorPalette, self).__init__(parent)
        self.setWindowTitle("TNT Color Palette")
        self.resize(400,400)
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


        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)
        

        vlayout1 = QVBoxLayout()
        self.pic_color_btn = QPushButton()
        vlayout1.addWidget(self.pic_color_btn)

        vlayout2 = QVBoxLayout()
        rgb_hlayout = QHBoxLayout()
        grayscale_hlayout = QHBoxLayout()
        pastel_hlayout = QHBoxLayout()
        light_hlayout = QHBoxLayout()
        pure_hlayout = QHBoxLayout()
        dark_hlayout = QHBoxLayout()
        darker_hlayout = QHBoxLayout()
        pale_hlayout = QHBoxLayout()
        vlayout2.addLayout(rgb_hlayout)
        vlayout2.addLayout(grayscale_hlayout)
        vlayout2.addLayout(pastel_hlayout)
        vlayout2.addLayout(light_hlayout)
        vlayout2.addLayout(pure_hlayout)
        vlayout2.addLayout(dark_hlayout)
        vlayout2.addLayout(darker_hlayout)
        vlayout2.addLayout(pale_hlayout)

        main_layout.addLayout(vlayout1)
        # main_layout.addWidget()
        main_layout.addLayout(vlayout2)

        for color_type, color_patette in self.color_data.items():
            if color_type == "RGB":
                for colorname, hexvalue in color_patette.items():
                    rgb_btn = QPushButton()
                    rgb_hlayout.addWidget(rgb_btn)

            if color_type == "Grayscale":
                for colorname, hexvalue in color_patette.items():
                    grayscale_btn = QPushButton()
                    grayscale_hlayout.addWidget(grayscale_btn)

            if color_type == "Pastel":
                for colorname, hexvalue in color_patette.items():
                    pastel_btn = QPushButton()
                    pastel_hlayout.addWidget(pastel_btn)

            if color_type == "Light":
                for colorname, hexvalue in color_patette.items():
                    light_btn = QPushButton()
                    light_hlayout.addWidget(light_btn)

            if color_type == "Pure":
                for colorname, hexvalue in color_patette.items():
                    pure_btn = QPushButton()
                    pure_hlayout.addWidget(pure_btn)

            if color_type == "Dark":
                for colorname, hexvalue in color_patette.items():
                    dark_btn = QPushButton()
                    dark_hlayout.addWidget(dark_btn)

            if color_type == "Darker":
                for colorname, hexvalue in color_patette.items():
                    darker_btn = QPushButton()
                    darker_hlayout.addWidget(darker_btn)

            if color_type == "Pale":
                for colorname, hexvalue in color_patette.items():
                    pale_btn = QPushButton()
                    pale_hlayout.addWidget(pale_btn)



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