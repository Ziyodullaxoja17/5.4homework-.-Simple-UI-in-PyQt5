from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QListWidget, QVBoxLayout, QWidget, QTextEdit, QListWidgetItem

class Label(QLabel):
    def __init__(self, text, x, y, window):
        super().__init__(window)
        self.setText(text)
        self.move(x, y)
        self.setStyleSheet("""
        font-size: 35px;
        border-radius: 8px;
        """)

class Button(QPushButton):
    def __init__(self, text, y, window, a, b):
        super().__init__(window)
        self.resize(a, b)
        self.move((480 - a) // 2, y)
        self.setText(text)
        self.setStyleSheet("""
          background-color :#85e2e6;
          font-size : 30px;
          border-radius : 10px
""")       

class Input(QLineEdit):
    def __init__(self, text, y, window):
        super().__init__(window)
        self.resize(360, 60)
        self.setPlaceholderText(text)
        self.setStyleSheet("""
        font-size: 30px;
        border-radius: 8px;
        """)
        self.move(60, y)

class Text_Area(QTextEdit):
    def __init__(self, oyna, y, a, b, text):
        super().__init__(oyna)
        self.resize(a, b)
        self.move(50, y)
        self.setPlaceholderText(text)
        self.setStyleSheet("""
        font-size: 30px;
        border-radius: 7px;
        background-color: #cce3f0;
        """)

class ListWidgetWithTextArea(QListWidget):
    def __init__(self, oyna):
        super().__init__(oyna)
        self.setGeometry(50, 250, 380, 300)
        self.setStyleSheet("color: green;")

    def addTextAreaItem(self, text):
        widget = QWidget()
        layout = QVBoxLayout()
        text_edit = Text_Area(widget, 150, 380, 300, text)
        text_edit.setText(text)
        text_edit.setEnabled(False)
        layout.addWidget(text_edit)
        widget.setLayout(layout)
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)
