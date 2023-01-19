from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PyQt6.QtPrintSupport import QPrinter


width = 1150
height = 550


class MyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Notepad")
        self.setMouseTracking(True)
        self.setFixedSize(width, height)
        my_menu = QMenuBar(self)
        # self.shortcut_save = QShortcut(QKeySequence('Ctrl+S'), self)
        # self.shortcut_save.activated.connect(self.save)
        # self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        # self.shortcut_open.activated.connect(self.open)
        my_menu.setStyleSheet(
            """
            QMenuBar
            {
                spacing:10px;
                font-size:14px;
                padding:8px;
                background-color: #EAF6F6;
                color: #999;
            }
            QMenuBar::item
            {
                background-color: #EAF6F6;
                color: #000;
            }
            QMenuBar::item::selected
            {
                background-color: #e1e1e1;
                color: #000;
            }
            QMenu
            {
                background-color: #FFFFFF;
                color: #000;
                padding:10;

            }
            QMenu::item::selected
            {
                background-color: #e1e1e1;
                color: #000;
                padding:10;
            }
             """
        )
        # my_menu = self.menuBar()
        my_menu.setObjectName("my_menu")
        # my_menu.setStyleSheet("background-color:#EAF6F6")
        file_menu = my_menu.addMenu("File")
        file_menu.setObjectName("file")
        # file_menu.setStyleSheet("background-color:#FFFFFF;padding-top:10;")
        new_file = QAction("New", self)
        new_file.setShortcut(QKeySequence("Ctrl+N"))
        new_window_file = QAction("New Window", self)
        new_window_file.setShortcut(QKeySequence("Ctrl+Shift+N"))
        new_window_file.triggered.connect(self.new_file_func)
        new_file.triggered.connect(self.reset)
        open_file = QAction("Open", self)
        open_file.setShortcut(QKeySequence('Ctrl+O'))
        save_file = QAction("Save", self)
        save_file.setShortcut(QKeySequence('Ctrl+S'))
        save_as_file = QAction("Save as", self)
        save_as_file.setShortcut(QKeySequence('Ctrl+Shift+S'))
        print_file = QAction("Print", self)
        print_file.setShortcut(QKeySequence('Ctrl+P'))
        print_file.triggered.connect(self.printer)
        exit_file = QAction("Exit", self)
        file_menu.addAction(new_file)
        file_menu.addAction(new_window_file)
        file_menu.addAction(open_file)
        file_menu.addAction(save_file)
        file_menu.addAction(save_as_file)
        file_menu.addAction(print_file)
        file_menu.addAction(exit_file)
        exit_file.triggered.connect(self.exit)
        open_file.triggered.connect(self.open)
        save_file.triggered.connect(self.save)
        save_as_file.triggered.connect(self.save_as)
        edit_menu = my_menu.addMenu("Edit")
        view_menu = my_menu.addMenu("View")
        edit_menu.setObjectName("exit")
        # new.triggered.connect(self.test)
        self.b = QPlainTextEdit(self)
        self.b.move(0, 40)
        self.b.resize(width, height + 50)

    def printer(self):
        dialog = QPrinter()
        dialog.printProgram()
    def new_file_func(self):
        new_window.show()

    def reset(self):
        self.b.setPlainText("")

    def exit(self):
        sys.exit()

    def save(self):
        try:
            files_types = "Text Documents (*.txt)"
            text = QFileDialog.getSaveFileName(self, 'Save File', 'untitled.txt', filter=files_types)
            # text = QFileDialog.getSaveFileName(self, 'Save File',"","Text Documents(.txt)",)
            file = open(str(text[0]), 'w')
            data = self.b.toPlainText()
            with file:
                file.write(data)
        except:
            window.show()
        # text = QInputDialog.getText(self, 'Save File', 'Enter File name:')
        # output = str(text[0]) + '.txt'
        # data = self.b.toPlainText()
        # with open(output, 'w') as file_data:
        #     file_data.write(data)

    def save_as(self):
        text = QInputDialog.getText(self, 'Save File', 'Enter File name:')
        extension = QInputDialog.getText(self, 'Save File', 'Enter File type')
        output = str(text[0]) + "." + str(extension[0])
        data = self.b.toPlainText()
        if str(text[0]) or str(extension[0]) != "":
            with open(output, 'w') as file_data:
                file_data.write(data)

    def open(self):
        try:
            text = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(str(text[0]), 'r')
            with file:
                output = file.read()
                self.b.setPlainText(output)
        except:
            window.show()
        # text = QInputDialog.getText(self, 'Open File', 'Enter File name:')

        # file_path = "D:" + chr(92) + "Advance Programming Techniques" + chr(92) + "Programs" + chr(92) + str(
        #     text[0]) + '.txt'
        # if os.path.exists(file_path):
        #     with open(file_path, 'r') as file_data:
        #         output = file_data.read()
        #         self.b.setPlainText(output)
        # else:
        #     print("Path Doesnt Exist")
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        #
        # msg.setText("This is a message box")
        # msg.setInformativeText("This is additional information")
        # msg.setWindowTitle("MessageBox demo")
        # msg.setDetailedText("The details are as follows:")
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


app = QApplication([])
window = MyMainWindow()
window.setStyleSheet("background-color:#FFFFFF")
window.show()
app.setWindowIcon(QIcon("images/Notepad.png"))
new_window = MyMainWindow()
sys.exit(app.exec())
