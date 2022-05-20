from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    countNumber = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainWindow")
        self.move(400,400)
        self.resize(720,576)
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Файл",self)
        self.btn.clicked.connect(self.save)
        self.btn.move(50,50)
        self.btn.resize(50,30)
        self.exel = QTableWidget(self)
        self.exel.setRowCount(10)
        self.exel.setColumnCount(3)
        self.exel.move(100,100)
        self.exel.resize(405,402)





    def save(self):
        self.btnSave = QPushButton("Сохранить",self)
        self.btnSave.move(100,50)
        self.btn.resize(50,30)
        self.btnSave.show()

        self.btnSaveHow = QPushButton("Сохранить как",self)
        self.btnSaveHow.move(100,80)
        self.btnSaveHow.resize(100,30)
        self.btnSaveHow.show()

        self.OpenFile = QPushButton("Открыть файл",self)
        self.OpenFile.move(100,20)
        self.OpenFile.resize(100,30)
        self.OpenFile.show()

        self.btn.clicked.close()




if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
