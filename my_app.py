from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from inst import *
from Test_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        wn=QWidget()
        wn.setWindowTitle(txt_title)
        wn.resize(win_width,win_height)
        wn.move(win_x,win_y)
    def initUI(self):
        self.text=QLabel(txt_hello)
        self.instruction=QLabel(txt_instruction)
        self.button=QPushButton(txt_next)
        self.layout=QVBoxLayout() 
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button,alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def next_click(self):
        self.tw=TestWin()
        self.hide()
    def connects(self):
        self.button.clicked.connect(self.next_click)



app=QApplication([])
mw=MainWin()
app.exec_()

