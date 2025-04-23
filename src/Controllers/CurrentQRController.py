from Views.ResultsView.CurrentQRCodeView import CurrentQRView
from PyQt5.QtCore import QObject
from Services.ResultModel import Result,Password
from resource_gather import get_resource

class CurrentQRController(QObject):
    def __init__(self):
        super().__init__()
    
    def connect_view(self,view:CurrentQRView):
        self.view = view
        self.load_stock_image()

    def load_stock_image(self):
        with open(get_resource("src/placeholder_1.jpeg"),"rb") as f:
            self.view.change_pixmap(f.read())
    
    def change_current_qr(self,password:Password):
        self.view.change_pixmap(password.get_bytes())
    