from PyQt5.QtWidgets import QWidget 
from os import system 
from PyQt5.QtGui import QIcon 
from kompanents import Button  , Label , ListWidgetWithTextArea




class Post_Page(QWidget):
     def __init__(self):
          super().__init__()


          self.resize(480 , 640 )
          self.setWindowTitle("Postlar")
          self.setWindowIcon(QIcon("download.jpg"))
          self.postlar_label=Label("Postlar" , 190 , 20 , self)

          self.create_post_btn=Button("Yangi Post" , 80 , self, 180 , 60 )
          self.post_history_btn=Button("Postlarim" , 160 , self , 180 , 60)
          self.post_area=ListWidgetWithTextArea(self)



          





