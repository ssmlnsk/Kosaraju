import sys
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from facade import Facade


class Window(QWidget):
    """
    Класс создания окна
    """
    def __init__(self):
        """
        Загрузка окна, прикрепление действий к кнопкам и отображение графа.
        """
        super(Window, self).__init__()
        self.resize(400, 400)
        self.facade = Facade(self)
        self.grid = QtWidgets.QVBoxLayout()
        self.setLayout(self.grid)
        self.figure = plt.figure()
        self.xolst = FigureCanvas(self.figure)
        self.downgrid = QtWidgets.QHBoxLayout()
        self.upgrid = QtWidgets.QHBoxLayout()
        self.btn_add = QtWidgets.QPushButton()
        self.btn_file = QtWidgets.QPushButton()
        self.btn_load = QtWidgets.QPushButton()
        self.btn_clear = QtWidgets.QPushButton()
        self.line1 = QtWidgets.QSpinBox()
        self.line2 = QtWidgets.QSpinBox()
        self.linefile = QtWidgets.QLineEdit()
        self.btn_add.setText("добавить соединение")
        self.btn_add.clicked.connect(self.facade.add_edge)
        self.btn_file.setText("Сохранить")
        self.btn_file.clicked.connect(self.facade.save)
        self.btn_load.setText("Загрузить")
        self.btn_load.clicked.connect(self.facade.load)
        self.btn_clear.setText("Стереть")
        self.btn_clear.clicked.connect(self.facade.clear)
        self.downgrid.addWidget(self.btn_add)
        self.downgrid.addWidget(self.line1)
        self.downgrid.addWidget(self.line2)
        self.downgrid.addWidget(self.btn_clear)
        self.upgrid.addWidget(self.btn_file)
        self.upgrid.addWidget(self.btn_load)
        self.upgrid.addWidget(self.linefile)
        self.grid.addLayout(self.upgrid)
        self.grid.addWidget(self.xolst, 0)
        self.grid.addLayout(self.downgrid)
        self.facade.redraw()


app = QApplication(sys.argv)

if __name__ == '__main__':
    gui = Window()
    gui.show()
    sys.exit(app.exec_())
