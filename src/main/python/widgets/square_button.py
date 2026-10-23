# SPDX-License-Identifier: GPL-2.0-or-later

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout

class SquareButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""
            QPushButton {
                text-align: center;
                padding: 2px 4px;
                margin: 0px;
            }
        """)

        self.scale = 1.2
        self.label = None
        self.word_wrap = False
        self.text = ""

    def setRelSize(self, ratio):
        self.scale = ratio
        self.updateGeometry()

    def setWordWrap(self, state):
        self.word_wrap = state
        self.setText(self.text)

    def sizeHint(self):
        fm = self.fontMetrics()
        size = int(round(fm.height() * self.scale * 1.4))
        size = max(size, 36)
        return QSize(size, size)

    # Override setText to facilitate automatic word wrapping
    def setText(self, text):
        self.text = text
        if self.word_wrap:
            super().setText("")
            if self.label is None:
                self.label = QLabel(text, self)
                self.label.setWordWrap(True)
                self.label.setAlignment(Qt.AlignCenter)
                layout = QHBoxLayout(self)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(self.label,0,Qt.AlignCenter)
            else:
                self.label.setText(text)
        else:
            if self.label is not None:
                self.label.deleteLater()
            super().setText(text)
