from modules.db import engine
from modules.lib.train import ClassificationTrain
from modules.settings import CAMERA_SOURCE
from modules.lib.utils import AppUtils
from modules.models import DBase
DBase.metadata.create_all(engine)

def title():
    t="Facial Attendance"
    print(t)
    
def menu():
    title()
    print("Use Numbers For Input")
    print("[1] Check Video Src")
    print("[2] Face")
    print("[3] Train")
    print("[4] Mark Attendance")
    print("[5] Quit")
    
    while True:
        face = AppUtils(CAMERA_SOURCE)
        choice = 0
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                face.chk()
                break
            elif choice == 2:
                face.check_n_snap()
                break
            elif choice == 3:
                ClassificationTrain.training()
                break
            elif choice == 4:
                face.rec_n_attendance()
                break
            elif choice == 5:
                print("Quitting...")
                break
            else:
                choice = 0
        except ValueError:
            print("Invalid Choice")
            choice = 0
        finally:
            if choice == 0:
                print("Invalid Choice Choose From 1-5")
            elif choice == 5:
                exit()
            else:
                menu()
                
if __name__ == "__main__":
    menu()
    