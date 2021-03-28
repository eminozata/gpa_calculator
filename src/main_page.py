from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from second_page import SecondPage
from third_page import ThirdPage



class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("main_page.ui", self)

        self.hesaplaButton.clicked.connect(self.open_second_page)
        self.cizButton.clicked.connect(self.open_third_page)


        self.second_page = SecondPage()
        self.third_page = ThirdPage()




    def open_second_page(self):

        harf2puan ={
            "AA": 4.,
            "BA": 3.5,
            "BB": 3.,
            "CB": 2.5,
            "CC": 2.,
            "DC": 1.5,
            "DD": 1.,
            "VF/FF": 0.,
        }

        eski_ortalama = float(self.eski_ortalama.text())
        kredi_toplam = float(self.eski_kredi_toplam.text())
        toplam_puan = eski_ortalama * kredi_toplam
        ortalama = eski_ortalama

        if self.aktif_checker_9.isChecked():

            kredi_9 = float(self.kredi_sayisi_9.currentText())
            not_9 = harf2puan[self.alinan_harf_notu_9.currentText()]
            yeni_puan_9 = kredi_9 * not_9

            if self.tekrar_checker_9.isChecked():
                kredi_toplam += 0
                eski_not_9 = harf2puan[self.eski_harf_notu_9.currentText()]
                eski_puan_9 = kredi_9 * eski_not_9
                toplam_puan = toplam_puan - eski_puan_9 + yeni_puan_9
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_9
                toplam_puan = toplam_puan + yeni_puan_9
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_10.isChecked():

            kredi_10 = float(self.kredi_sayisi_10.currentText())
            not_10 = harf10puan[self.alinan_harf_notu_10.currentText()]
            yeni_puan_10 = kredi_10 * not_10

            if self.tekrar_checker_10.isChecked():
                kredi_toplam += 0
                eski_not_10 = harf10puan[self.eski_harf_notu_10.currentText()]
                eski_puan_10 = kredi_10 * eski_not_10
                toplam_puan = toplam_puan - eski_puan_10 + yeni_puan_10
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_10
                toplam_puan = toplam_puan + yeni_puan_10
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_11.isChecked():

            kredi_11 = float(self.kredi_sayisi_11.currentText())
            not_11 = harf2puan[self.alinan_harf_notu_11.currentText()]
            yeni_puan_11 = kredi_11 * not_11

            if self.tekrar_checker_11.isChecked():
                kredi_toplam += 0
                eski_not_11 = harf2puan[self.eski_harf_notu_11.currentText()]
                eski_puan_11 = kredi_11 * eski_not_11
                toplam_puan = toplam_puan - eski_puan_11 + yeni_puan_11
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_11
                toplam_puan = toplam_puan + yeni_puan_11
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_12.isChecked():

            kredi_12 = float(self.kredi_sayisi_12.currentText())
            not_12 = harf2puan[self.alinan_harf_notu_12.currentText()]
            yeni_puan_12 = kredi_12 * not_12

            if self.tekrar_checker_12.isChecked():
                kredi_toplam += 0
                eski_not_12 = harf2puan[self.eski_harf_notu_12.currentText()]
                eski_puan_12 = kredi_12 * eski_not_12
                toplam_puan = toplam_puan - eski_puan_12 + yeni_puan_12
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_12
                toplam_puan = toplam_puan + yeni_puan_12
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_13.isChecked():

            kredi_13 = float(self.kredi_sayisi_13.currentText())
            not_13 = harf2puan[self.alinan_harf_notu_13.currentText()]
            yeni_puan_13 = kredi_13 * not_13

            if self.tekrar_checker_13.isChecked():
                kredi_toplam += 0
                eski_not_13 = harf2puan[self.eski_harf_notu_13.currentText()]
                eski_puan_13 = kredi_13 * eski_not_13
                toplam_puan = toplam_puan - eski_puan_13 + yeni_puan_13
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_13
                toplam_puan = toplam_puan + yeni_puan_13
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_14.isChecked():

            kredi_14 = float(self.kredi_sayisi_14.currentText())
            not_14 = harf2puan[self.alinan_harf_notu_14.currentText()]
            yeni_puan_14 = kredi_14 * not_14

            if self.tekrar_checker_14.isChecked():
                kredi_toplam += 0
                eski_not_14 = harf2puan[self.eski_harf_notu_14.currentText()]
                eski_puan_14 = kredi_14 * eski_not_14
                toplam_puan = toplam_puan - eski_puan_14 + yeni_puan_14
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_14
                toplam_puan = toplam_puan + yeni_puan_14
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_15.isChecked():

            kredi_15 = float(self.kredi_sayisi_15.currentText())
            not_15 = harf2puan[self.alinan_harf_notu_15.currentText()]
            yeni_puan_15 = kredi_15 * not_15

            if self.tekrar_checker_15.isChecked():
                kredi_toplam += 0
                eski_not_15 = harf2puan[self.eski_harf_notu_15.currentText()]
                eski_puan_15 = kredi_15 * eski_not_15
                toplam_puan = toplam_puan - eski_puan_15 + yeni_puan_15
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_15
                toplam_puan = toplam_puan + yeni_puan_15
                ortalama = toplam_puan / kredi_toplam
        if self.aktif_checker_16.isChecked():

            kredi_16 = float(self.kredi_sayisi_16.currentText())
            not_16 = harf2puan[self.alinan_harf_notu_16.currentText()]
            yeni_puan_16 = kredi_16 * not_16

            if self.tekrar_checker_16.isChecked():
                kredi_toplam += 0
                eski_not_16 = harf2puan[self.eski_harf_notu_16.currentText()]
                eski_puan_16 = kredi_16 * eski_not_16
                toplam_puan = toplam_puan - eski_puan_16 + yeni_puan_16
                ortalama = toplam_puan / kredi_toplam
            else:
                kredi_toplam += kredi_16
                toplam_puan = toplam_puan + yeni_puan_16
                ortalama = toplam_puan / kredi_toplam


        self.second_page.display_gpa(str("{:.2f}".format(ortalama)))
        self.second_page.show()



    def open_third_page(self):
        self.third_page.show()





