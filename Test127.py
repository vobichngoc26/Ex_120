from PyQt6.QtWidgets import QApplication, QMainWindow
from Chapter6.Ex_127.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()