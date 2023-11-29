
import datetime
import time

def afficher_heure(heure, mode):
    if mode == "12h":
        current_time = heure.strftime("%I:%M:%S %p")
    elif mode == "24h":
        current_time = heure.strftime("%H:%M:%S")
    else:
        print("Mode d'affichage invalid")
        return
    
    print(current_time, end="\r")

def configurer_alarme(heure_alarme, mode):
    while True:
        heure_actuelle = datetime.datetime.now().time()
        if heure_actuelle.hour == heure_alarme[0] and heure_actuelle.minute == heure_alarme[1] and heure_actuelle.second == heure_alarme[2]:
            print("¡Alarme Activée!")
            break
        time.sleep(1)

def pause():
    global pause_horloge
    pause_horloge = True

def play():
    global pause_horloge
    pause_horloge = False

heure_actuelle = datetime.datetime.now().time()
mode_affichage = "12h" #mode d'affichage par defaut
afficher_heure(heure_actuelle, mode_affichage)
heure_alarme = (16, 17, 0)
configurer_alarme(heure_alarme, mode_affichage)

pause()
time.sleep(6)
play()