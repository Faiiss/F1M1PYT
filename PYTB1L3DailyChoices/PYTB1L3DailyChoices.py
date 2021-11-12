import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.045)

delay_print("Hallo, ik ga je vijf keuzes geven.")
print("")
delay_print("Wat doe je na school? Gamen, Werken, slapen of tv kijken")
print("")
antwoord_1 = input(">>> ")

if antwoord_1 == "Gamen" :
    delay_print("Jij gaat dus meestal gamen, dat is lekker!")
    
elif antwoord_1 == "Werken" :
    delay_print("Jij gaat dus meestal werken, dat is goed!")

elif antwoord_1 == "Slapen" :
    delay_print("Jij gaat dus meestal slapen, dat is lekker!")

elif antwoord_1 == "Tv kijken" :
    delay_print("Jij gaat dus meestal tv kijken vet man!")

else:
    delay_print("Je hebt niet goed antwoord gegeven. Laten we naar de volgende vraag gaan!")

print("")
delay_print("dit was de vragenlijst, doei")

