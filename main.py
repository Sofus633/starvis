import pygame 
import time
import json

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

mainloop = True

class Star:
    def __init__(self, pos, name, color):
        self.position = (pos[0], pos[1])
        self.size = abs(pos[2])
        self.name = name
        self.color = (color["r"] * 50, color["g"]* 50, color["b"]* 50)
        
    def display(self):
        print(self.position,self.size ,self.name, )
        pygame.draw.circle(window, self.color, self.position, self.size)
        time.sleep(0.01)


def extractdatta():
    with open('bsc5p_3d.json') as f:
        data = json.load(f)
    return data

def getstarspos(data):
    starspos = []
    for star in data:
        print(star)
        k_value = star.get("K",{"r": 0.5,"g": 0.5,"b": 0.5})
        if star["x"] != None and star["y"]  != None and star["z"]!= None and star["x"]*10 < pygame.display.Info().current_w and star["x"]*10 > 0 and star["y"]*10 < pygame.display.Info().current_h and star["y"]*10 > 0 :
            starspos.append(Star([star["x"]*10, star["y"]*10, star["z"]], star["n"], k_value))
    return starspos

def displaystars(starspos):
    for star in starspos:
        star.display()
        pygame.display.flip()
    
        

starpositions = getstarspos(extractdatta())
print(pygame.display.Info().current_w)
displaystars(starpositions)
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                window.fill(0)
                displaystars(starpositions)
            
    time.sleep(1)