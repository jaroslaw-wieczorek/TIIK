from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget


from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPlainTextEdit

from PyQt5.QtWidgets import QLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtGui import QIcon

from pathlib import Path
import os
import sys


PROJECT_DIR = Path(__file__).parents[2]
sys.path.append(PROJECT_DIR)

from project.src.utils.entropy import H

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

        self.read_path = ''
        self.save_path = ''
        
    def initUI(self):

        wid = QWidget(self)
        self.setCentralWidget(wid)

        #self.textEdit = QTextEdit()
        #self.setCentralWidget(self.textEdit)
        self.statusBar()

        self.text_input = QTextEdit("")
        self.text_output = QTextEdit("")

        self.entropy_btn = QPushButton("Entropy")


        self.save_file_btn = QPushButton("Save file")
        self.select_file_btn = QPushButton("Select file")


        self.select_file_btn.clicked.connect(self.selectFile)
        self.save_file_btn.clicked.connect(self.saveFile)
        self.entropy_btn.clicked.connect(self.entropy)


        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.text_input)
        self.vbox.addWidget(self.text_output)
        self.vbox.addWidget(self.entropy_btn)
        self.vbox.addStretch(1)

        self.vbox.addWidget(self.select_file_btn)
        self.vbox.addWidget(self.save_file_btn)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox)

        wid.setLayout(self.hbox)



        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        ##openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.selectFile)

        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openFile)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
        
    def selectFile(self):

        fname = QFileDialog.getOpenFileName(self, 'Select file', './')

        if fname[0]:
            # f = open(fname[0], 'r')

            # Return path on file
            self.read_path = fname[0]

            with open(self.read_path, 'r') as file:
                data = file.read()
                self.text_input.setPlainText(str(data))
            return fname[0]


    def saveFile(self):

        fname = QFileDialog.getSaveFileName(self, 'Save file', './')

        if fname[0]:
            self.save_path = fname[0]
            with open(self.save_path, 'w') as file:
                try:
                    file.write(str(self.text_output.toPlainText()))
                except Exception as err:
                    print(err)

            return fname[0]


    def entropy(self):
        text = self.text_input.toPlainText()

        stats = H(text)
        data = dict()

        for letter, value in stats[0].items():
            data[letter] = value

        self.text_output.setText(str(data))# ready_data[1]]))
        self.text_output.append("Entropy: " + str(stats[1]))

