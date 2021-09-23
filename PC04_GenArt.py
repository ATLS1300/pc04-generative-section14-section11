# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:35:23 2021

@author: sasha

This is a piece of generative art that creates a random amount of 10-25 different 
colored squares, with the color selected from a pastel rainbow palette at random.
The squares therefore layer over each other at different places and create a unique
experience each time. 

# in my pseudocode they were supposed to be cubes but I changed it to squaresto make the 
loops simpler to achieve and I added more colors to make the image more interesting 
"""


import turtle,random #libraries     

stay = turtle.Turtle() #initialize turtle for stationery cubes
panel = turtle.Screen() #panel setup     
turtle.colormode(255)

panel.setup(600, 600) # panel size

stay.pencolor("BLACK") # pencolor + size for stationery squares
stay.pensize(5)

#draw square 1 in upper left corner

stay.up()
stay.goto(-280,150)
stay.down()

for i in range(4):
    stay.forward(100)
    stay.left(90)
  
#draw square 2 in lower right corner

stay.up()
stay.goto(180,-150)
stay.down()

for i in range(4):
    stay.forward(100)
    stay.left(90)
 
# begins the generative portion of the piece    
    
gen = turtle.Turtle() #initialize new turtle 
gen.pensize(5) #set pensize

#my color palette that I found using coolors.co

palette = [(255,173,173),(255,214,165),(252,255,182),(155,246,255),(160,196,255),(189,178,255)]

# I used hex colors, (FFADAD),(FFD6A5),(FDFFB6),(CAFFBF),(9BF6FF),(A0C4FF), and (BDB2FF)

for j in range(random.randint(10,25)): #will draw squares a random amount of times
    
    color = random.choice(palette) #chooses random color from palette above
    
    gen.up() # so the turtle isn't drawing until its time to make a square  
    
    gen.goto(random.randint(-280,280),random.randint(-280,280)) # goes to a random loc
  
    gen.down() #pen back down so turtle can draw a square
    
    for i in range(4): # draws said square
        gen.color(color) # sets the color to the random color chosen per square
        gen.forward(100)
        gen.left(90)
      

turtle.done() #stops the turtle



