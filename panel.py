#encoding=utf-8
import PyQt4.QtGui as Qg
import PyQt4.QtCore as Qc
import sys
import test


class Title(Qg.QWidget): # 题目类

    def __init__(self):
        super(Title,self).__init__()
        self.title = Qg.QLabel('Chinese Input',self)
        self.title.setFont(Qg.QFont("Times", 12, Qg.QFont.Bold))

class InputBox(Qg.QWidget): # 输入框类

    def __init__(self):
        super(InputBox,self).__init__()

        self.initInputBox()

    def initInputBox(self):
        #self.resize(50,50)
        self.inputBox = Qg.QLineEdit()
        grid = Qg.QGridLayout()
        grid.addWidget(self.inputBox,1,1)
        self.setLayout(grid)

    def keyPressEvent(self, event):
        # if type(event) == Qc.Qt.Key_Enter:
        #     print "aaaaaa"
        #     self.emit("APressed")
        #     event.accept()
        # else:
        #     event.ignore()
        if event.key() == Qc.Qt.Key_F1:
            self.emit("f1()")



class ShowBox(Qg.QWidget): # 显示框类

    def __init__(self):
        super(ShowBox,self).__init__()

        self.initShowBox()

    def initShowBox(self):
        #self.resize(50,50)
        self.showBox = Qg.QTextEdit(self)
        grid = Qg.QGridLayout()
        grid.addWidget(self.showBox)
        self.setLayout(grid)

class ChineseInput(Qg.QMainWindow):

    def __init__(self):
        super(ChineseInput,self).__init__()
        self.candinate = []
        self.candinateStr = ""
        self.timer = Qc.QTimer()
        self.initGUI()

    # def keyPressEvent(self, event):
    #     # if type(event) == Qc.Qt.Key_Enter:
    #     #     print "aaaaaa"
    #     #     self.emit("APressed")
    #     #     event.accept()
    #     # else:
    #     #     event.ignore()
    #     if event.key() == Qc.Qt.Key_Escape:
    #         self.close()

    def initGUI(self):

        self.resize(1000,500)
        self.setWindowTitle('Chinese Input')
        # self.setWindowIcon(Qg.QIcon("B.jpg"))
        self.center()

        self.title = Title()

        self.inputBox = InputBox()
        self.candinateBox = ShowBox()
        self.editBox = ShowBox()

        self.inputLabel = Qg.QLabel('input', self)
        self.candinateLabel = Qg.QLabel('Chinese', self)
        self.editorLabel = Qg.QLabel('Editor', self)

        self.createMainWidget()
        self.connectEvent()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = Qg.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createMainWidget(self):
        widget=Qg.QWidget()

        grid = Qg.QGridLayout(widget)
        grid.setSpacing(10)
        # grid.addWidget(self.title,1,3,2,1)
        # grid.addWidget(self.candinateBox, 2, 2, 7, 4)
        # grid.addWidget(self.inputBox, 9, 2, 3, 3)
        # grid.addWidget(self.editBox, 10, 5, 2, 1)
        #grid.addWidget(self.title,)

        grid.addWidget(self.inputLabel, )
        grid.addWidget(self.inputBox, )
        grid.addWidget(self.candinateLabel, )
        grid.addWidget(self.candinateBox,)
        grid.addWidget(self.editorLabel,)
        grid.addWidget(self.editBox,)
        widget.setLayout(grid)

        self.setCentralWidget(widget)


    def connectEvent(self):

        # 两种输入方式，一种是需要用户回车，一种定时刷新，后一种逻辑不完整
        self.connect(self.inputBox.inputBox, Qc.SIGNAL("returnPressed()"), self.updateUi)
        #self.connect(self.inputBox.inputBox, Qc.SIGNAL("f1()"), self.updateUi)

        #Qc.QTimer.connect(self.timer, Qc.SIGNAL("timeout()"),self.updateUi)
        #self.timer.start(2000) # 时钟频率，2000ms刷新一次

    def updateUi(self):
        pinyin = str(self.inputBox.inputBox.text())
        if pinyin.isdigit():
            if len(self.candinate) != 0:
                self.editBox.showBox.insertPlainText(self.candinate[int(pinyin)-1])
                self.candinate = []
            else:
                self.editBox.showBox.insertPlainText(str(pinyin))
            self.inputBox.inputBox.clear()
            self.candinateBox.showBox.clear()
        elif pinyin.islower():
            print 'a'
            chinese = test.pinyin2hanzi(pinyin)
            showCandinate = []
            self.candinate = []
            candinateStr = ""
            for index, word in enumerate(chinese):
                showCandinate.append(str(index + 1) + " " + word + "\n")
                self.candinate.append(word)
                candinateStr = "".join(showCandinate)
            self.candinateBox.showBox.setText(candinateStr)
            self.inputBox.inputBox.clear()
        else:
            self.editBox.showBox.insertPlainText(pinyin)
            self.inputBox.inputBox.clear()




app = Qg.QApplication(sys.argv)
mainWindow = ChineseInput()
app.exec_()
