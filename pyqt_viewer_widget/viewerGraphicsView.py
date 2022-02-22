from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt, pyqtSignal, QPoint, QRect
from pyqt_fitting_graphics_view.fittingGraphicsView import FittingGraphicsView


class ViewerGraphicsView(FittingGraphicsView):
    photoClicked = pyqtSignal(QPoint)
    rectChanged = pyqtSignal(QRect)

    def __init__(self):
        super().__init__()
        self.__filenames = []

    def setFilenames(self, filenames):
        self.__filenames = filenames

    def setIndex(self, index):
        self.setFilename(self.__filenames[index])