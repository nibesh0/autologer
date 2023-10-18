import sys
import time
from PIL import Image
from ping3 import ping
from enc import enc
from req import req

def login(ip_address):
    conn = None
    while (conn is None or conn is False):
        time.sleep(1)
        try:
            conn = ping(ip_address)
            print(conn)
        except:
            print(conn)
    
    key_file = "C:/Program Files (x86)/AutoLoger/key/encryption_key.key"
    file = "C:/Program Files (x86)/AutoLoger/key/credentials.enc" 
    Uid, passwd = enc.retrieve_credentials(file, key_file)
    status_code, check = req(Uid, passwd)
    if check == 0:
        print("success")
        return Uid
    elif check == -1:
        print("authentication failed")
        return -1
    elif check == -2:
        print("General failure:\n your data limit has been exhausted or multiple devices are using your user_id")
        return -1

if __name__ == "__main__":
    ip_address = '192.168.2.190'
    Uid = login(ip_address)

    if Uid == -1:
        print("Connection failed")
    else:
        print(f"Logged In as : {Uid}")
