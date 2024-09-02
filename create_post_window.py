from PyQt5.QtWidgets import QWidget 
from PyQt5.QtGui import QIcon 
from kompanents import Button , Label , Text_Area 
from os import system 
system("cls")


class New_Post(QWidget):
     def __init__(self):
          super().__init__()
          self.setWindowIcon(QIcon("download.jpg"))
          self.resize(480  , 640 )
          self.setWindowTitle("Share_Post")
          self.create_post_label=Label("Create Post" , 130 , 50 , self)

          self.post_area=Text_Area (self , 100 , 380 , 350 , "Craate New Post"  )

          self.save_new_post_btn=Button("Save" , 500 , self  , 100 , 50 )
          self.return_post_window_btn=Button("Back" , 580 , self , 100 , 50 )













