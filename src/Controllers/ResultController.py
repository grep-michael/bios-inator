from Views.ResultsView.ResultView import ResultsView
from Views.ResultsView.ResultsListView import ResultsListView
from Controllers.ResultListController import ResultListController
from Controllers.CurrentQRController import CurrentQRController
from Views.ResultsView.CurrentQRCodeView import CurrentQRView
from Services.ResultModel import *
from PyQt5.QtCore import QObject,pyqtSlot


class ResultController(QObject):

    def __init__(self,result_list=[]):
        super().__init__()
        self.result_list = result_list
    
    def connect_view(self,view:ResultsView):
        self.view = view
        self.build_result_list()
        self.build_result_qr()
    
    @pyqtSlot(list)
    def slot_query_results(self,result_list:list[Result]):
        self.result_list = result_list
        self.view.clear_layout()

        self.build_result_list()
        self.build_result_qr()

    def build_result_list(self):
        self.result_list_controller = ResultListController(self.result_list)
        self.result_list_view = ResultsListView(self.view)
        self.result_list_controller.connect_view(self.result_list_view)
        self.view.add_result_list(self.result_list_view)
    
    def build_result_qr(self):
        self.result_qr_controller = CurrentQRController()
        self.result_qr_view = CurrentQRView(self.view)
        self.result_qr_controller.connect_view(self.result_qr_view)
        self.result_list_controller.current_qr_controller = self.result_qr_controller
        self.view.add_current_qr_code(self.result_qr_view)