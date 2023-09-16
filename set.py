import sys
import os  
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PIL import Image
from ping3 import ping
from enc import enc
from req import req

def login(ip_address):
    conn = ping(ip_address)
    if conn is not None:
        key_file ="C:/Program Files (x86)/AutoLoger/key/encryption_key.key"
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
    else:
        print("General transmission failed")
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

    icon = QSystemTrayIcon()
    icon.setIcon(QIcon(os.path.abspath("res/image.jpeg")))  # Use absolute path

    Uid = login(ip_address)
    initial_status = f"Logged In as : {Uid}"
    icon.setToolTip(initial_status) 

    menu = QMenu()

    check_action = QAction("Check Connection")
    check_action.triggered.connect(lambda: check_connection_action(icon, ip_address, Uid))  
    exit_action = QAction("Exit")
    exit_action.triggered.connect(app.quit)

    menu.addAction(check_action)
    menu.addAction(exit_action)

    icon.setContextMenu(menu)
    icon.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
