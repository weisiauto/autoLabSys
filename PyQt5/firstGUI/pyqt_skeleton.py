import sys
from PyQt5 import QtCore,QtWidgets,uic

# qtCreatorFile=r'E:\Documents\Python\firstGUI\firstGUI.ui'

qtCreatorFile=r'firstGUI.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        #QtWidgets.QMainWindow.__init__(self)
        super(MyApp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonCalTax.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = int(self.ui.textEditPriceBox.toPlainText())
        tax = (self.ui.spinBoxTaxRate.value())
        total_price = price  + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.ui.textEditResult.setText(total_price_string)

    
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



