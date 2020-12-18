# After every 40 min --> Water
# After every 30 min --> Eye Exercise
#After every 45 min --> Physical Exercise

# Bhai bohut hi behatareen cheeze iss waale session mei pata chali hai ki pehle sab 
# functions bana lena chahiye wahi sahi rhta hai

import pygame # Pygame ko import kiya
import time

def music(filename,stop):
    pygame.init() #pygame ko initialise kiya
    pygame.mixer.init() #Pygame ke mixer ko khola
    sound = pygame.mixer.Sound(filename) # Mixer mei apni desire file daali 
    sound.play() #Play kiya
    while(True):
        userstopper = input("Type done when you have done the actvity")
        if userstopper == stop:
            sound.stop()
        break

def loginfile(msg):
    f = open(Shivansh_Water_Drank.txt)
    f.write(f"{msg}, {time.asctime()}\n")

init_water = time.time()
init_eye = time.time()
init_exercise = time.time()

watersecs = 40*60
execisesecs = 30*60
phy  = 45*60


while(True):
    if time.time() - init_water > watersecs:
        music("E:\\Shivansh.mp3","Drank")
        init_water = time.time()
        loginfile("Water drank at:")
    if time.time() - init_eye > execisesecs:
        music("E:\\Shivansh.mp3","Done")
        init_water = time.time()
        loginfile("Eye Exercise at:")
    if time.time() - init_exercise > phy:
        music("E:\\Shivansh.mp3","Done")
        init_water = time.time()
        loginfile("Physical Exercise at:")