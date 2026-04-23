import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
import LaberryO.GlobalUtils
import LaberryO.Pages
# main loop
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("라베리의 유틸리티 프로그램")
        self.resize(800, 600)

        # global menu
        self.menu_manager = LaberryO.GlobalUtils.AppMenu(self)

        # stack widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # page
        self.main_menu = LaberryO.Pages.MainMenu(self.stack)
        self.rand_page = LaberryO.Pages.RandomGenerator(self.stack)

        # stack
        self.stack.addWidget(self.main_menu) # index 0
        self.stack.addWidget(self.rand_page) # index 1

        self.stack.setCurrentIndex(0)

        for btn in self.findChildren(QPushButton):
            btn.setCursor(Qt.PointingHandCursor)

def load_stylesheet(app):
    try:
        with open("LaberryO/style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("[ERROR] QSS File Not Found")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    load_stylesheet(app)

    window = Main()
    window.show()
    sys.exit(app.exec_())