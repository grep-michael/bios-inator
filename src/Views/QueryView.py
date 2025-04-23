from PyQt5.QtWidgets import *

class QueryView(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.controls = ControlLayout()
        self._layout = QVBoxLayout()
        
        self._layout.addLayout(self.controls)
        self.setLayout(self._layout)
    
    def get_search_bar_text(self):
        return self.controls.text_box.text()
    

class ControlLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.initLayout()
    
    def initLayout(self):
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("JS4QZW2-E7A8")
        self.submit_button = QPushButton("Generate Password")
        
        self.addWidget(self.text_box)
        self.addWidget(self.submit_button)
        