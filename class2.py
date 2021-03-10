import sys
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QGraphicsPixmapItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press me")
        self.setFixedSize(QSize(700,500))
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()