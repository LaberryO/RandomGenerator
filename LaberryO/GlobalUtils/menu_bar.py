from PyQt5.QtWidgets import QMenuBar, QAction, QMessageBox

class AppMenu:
    def __init__(self, parent):
        self.parent = parent  # Main Window 인스턴스
        self.setup_menu()

    def setup_menu(self):
        # 1. 메뉴바 생성
        menubar = self.parent.menuBar()
        menubar.setNativeMenuBar(False) # OS(특히 Mac) 설정에 상관없이 윈도우 안에 메뉴 표시

        # 2. 상위 메뉴 만들기
        file_menu = menubar.addMenu("옵션")

        # 3. 액션(메뉴 항목) 추가
        exit_action = QAction("종료", self.parent)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.parent.close) # Main의 기능 사용

        file_menu.addSeparator() # 구분선
        file_menu.addAction(exit_action)