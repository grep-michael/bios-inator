from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QRect,QCoreApplication,QObject
from PyQt5.QtGui import QFont,QResizeEvent
import sys
from MainWindow import MainWindow

FONT_FAMILY = "DejaVu Sans"
class Application(QApplication):

    def calculate_font_factor(self):
        """
        idk how this works but it does, kinda, what do i look like a computer scientist?
        """
        screen = QApplication.primaryScreen()
        width = screen.size().width()
        height = screen.size().height()

        dpi = screen.physicalDotsPerInch()
        print("dpi",dpi)
        dpi_factor = dpi/100
        print("dpi_factor",dpi_factor)
        resolution = width * height
        
        reference_resolution = 1920 * 1080

        scaling_factor = (resolution / reference_resolution) ** 0.5
        scaling_factor = (reference_resolution/resolution) #** 0.5
        print("scaling_factor", scaling_factor)

        min_scale = 0.5  # Won't go smaller than half base size
        max_scale = 3.0  # Won't go larger than 3x base size
        
        scaling_factor = max(min_scale, min(max_scale, scaling_factor))
        print("scaling_factor",scaling_factor)
        font_size = (12*dpi_factor)/scaling_factor
        print("calculated font size",font_size)

        return int(max(10,font_size)) #float font sizes dont work on windows ig

    def __init__(self):
        super().__init__(sys.argv)
        self.font_factor = self.calculate_font_factor()
        self._font = QFont(FONT_FAMILY)
        self._font.setPointSize(self.font_factor)  # Increase font size
        self.setFont(self._font)

        self.main_window = MainWindow()
        self.main_window.show()

    def run(self):
        try:
            self.exec()
        except Exception as e:
            print(e)