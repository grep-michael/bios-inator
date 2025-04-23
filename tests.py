import sys,os
sys.path.insert(0, os.getcwd() + "/src/") #assuming you are running the script from inside the BIOS_PW_SCANNER folder


import unittest
from Services.KeygenAPI import ApiClient
from Services.ResultModel import Result
from Controllers.ResultController import ResultController
from Views.ResultsView.ResultView import ResultsView
from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, 
                         QMessageBox, QVBoxLayout)

class TestApiClient(unittest.TestCase):

    TEST_MODEL = "JS4QZW2-E7A8"

    def test_bios_pw(self):
        api = ApiClient()
        result_list = api.get_solutions_for_model(TestApiClient.TEST_MODEL)
        expected_list = [ Result('dellHDDOld',['sssss000']), Result('dellTag',['FLsUhh40BZr66N5D', 'GLMGs4[[mDMPGdnz'])]
        
        self.assertEqual(len(result_list),2)

        for index,result in enumerate(result_list):
            self.assertEqual(result.name,expected_list[index].name)
            self.assertEqual(result.passwords[0].get_text(),expected_list[index].passwords[0].get_text())

class TestResults(unittest.TestCase):

    def test(self):
        #idk how to test something with limited functionality
        a = Result("dellHDDOld",['sssss000'])
        self.assertEqual(len(a.passwords),1)

class testGui(unittest.TestCase):
    
    def test_gui(self):
        api = ApiClient()
        result_list = api.get_solutions_for_model(TestApiClient.TEST_MODEL)
        
        #app = QApplication(sys.argv)
        #controller = ResultController()
        #view = ResultsView()
        #controller.connect_view(view)
        #controller.change_result_list(result_list)
        #view.show()
        #app.exec_()

if __name__ == '__main__':
    unittest.main()
    