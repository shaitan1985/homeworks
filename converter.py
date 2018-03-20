import sys

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)


class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()
        self.initSignals()
        self.changeBtn()


    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)

        self.convertBtn = QPushButton('Перевести', self)
        self.clearBtn = QPushButton('Сброс', self)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.clearBtn.clicked.connect(self.clearAmounts)
        self.srcAmount.valueChanged.connect(self.changeBtn)
        self.resultAmount.valueChanged.connect(self.changeBtn)

    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(w)

    def onClickConvertBtn(self):
        value = self.srcAmount.value()

        if self.srcAmount.value():
            self.resultAmount.setValue(value / 30)
        else:
            self.srcAmount.setValue(self.resultAmount.value() * 30)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.onClickConvertBtn()


    def clearAmounts(self):

        self.resultAmount.setValue(0)
        self.srcAmount.setValue(0)
        self.changeBtn()


    def changeBtn(self):
        v1 = self.srcAmount.value()
        v2 = self.resultAmount.value()

        if (not v1 and not v2) or (v1 and v2):
            self.convertBtn.setEnabled(False)
        else:
            self.convertBtn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    c = Converter()
    c.show()

    sys.exit(app.exec_())
