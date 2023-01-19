from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

width = 1150
height = 550


class MyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Notepad")
        self.setMouseTracking(True)
        self.setFixedSize(width, height)
        my_menu = QMenuBar(self)
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
                border-radius: 20px;
            }
            QMenu::item::selected
            {
                background-color: #e1e1e1;
                color: #000;
                padding:10;
            }
             """
        )
        my_menu.setObjectName("my_menu")
        file_menu = my_menu.addMenu("File")
        file_menu.setObjectName("file")
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
        exit_file = QAction("Exit", self)
        file_menu.addAction(new_file)
        file_menu.addAction(new_window_file)
        file_menu.addAction(open_file)
        file_menu.addAction(save_file)
        file_menu.addAction(save_as_file)
        file_menu.addAction(exit_file)
        exit_file.triggered.connect(self.exit)
        open_file.triggered.connect(self.open)
        save_file.triggered.connect(self.save)
        save_as_file.triggered.connect(self.save_as)
        edit_menu = my_menu.addMenu("Edit")
        undo_edit = QAction("Undo", self)
        edit_menu.addAction(undo_edit)
        undo_edit.setShortcut(QKeySequence('Ctrl+Z'))
        undo_edit.triggered.connect(self.undof)
        copy_edit = QAction("Copy", self)
        edit_menu.addAction(copy_edit)
        copy_edit.setShortcut(QKeySequence('Ctrl+C'))
        copy_edit.triggered.connect(self.copyf)
        paste_edit = QAction("Paste", self)
        edit_menu.addAction(paste_edit)
        paste_edit.setShortcut(QKeySequence('Ctrl+V'))
        paste_edit.triggered.connect(self.printf)
        cut_edit = QAction("Cut", self)
        edit_menu.addAction(cut_edit)
        cut_edit.setShortcut(QKeySequence('Ctrl+X'))
        cut_edit.triggered.connect(self.cutf)
        view_menu = my_menu.addMenu("View")
        fontfam = view_menu.addMenu("Font")
        timesnew = QAction("Times New Roman", self)
        timesnew.triggered.connect(self.times)
        fontfam.addAction(timesnew)
        arial = QAction("Arial", self)
        arial.triggered.connect(self.arial)
        fontfam.addAction(arial)
        zoom = view_menu.addMenu("Zoom")
        zoomin = QAction("Zoom In", self)
        zoomin.triggered.connect(self.zoomin)
        zoom.addAction(zoomin)
        zoomout = QAction("Zoom Out", self)
        zoomout.triggered.connect(self.zoomout)
        zoom.addAction(zoomout)
        status_bar = QAction("Status Bar", self)
        view_menu.addAction(status_bar)
        self.b = QPlainTextEdit(self)
        self.b.setStyleSheet("font-size:14px")
        self.b.textChanged.connect(self.textchanged)
        self.b.move(0, 40)
        self.b.resize(width, height + 50)
        self.statusBar = QStatusBar(self)
        self.statusBar.setStyleSheet("background-color:#EAF6F6;padding:8px")
        self.setStatusBar(self.statusBar)

    def zoomin(self):
        self.b.setStyleSheet("font-size:35px")

    def zoomout(self):
        self.b.setStyleSheet("font-size:14px")

    def times(self):
        self.b.setStyleSheet("font-family:Times New Roman")

    def arial(self):
        self.b.setStyleSheet("font-family:Arial")

    def cutf(self):
        QApplication.clipboard().setText(self.b.toPlainText())
        self.b.setPlainText("")

    def copyf(self):
        QApplication.clipboard().setText(self.b.toPlainText())

    def printf(self):
        self.b.setPlainText(self.b.toPlainText() + QApplication.clipboard().text())

    def undof(self):
        a = self.b.toPlainText()
        b = len(a) - 1
        c = a[:b]
        self.b.setPlainText(c)

    def textchanged(self):
        a = self.b.toPlainText()
        b = len(a)
        self.statusBar.showMessage("    No. of Words: " + str(b))

    def new_file_func(self):
        window.show()

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


app = QApplication([])
window = MyMainWindow()
window.setStyleSheet("background-color:#FFFFFF")
window.show()
app.setWindowIcon(QIcon("images/Notepad.png"))
new_window = MyMainWindow()
sys.exit(app.exec())
