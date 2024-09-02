from PyQt5.QtWidgets import  QWidget 
from kompanents import Label , Button , ListWidgetWithTextArea 
from os import system
from PyQt5.QtGui import QIcon 
system("cls")

class Post_history(QWidget):
     def __init__(self):
          super().__init__()

          self.setWindowTitle("History Posts")
          self.setWindowIcon(QIcon("download.jpg"))
          self.resize(480 , 640 )
          self.history_label=Label("Ulashilgan postlar ro'yxati " , 40 , 50 , self)
          self.post_list_widget=ListWidgetWithTextArea(self)
          self.return_post_window_from_history_btn=Button("Back" , 500 , self ,100 , 50 )






