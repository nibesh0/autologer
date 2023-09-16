import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PIL import Image
from ping3 import ping
from enc import enc
from req import req
import time

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
    status_code, check = req.req(Uid, passwd)
    if check == 0:
        print("success")
        return Uid
    elif check == -1:
        print("authentication failed")
        return -1
    elif check == -2:
        print("General failure:\n your data limit has been exhausted or multiple devices are using your user_id")
        return -1

def check_connection(ip_address, Uid):
    conn = ping(ip_address)
    if conn is not None:
        return f"Logged In as : {Uid}"
    else:
        return "Connection failed"

def check_connection_action(icon, ip_address, Uid):
    status = check_connection(ip_address, Uid)
    icon.setToolTip(status)

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    ip_address = '192.168.2.190'

    
    script_dir = os.path.dirname(os.path.abspath(__file__))

   
    image_path = os.path.join(script_dir, "res/image.jpeg")

    icon = QSystemTrayIcon()
    icon.setIcon(QIcon(image_path))  # Use the corrected absolute path
    menu = QMenu()
    initial_status = "Connecting in"

    check_action = QAction("Check Connection")
    check_action.triggered.connect(lambda: check_connection_action(icon, ip_address, Uid))  
    exit_action = QAction("Exit")
    exit_action.triggered.connect(app.quit)

    menu.addAction(check_action)
    menu.addAction(exit_action)

    icon.setContextMenu(menu)
    icon.show()
    icon.setToolTip(initial_status) 
    Uid = login(ip_address)

    initial_status = f"Logged In as : {Uid}"
    icon.setToolTip(initial_status) 
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
