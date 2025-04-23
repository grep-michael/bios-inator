from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontMetrics,QPixmap
from Services.ResultModel import Result,Password


class ResultsListView(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.result_list = QListWidget()
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.result_list)
        self.setLayout(self._layout)


    def add_result(self,result:Result):
        for password in result.passwords:
            self.result_list.addItem(password)
