from multiprocessing import Process
from time import sleep
import win32api,requests,win32con
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage

def get_imagi_contant(url):
    return requests.get(url).content

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 350)

        url_image = 'https://media.tenor.com/images/860b45652ebdaade6526e2ecde84bf88/tenor.png'
        image = QImage()
        image.loadFromData(get_imagi_contant(url_image))

        bg_url = "https://th.bing.com/th/id/OIP.W5DTyrTJPMH0ez0xgHoPmQHaEc?pid=ImgDet&rs=1"
        bg = QImage()
        bg.loadFromData(get_imagi_contant(bg_url))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 441, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(bg))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.StartB = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.StartB_func())
        self.StartB.setGeometry(QtCore.QRect(80, 300, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StartB.setFont(font)
        self.StartB.setCheckable(True)
        self.StartB.setObjectName("StartB")
        self.StatusL = QtWidgets.QLabel(self.centralwidget)
        self.StatusL.setGeometry(QtCore.QRect(81, 280, 121, 16))
        self.StatusL.setObjectName("StatusL")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 221, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(image))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(8, 25, 231, 21))
        self.label_4.setObjectName("label_4")
        self.Recoil = QtWidgets.QSpinBox(self.centralwidget)
        self.Recoil.setGeometry(QtCore.QRect(20, 301, 41, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Recoil.setFont(font)
        self.Recoil.setMinimum(1)
        self.Recoil.setMaximum(10)
        self.Recoil.setObjectName("Recoil")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Control = True

    def Move(self):
        try:
            sleep(0.06)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int(self.Recoil.text()))
        except Exception:
            exit(-1)

    def Check(self):
        while True:
            QtCore.QCoreApplication.processEvents()
            try:
                self.a = win32api.GetKeyState(0x01)
                if self.a == -128:
                    # pressed
                    self.Move()
                elif self.a == -127:
                    # pressed
                    self.Move()
                elif self.Control == False:
                    break
            except Exception:
                exit(-1)


    def StartB_func(self):
        if self.StartB.isChecked():
            self.Control = True
            self.StatusL.setStyleSheet("color:#38a739;")
            self.StartB.setStyleSheet("color:#38a739;")
            self.StatusL.setText("Status : ON")

            processlist = []
            processlist.append(Process(target=self.Check()))
            processlist.append(Process(target=self.Move()))
            for t in processlist:
                t.start()
            for t in processlist:
                t.join()


        elif not self.StartB.isChecked():
            self.Control = False
            self.StatusL.setStyleSheet("color:#ff0000;")
            self.StartB.setStyleSheet("color:#ff0000;")
            self.StatusL.setText("Status : OFF")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("#LR")
        MainWindow.setMaximumSize(241,350)
        self.StartB.setText(_translate("MainWindow", "ON/OFF"))
        self.StatusL.setText(_translate("MainWindow", '<html><head/><body><p><span style=" color:#FFFFFF;">Status : </span></p></body></html>'))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#5500ff;\"># Less Recoil By @kraken.exe</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
