from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class MainMenu(QWidget):
    def __init__(self, parent_stacks):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("메인 메뉴"), alignment=Qt.AlignLeft | Qt.AlignTop)

        btn = QPushButton("랜덤 생성기")
        btn.clicked.connect(lambda: parent_stacks.setCurrentIndex(1))
        layout.addWidget(btn, alignment=Qt.AlignRight | Qt.AlignBottom)

        self.setLayout(layout)