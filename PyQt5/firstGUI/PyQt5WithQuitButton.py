import sys
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setGeometry(300,300,350,350)
        self.setWindowTitle('Presss Button To Close')
        quit=QPushButton('Close',self)
        quit.setGeometry(10,10,60,35)
        quit.setStyleSheet('backgroud-color:red')
        quit.clicked.connect(self.close)

if __name__=='__main__':
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())
    
