from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar




class Graphic(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("graphic.ui", self)

    def display_graphic(self,liste):

        x_axis = []
        for i in range(1,len(liste)):
            x_axis.append(i)









