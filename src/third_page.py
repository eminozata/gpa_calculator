from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np



class ThirdPage(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("third_page.ui", self)


        self.ciz_button.clicked.connect(self.draw_graph)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))







    def draw_graph(self):
        donem_ortalamaları = []

        if self.donem_ort_check_1.isChecked():
            donem_ortalamaları.append(self.donem_ort_1.value())

        if self.donem_ort_check_2.isChecked():
            donem_ortalamaları.append(self.donem_ort_2.value())

        if self.donem_ort_check_3.isChecked():
            donem_ortalamaları.append(self.donem_ort_3.value())

        if self.donem_ort_check_4.isChecked():
            donem_ortalamaları.append(self.donem_ort_4.value())

        if self.donem_ort_check_5.isChecked():
            donem_ortalamaları.append(self.donem_ort_5.value())

        if self.donem_ort_check_6.isChecked():
            donem_ortalamaları.append(self.donem_ort_6.value())

        if self.donem_ort_check_7.isChecked():
            donem_ortalamaları.append(self.donem_ort_7.value())

        if self.donem_ort_check_8.isChecked():
            donem_ortalamaları.append(self.donem_ort_8.value())

        if self.donem_ort_check_9.isChecked():
            donem_ortalamaları.append(self.donem_ort_9.value())

        if self.donem_ort_check_10.isChecked():
            donem_ortalamaları.append(self.donem_ort_10.value())

        if self.donem_ort_check_11.isChecked():
            donem_ortalamaları.append(self.donem_ort_11.value())

        if self.donem_ort_check_12.isChecked():
            donem_ortalamaları.append(self.donem_ort_12.value())

        if self.donem_ort_check_13.isChecked():
            donem_ortalamaları.append(self.donem_ort_13.value())

        if self.donem_ort_check_14.isChecked():
            donem_ortalamaları.append(self.donem_ort_14.value())

        if self.donem_ort_check_15.isChecked():
            donem_ortalamaları.append(self.donem_ort_15.value())

        arr_don_ort = np.array(donem_ortalamaları)
        x_axis = np.arange(arr_don_ort.size)



        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(x_axis, arr_don_ort)
        self.MplWidget.canvas.draw()













