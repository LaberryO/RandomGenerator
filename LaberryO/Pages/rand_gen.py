from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class RandomGenerator(QWidget):
    def __init__(self, parent_stacks):
        super().__init__()
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        btn = QPushButton("메인 메뉴")
        btn.clicked.connect(lambda: parent_stacks.setCurrentIndex(0))
        button_layout.addWidget(btn, alignment=Qt.AlignLeft | Qt.AlignTop)
        
        btn = QPushButton("랜덤 생성기")
        btn.clicked.connect(lambda: parent_stacks.setCurrentIndex(1))
        btn.setObjectName("active")
        button_layout.addWidget(btn, alignment=Qt.AlignLeft | Qt.AlignTop)

        button_layout.addStretch(1)

        layout.addLayout(button_layout)
        layout.addWidget(QLabel("랜덤 생성기 페이지"))
        
        layout.addStretch(1)

        self.setLayout(layout)