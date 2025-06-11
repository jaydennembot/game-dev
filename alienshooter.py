import pygame
import pgzrun
from random import randint

TITLE="Alien destroyers"
WIDTH=1500
HEIGHT=750
message=" "

fishy=Actor("jayden")
def draw():
    screen.clear()
    # screen.fill("lightblue")
    screen.blit("bg",(0,0))
    fishy.draw()
    screen.draw.text(message,center=(450,10),fontsize=30)

def place():
    fishy.y=randint(50,HEIGHT-50)
    fishy.x=randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if fishy.collidepoint(pos):
        message="super aim "
        place()
    else: 
        message="unlucky try again"

place()

pgzrun.go()
                    

                                                   
