import os
from modules.db import engine
from modules.lib.train import TrainClassifier
from modules.models import DBase
from modules.settings import VIDEO_SOURCE
from modules.lib.utils import AppUtils

DBase.metadata.create_all(engine)

def title_bar():

    title =("Attendance System")
    print(title)


def main():
    title_bar()
    print(10*"*", "WELCOME", 10*"*")
    print("[1] Check Test")
    print("[2] Make Face Dataset")
    print("[3] Model Training")
    print("[4] Mark Attendance")
    print("[5] Quit")

    while True:
        face_util = AppUtils(VIDEO_SOURCE)
        choice = 0
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                face_util.chk()
                break
            elif choice == 2:
                face_util.detect_cap()
                break
            elif choice == 3:
                TrainClassifier.train()
                break
            elif choice == 4:
                face_util.markAttendance()
                break
            elif choice == 5:
                print("Bye!")
            else:
                choice = 0
        except ValueError:
            choice = 0
        finally:
            if choice == 0:
                print("Invalid Choice. Enter 1-5")
            elif choice == 5:
                exit()
            else:
                main()
if __name__ == "__main__":
    main()
