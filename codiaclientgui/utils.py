import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QBrush, QColor
from PyQt5.QtWidgets import QApplication

Font = {
    'main': QFont(),
    'status': QFont(),
}

Palette = {
    "green": QPalette(),
    "red": QPalette(),
    "gray": QPalette(),
}

Style = {
    "progressBar": "",
}

import sys
if sys.platform == 'win32':
    Font['main'].setFamily("Microsoft YaHei")
    Font['main'].setPointSize(10)
    Font['status'].setFamily("KaiTi")
    Font['status'].setPointSize(10)
    Style['progressBar'] = "QProgressBar { border: 1px solid grey; border-radius: 2px; text-align: center; background-color: #FFFFFF;}QProgressBar::chunk { background-color: #30A132; width: 10px;}"
elif sys.platform == 'darwin':
    Font['main'].setFamily(".AppleSystemUIFont")
    Font['main'].setPointSize(13)
    Font['status'].setFamily(".AppleSystemUIFont")
    Font['status'].setPointSize(13)
else:
    Font['main'].setFamily("Microsoft YaHei")
    Font['main'].setPointSize(13)

greenBrush = QBrush(QColor(80, 160, 30))
greenBrush.setStyle(Qt.SolidPattern)
Palette['green'].setBrush(QPalette.Active, QPalette.Text, greenBrush)
greenBrush = QBrush(QColor(80, 160, 30))
greenBrush.setStyle(Qt.SolidPattern)
Palette['green'].setBrush(QPalette.Inactive, QPalette.Text, greenBrush)
greenBrush = QBrush(QColor(120, 120, 120))
greenBrush.setStyle(Qt.SolidPattern)
Palette['green'].setBrush(QPalette.Disabled, QPalette.Text, greenBrush)

redBrush = QBrush(QColor(160, 0, 30))
redBrush.setStyle(Qt.SolidPattern)
Palette['red'].setBrush(QPalette.Active, QPalette.Text, redBrush)
redBrush = QBrush(QColor(160, 0, 30))
redBrush.setStyle(Qt.SolidPattern)
Palette['red'].setBrush(QPalette.Inactive, QPalette.Text, redBrush)
redBrush = QBrush(QColor(120, 120, 120))
redBrush.setStyle(Qt.SolidPattern)
Palette['red'].setBrush(QPalette.Disabled, QPalette.Text, redBrush)

grayBrush = QBrush(QColor(150, 151, 152))
grayBrush.setStyle(Qt.SolidPattern)
Palette['gray'].setBrush(QPalette.Active, QPalette.Text, grayBrush)
grayBrush = QBrush(QColor(150, 151, 152))
grayBrush.setStyle(Qt.SolidPattern)
Palette['gray'].setBrush(QPalette.Inactive, QPalette.Text, grayBrush)
grayBrush = QBrush(QColor(120, 120, 120))
grayBrush.setStyle(Qt.SolidPattern)
Palette['gray'].setBrush(QPalette.Disabled, QPalette.Text, grayBrush)
