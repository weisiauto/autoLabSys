import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from firstGUI import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButtonCalTax.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = int(self.textEditPriceBox.toPlainText())
        tax = (self.spinBoxTaxRate.value())
        total_price = price  + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.textEditResult.setText(total_price_string)

if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
