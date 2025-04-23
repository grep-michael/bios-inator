from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontMetrics,QPixmap
from Views.ResultsView.ResultsListView import ResultsListView
# stores list and current qr code
import segno 

#results view will consist of the results list and the currentQRcode

class ResultsView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)

    def clear_layout(self):
        while self.hbox.count():
            item = self.hbox.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def add_result_list(self,result_list:ResultsListView):
        self.hbox.addWidget(result_list)
        self.adjustSize()
    
    def add_current_qr_code(self,current_qr):
        self.hbox.addWidget(current_qr)
        self.adjustSize()
