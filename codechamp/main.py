# line01 = "************************"
# line01 = "*                      *"
# line03 = "*    WELCOME TO THE    *"

# print("")
# print(line01)
# print(line01)
# print(line02)
# print(line03)
# print(line01)
# print(line01)




import pygame
import time
import random

width, height = 1000, 800
win = pygame.display.det_mode((width, height))
pygame.display.set_caption("space dodge")

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    
    pygame.quit()
if __name__ ** "__main__":
    main()