
import datetime
import time

def afficher_heure(heure):
    current_time = heure.strftime("%H:%M:%S")
    print(current_time, end="\r")

def configurer_alarme(heure_alarme):
    while True:
        heure_actuelle = datetime.datetime.now().time()
        if heure_actuelle.hour == heure_alarme[0] and heure_actuelle.minute == heure_alarme[1] and heure_actuelle.second == heure_alarme[2]:
            print("¡Alarme Activée!")
            break
        time.sleep(1)

heure_actuelle = datetime.datetime.now().time()
afficher_heure(heure_actuelle)
heure_alarme = (13, 52, 0)
configurer_alarme(heure_alarme)