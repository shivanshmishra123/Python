import pygame # Pygame ko import kiya
pygame.init() #pygame ko initialise kiya
pygame.mixer.init() #Pygame ke mixer ko khola
sound = pygame.mixer.Sound("E:\\Shivansh.mp3") # Mixer mei apni desire file daali 
sound.play() #Play kiya
while pygame.mixer.get_busy():
    pygame.time.delay(100)