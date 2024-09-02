from PyQt5.QtWidgets import QWidget 
from os import system 

from kompanents import Label , Input , Button 

from PyQt5.QtGui import QIcon 

system("cls")

class Login_Window(QWidget):
     def __init__(self):
          super().__init__()
          self.resize(480 , 640 )
          self.setWindowTitle("Tekshiruv")
          self.setWindowIcon(QIcon("download.jpg"))

          self.tizimga_kirish_label=Label("Tizimga Kirish" , 125 , 100 , self)
          self.username_input=Input("Username kiriting " , 220 , self)
          self.parol_input=Input("Parolni kiriting " , 300 , self)

          self.tasdiqlash_btn=Button("Kirish"  , 480 ,self ,  120 , 60 )
          self.back_main_window_from_login_window_btn=Button("Orqaga" , 560 , self ,120 , 60 )



     

          

          







