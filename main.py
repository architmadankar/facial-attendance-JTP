import os
from modules.db import engine
from modules.lib.train import ClassificationTrain
from modules.settings import CAMERA_SOURCE
from modules.lib.utils import AppUtils

def title():
    t="Facial Attendance"
    print(t)
    
def menu():
    title()
    print("Use Numbers For Input")
    print("[0] Check Video Src")
    print("[1] Face")
    print("[2] Train")
    print("[3] Mark Attendance")
    print("[4] Quit")
    
    while True:
        face = AppUtils(CAMERA_SOURCE)
        choice =0
        try:
            choice = int(input("ENTER INT OF ABOVE COMMANDS: "))
            if choice ==0:
                face.chk()
                break
        except: ValueError
        
        finally:
            if choice == 0:
                print("Invalid Choice. Enter 1-5")
            elif choice == 5:
                exit()
            else:
                menu()
                
                
if __name__ == "__main__":
    menu()
    