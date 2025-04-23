from PyQt5.QtCore import QObject 
from Views.ResultsView.ResultsListView import ResultsListView
from Services.ResultModel import Result,Password
from Controllers.CurrentQRController import CurrentQRController

class ResultListController(QObject):
    
    def __init__(self,result_list):
        super().__init__()
        self.result_list = result_list
        self.current_qr_controller:CurrentQRController

    def connect_view(self,view:ResultsListView):
        self.view = view
        self.view.result_list.currentItemChanged.connect(self.handle_result_list_change)
        for result in self.result_list:
            self.view.add_result(result)
    
    def handle_result_list_change(self,current:Password,previous:Password):
        if self.current_qr_controller:
            self.current_qr_controller.change_current_qr(current)
            self.view.parent().adjustSize()
        else:
            print("current_qr_controller not set")

