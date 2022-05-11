import unittest
from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from gui import Window


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.gui = Window()

    def test_add_edge(self):
        for n in range(8):
            self.gui.line1.setValue(n)
            self.gui.line2.setValue(n+1)
            QTest.mouseClick(self.gui.btn_add, QtCore.Qt.LeftButton)
        self.gui.line1.setValue(6)
        self.gui.line2.setValue(1)
        QTest.mouseClick(self.gui.btn_add, QtCore.Qt.LeftButton)
        for n in range(5):
            self.gui.line1.setValue(n+6)
            self.gui.line2.setValue(n+7)
            QTest.mouseClick(self.gui.btn_add, QtCore.Qt.LeftButton)
        self.gui.line1.setValue(12)
        self.gui.line2.setValue(6)
        QTest.mouseClick(self.gui.btn_add, QtCore.Qt.LeftButton)
        self.assertEqual(list(self.gui.facade.g.nodes), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_clear(self):
        for n in range(15):
            self.gui.line1.setValue(n)
            self.gui.line2.setValue(n + 1)
            QTest.mouseClick(self.gui.btn_add, QtCore.Qt.LeftButton)
        QTest.mouseClick(self.gui.btn_clear, QtCore.Qt.LeftButton)
        self.assertEqual(list(self.gui.facade.g.nodes), [0, 1])

    def test_save_load(self):
        for n in range(15):
            self.gui.line1.setValue(n)
            self.gui.line2.setValue(n + 1)
            QTest.mouseClick(self.gui.btn_add, QtCore.Qt.LeftButton)
        self.gui.linefile.setText('tmp123')
        QTest.mouseClick(self.gui.btn_file, QtCore.Qt.LeftButton)
        QTest.mouseClick(self.gui.btn_clear, QtCore.Qt.LeftButton)
        QTest.mouseClick(self.gui.btn_load, QtCore.Qt.LeftButton)
        self.assertEqual(list(self.gui.facade.g.nodes), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


if __name__ == '__main__':
    unittest.main()
