from PyQt5.QtWidgets import *
from Views.QueryView import QueryView
from Controllers.ResultController import ResultController
from Views.ResultsView.ResultView import ResultsView
from Controllers.QueryController import QueryController
from Views.QueryView import QueryView

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    
    def initUI(self):
        self.container = QWidget()
        self.vbox = QVBoxLayout()

        self.build_query()
        self.build_results()

        self.connect_query_to_results()

        self.container.setLayout(self.vbox)
        self.setCentralWidget(self.container)
    
    def connect_query_to_results(self):
        
        self.query_controller.signal_query_result.connect(self.results_controller.slot_query_results)

    def build_query(self):
        self.query_controller = QueryController()
        self.query_view = QueryView()
        self.query_controller.connect_view(self.query_view)

        self.vbox.addWidget(self.query_view)

    def build_results(self):
        self.results_controller = ResultController()
        self.results_view = ResultsView()
        self.results_controller.connect_view(self.results_view)
        self.vbox.addWidget(self.results_view)

    