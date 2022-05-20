from PyQt5.QtWidgets import *
import sys

mainSize = 144
countRow = 7

widthWindow  = 5*mainSize
heightWindow = 4*mainSize

sideSize = heightWindow//(countRow + 5)
# Размеры----------------------------------------
heightTableTitle = sideSize*1
widthTableTitle  = widthWindow - sideSize*4

heightTableOutput = sideSize*(countRow)
widthTableOutput  = widthWindow - sideSize*4

heightTableInput = sideSize*1
widthTableInput  = widthWindow - sideSize*4
# Смещения----------------------------------------
horizontalMoveTableTitle =  sideSize*2
verticalMoveTableTitle =  sideSize*2

horizontalMoveTableOutput =  sideSize*2
verticalMoveTableOutput =  sideSize*3

horizontalMoveTableInput =  sideSize*2
verticalMoveTableInput =  sideSize*(3+countRow)
#-------------------------------------------------
class MainWindow(QMainWindow):
    countNumber = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainWindow")
        self.move(400,400)

        self.resize(widthWindow,heightWindow)
        self.initUI()

    def initUI(self):
        # Заголовок таблица
        self.tableTitle = QTableWidget(self)
        self.tableTitle.setColumnCount(3)
        self.tableTitle.setRowCount(1)
        self.tableTitle.resize(widthTableTitle,heightTableTitle)
        self.tableTitle.move(horizontalMoveTableTitle,verticalMoveTableTitle)
        # Таблица вывода
        self.tableOutput = QTableWidget(self)
        self.tableOutput.setColumnCount(3)
        self.tableOutput.setRowCount(countRow)
        self.tableOutput.resize(widthTableOutput,heightTableOutput)
        self.tableOutput.move(horizontalMoveTableOutput,verticalMoveTableOutput)
        # Таблица ввода
        self.tableInput = QTableWidget(self)
        self.tableInput.setColumnCount(3)
        self.tableInput.setRowCount(1)
        self.tableInput.resize(widthTableInput,heightTableInput)
        self.tableInput.move(horizontalMoveTableInput,verticalMoveTableInput)







    def save(self):
      pass

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







if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
