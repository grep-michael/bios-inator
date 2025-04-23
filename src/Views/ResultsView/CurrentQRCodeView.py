from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
#from Services.ResultModel import Password
class CurrentQRView(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.vbox = QVBoxLayout()

        self.header = QLabel("Current QR Code")
        self.vbox.addWidget(self.header)

        self.pixmap = QPixmap()
        self.pixmap_label = QLabel("QR Code Label")
        
        self.vbox.addWidget(self.pixmap_label)
        self.setLayout(self.vbox)
    
    def change_pixmap(self,qr_bytes:bytes):
        self.pixmap.loadFromData(qr_bytes)
        self.pixmap_label.setPixmap(self.pixmap)
