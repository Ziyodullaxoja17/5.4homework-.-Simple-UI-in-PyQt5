from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QIcon
from kompanents import Label , Button
from os import system
system("cls")


class Main_Window(QWidget):
     def __init__(self):
          super().__init__()

          self.setWindowTitle("Uz_Chat")
          self.setWindowIcon(QIcon("download.jpg"))
          self.resize(480 , 640 )

          self.sarlavha=Label("Xush Kelibsiz !",130, 100 , self)

          self.tizimga_kirish_btn=Button("Tizimga Kirish" , 300 , self , 270 , 60)

          self.registratisiya_btn=Button("Ro'yxatdan O'tish" , 400 , self , 270 , 60 )
     











