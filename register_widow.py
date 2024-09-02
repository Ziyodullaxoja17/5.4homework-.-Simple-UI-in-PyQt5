from PyQt5.QtWidgets import QWidget  
from kompanents import Label , Input  , Button
from PyQt5.QtGui import QIcon
from os  import system 
system('cls')



class Register_Window(QWidget):
     def __init__(self):
          super().__init__()
          self.setWindowTitle("Registratisiya")
          self.resize(480 , 640 )
          self.setWindowIcon(QIcon("download"))


          self.register_Label=Label ("Registratsiya " , 140 , 60 , self )

          self.familiya_input=Input("Familiya kiriting " , 140 , self)
          
          self.ism_input=Input("Ism kiriting " , 220 , self)

          self.username_input=Input("Username kiriting " , 300 , self)

          self.password_input=Input("Parol yarating " , 380 , self)

          self.save_btn=Button("Tasdiqlash" , 500, self , 200 , 70 )
          self.back_main_window_from_register=Button("  Orqaga  " , 580 , self  , 200 ,70 )


