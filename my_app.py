from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from inst import *
app=QApplication([])
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        wn=QWidget()
        wn.setWindowTitle(titel)
        wn.resize(win_width,win_height)
        wn.move(win_x,win_y)
    def initUI(self):
        self.text=QLabel(label1)
        self.instruction=QLabel(label2)
        self.button=QPushButton(button)
        self.layout=QVBoxLayout 
        self.text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWidget(self.layout,alignment=Qt.AlignCenter)

    def  connects(self):
        
  
