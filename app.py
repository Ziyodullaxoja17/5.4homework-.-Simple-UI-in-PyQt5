from PyQt5.QtWidgets import QApplication, QMessageBox
import json
from os import system

system("cls")

from main_window import Main_Window
from login_window import Login_Window
from register_widow import Register_Window  
from posts_window import Post_Page
from  create_post_window import New_Post
from posts_history_window import Post_history



class App:
    def __init__(self):
        
        self.bosh_oyna = Main_Window()
        self.tizimga_kirish_oyna = Login_Window()
        self.register_oyna = Register_Window()  
        self.post_window = Post_Page()
        self.create_new_post_oyna=New_Post()
        self.post_history_oyna=Post_history()
      

        self.bosh_oyna.tizimga_kirish_btn.clicked.connect(self.tizimga_kirish_func)
        self.bosh_oyna.registratisiya_btn.clicked.connect(self.registratsiya_func)  

        self.bosh_oyna.show()

    def tizimga_kirish_func(self):
        self.tizimga_kirish_oyna.show()
        self.bosh_oyna.close()
        self.tizimga_kirish_oyna.tasdiqlash_btn.clicked.connect(self.tekshiruv)
        self.tizimga_kirish_oyna.back_main_window_from_login_window_btn.clicked.connect(self.return_main_window_from_login_window)

    def return_main_window_from_login_window(self):
        self.bosh_oyna.show()
        self.tizimga_kirish_oyna.close()     

    def tekshiruv(self):
    
        username = self.tizimga_kirish_oyna.username_input.text().strip()
        parol = self.tizimga_kirish_oyna.parol_input.text().strip()
        
       
        with open("data_password.json", 'r') as file:
            get_data = json.load(file)

       
        for user in get_data:
            if user["username"] == username and user["parol"] == parol:
                self.post_window.show()
                self.tizimga_kirish_oyna.close()
                return 

        self.msg_box = QMessageBox(self.tizimga_kirish_oyna)
        self.msg_box.setText("Parol yoki username mos emas")
        self.msg_box.exec()

    def registratsiya_func(self):
        self.register_oyna.show()
        self.bosh_oyna.close()
        self.register_oyna.save_btn.clicked.connect(self.malumot_saqlash)
        self.register_oyna.back_main_window_from_register.clicked.connect(self.return_main_window_from_register_window)


    def return_main_window_from_register_window(self):
        self.bosh_oyna.show()
        self.register_oyna.close()
       

    def malumot_saqlash(self):
        familiya = self.register_oyna.familiya_input.text().strip()
        ism = self.register_oyna.ism_input.text().strip()
        username = self.register_oyna.username_input.text().strip()
        parol = self.register_oyna.password_input.text().strip()

        info_user = {
            "familiya": familiya,
            "ism": ism,
            "username": username,
            "parol": parol
        }

        info_user_password = {
            "username": username,
            "parol": parol
        }

        try:
            with open("data_users.json", "r") as file:
                data_users = json.load(file)
        except FileNotFoundError:
            data_users = []

        try:
            with open("data_password.json", "r") as files:
                data_passwords = json.load(files)
        except FileNotFoundError:
            data_passwords = []

        for old_username in data_passwords:
            if old_username["username"] == username:
                self.msg_box = QMessageBox(self.register_oyna)
                self.msg_box.setText("Iltimos boshqa username kiriting")
                self.msg_box.exec()
                return

        if info_user["familiya"] and info_user["ism"] and info_user["username"] and info_user["parol"]:
            data_users.append(info_user)
            with open("data_users.json", "w") as file:
                json.dump(data_users, file, indent=4)
            print("Ma'lumot saqlandi")

            data_passwords.append(info_user_password)
            with open("data_password.json", "w") as files:
                json.dump(data_passwords, files, indent=4)

            
            self.register_oyna.ism_input.clear()
            self.register_oyna.familiya_input.clear()
            self.register_oyna.username_input.clear()
            self.register_oyna.password_input.clear()
            self.post_window.show()
            self.register_oyna.close()
            self.post_window.create_post_btn.clicked.connect(self.post_create_func)
            self.post_window.post_history_btn.clicked.connect(self.post_history_func)

        else:
            self.msg_box = QMessageBox(self.register_oyna)
            self.msg_box.setText("Iltimos ma'lumotlarni to'liq kiriting")
            self.msg_box.setInformativeText("Sizdan barcha ma'lumotlar talab qilinadi")
            self.msg_box.exec()

    def post_create_func(self):
        self.create_new_post_oyna.show()
        self.post_window.close()
        self.create_new_post_oyna.save_new_post_btn.clicked.connect(self.save_new_post_func)
        self.create_new_post_oyna.return_post_window_btn.clicked.connect(self.return_post_window_func)

       
    def post_history_func(self):
        self.post_history_oyna.show()
        self.post_window.close()
        

        self.post_history_oyna.return_post_window_from_history_btn.clicked.connect(self.return_posr_window_from_history_window_func)
            
    

    def return_posr_window_from_history_window_func(self):
        self.post_window.show()
        self.post_history_oyna.close()



    def save_new_post_func(self):
        info_new_post=self.create_new_post_oyna.post_area.toPlainText()

        try :
            with open("post_history.json" , 'r') as file:
                data_post=json.load(file)
        
        except FileNotFoundError :
            data_post=[]
        

        data_post.append(info_new_post)


        with open("post_history.json" , 'w'  ) as file :
            json.dump(data_post , file , indent=4)
            print("Yangi post saqlandi ")


        self.create_new_post_oyna.post_area.clear()

        

    def return_post_window_func(self):
        self.post_window.show()
        self.create_new_post_oyna.close()


app = QApplication([])
main = App()
app.exec()
