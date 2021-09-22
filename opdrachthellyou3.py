print("Hell you! ik ben Faissal")

x = input("Wie ben jij?")
print ('Hello,' + x)

import datetime
import os
x = datetime.datetime.now()

print ("De datum van vandaag is:")
print (x)

while True:
if (input("Want to repeat?") == "Y" ):
    os.system('cls')
    continue
else:
    break
