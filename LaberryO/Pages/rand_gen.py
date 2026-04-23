from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class RandomGenerator(QWidget):
    def __init__(self, parent_stacks):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("랜덤 제조기"), alignment=Qt.AlignLeft | Qt.AlignTop)

        btn = QPushButton("메인으로 돌아가기")
        btn.clicked.connect(lambda: parent_stacks.setCurrentIndex(0))
        layout.addWidget(btn, alignment=Qt.AlignRight | Qt.AlignBottom)

        self.setLayout(layout)