from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from inst import *
from PyQt5.QtGui import *
class data():
    def __init__(self,age,test1,test2,test3):
        self.age=age
        self.t1=test1
        self.t2=test2
        self.t3=test3




class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        print('nnnnn')
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
        self.btn_next=QPushButton(txt_sendresults,self)
        self.btn_test1=QPushButton(txt_starttest1,self)
        self.btn_test2=QPushButton(txt_starttest2,self)
        self.btn_test3=QPushButton(txt_starttest3,self)



        self.text_name=QLabel(txt_name)
        self.text_age=QLabel(txt_age)
        self.text_test1=QLabel(txt_test1)
        self.text_test2=QLabel(txt_test2)
        self.text_test3=QLabel(txt_test3)
        self.text_timer=QLabel(txt_timer)
        self.text_timer.setFont(QFont("Time",36,QFont.Bold))



        self.line_name=QLineEdit(txt_hintname)
        self.line_age=QLineEdit(txt_hintage)
        self.line_test1=QLineEdit(txt_hinttest1)
        self.line_test2=QLineEdit(txt_hinttest2)
        self.line_test3=QLineEdit(txt_hinttest3)


        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line) 
        self.h_line.addLayout(self.r_line)       
        self.setLayout(self.h_line)

    def next_click(self):
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test1.clicked.connect(self.timer_sits)
        self.btn_test1.clicked.connect(self.timer_final)
    def timer_test(self):
        global time
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer2Event)
        #one squat in 1.5 seconds
        self.timer.start(15000)

    def timer_final(self):
        global time
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer3Event) 
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Time",36,QFont.Bold))
        self.text_timer.setStyleSheet("Color:rgb(255,55,88)")
        if time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])#cut hh:mm:ss show ss
        self.text_timer.setFont(QFont("Time",36,QFont.Bold))
        self.text_timer.setStyleSheet("Color:rgb(255,55,88)")
        if time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Time",36,QFont.Bold))
        self.text_timer.setStyleSheet("Color:rgb(255,55,88)")
        if time.toString("hh:mm:ss")=="00:00:45":
            self.text_timer.setStyleSheet("Color:rgb(80,0,150)") 
        if time.toString("hh:mm:ss")=="00:00:15":
            self.text_timer.setStyleSheet("Color:rgb(0,0,255)") 
        if time.toString("hh:mm:ss")=="00:00:00":
            self.text_timer.setStyleSheet("Color:rgb(80,190,80)") 
            self.timer.stop()