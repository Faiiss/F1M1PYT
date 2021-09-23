import datetime
import os

while True:
    print("Hello you! My name is Faissal\n")
    c = input("Who are you?\n")
    print(f"Hello,{c}. Today it is {datetime.datetime.now()}\n")

    if (input("Want to repeat?") == "Y" ):
        os.system('cls')
        continue
    else:
        break
input()