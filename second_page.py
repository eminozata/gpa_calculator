from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi



class SecondPage(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("second_page.ui", self)

    def display_gpa(self,text):
        self.ortalama_label.setText(text)







