from PyQt5.QtCore import QObject,pyqtSignal
from Services.KeygenAPI import ApiClient
from Services.ResultModel import Result

from Views.QueryView import QueryView

class QueryController(QObject):

    signal_query_result = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.api_client = ApiClient()
    
    def connect_view(self,view:QueryView):
        self.view = view
        self.view.controls.submit_button.clicked.connect(self.handle_model_search)
    
    def handle_model_search(self):
        model = self.view.get_search_bar_text()
        results = self.api_client.get_solutions_for_model(model)
        self.signal_query_result.emit(results)
