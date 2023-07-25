import sys
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow

class GeckoEmbed(QMainWindow):
    firefoxWinId = 0
    windowTitle = ""
    windowPosX = 0
    windowPosY = 0
    windowWidth = 0
    windowHeight = 0
    
    def __init__(self, window_id, title, x, y, w, h):
        self.firefoxWinId = window_id
        self.windowTitle = title
        self.windowPosX = x
        self.windowPosY = y
        self.windowWidth = w
        self.windowHeight = h
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.windowTitle)
        self.setGeometry(self.windowPosX, self.windowPosY, self.windowWidth, self.windowHeight)

        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)

        window = QWindow.fromWinId(self.firefoxWinId)
        widget = QWidget.createWindowContainer(window)
        layout.addWidget(widget)

        self.setCentralWidget(main_widget)
        
def run_app(window_id, title, x, y, w, h, exitApp = True):
    app = QApplication(sys.argv)
    mainWindow = GeckoEmbed(window_id, title, x, y, w, h)
    mainWindow.show()
    if exitApp:
        sys.exit(app.exec_())