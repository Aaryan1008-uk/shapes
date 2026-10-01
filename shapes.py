import pgzrun

import pygame

import math

 

WIDTH = 500

HEIGHT = 500

 

def draw():

    screen.fill("skyblue")

 

    # Face

    screen.draw.filled_circle((250, 250), 150, "yellow")

 

    # Eyes

    screen.draw.filled_circle((200, 220), 20, "black")

    screen.draw.filled_circle((300, 220), 20, "black")

 

    # Smile

    pygame.draw.arc(

        screen.surface,

        "black",

        (175, 250, 150, 100),

        math.pi, 
        2 * math.pi,

        8

    )

 

pgzrun.go()