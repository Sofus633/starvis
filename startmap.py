import pygame 
import time
import json

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

mainloop = True

disp = {
    "xt" : -1000 ,
    "yt" : -1000 ,
    "xb" : 1080,
    "yb" : 1920,
    "zm"  : 50,
    "zmax": 55,
    "zoom" : 1
    }

def extractdatta():
    listofstar = []
    with open('bsc5p_3d.json') as f:
        data = json.load(f)
    for star in data:

        if any(value is None for value in star.values()) or not "K" in star:
            print(star)
        else: 
            listofstar.append(star)
    return listofstar

def startodisplay(data):
    todislay = []
    window.fill(0)
    for star in data:
        if star["y"] > disp["yt"] and star["y"] < disp["yb"] and star["x"] > disp["xt"] and star["x"] < disp["xb"] and  star["z"] <  disp["zmax"] and star["z"] >  disp["zm"]:
            todislay.append(star)
    print(todislay)
    return todislay
            
def displayastar(star):
    pygame.draw.circle(window, (star["K"]["r"]*100, star["K"]["g"]*100, star["K"]["b"]*100), ((star["x"] - disp["xt"])*disp["zoom"] , (star["y"] - disp["yt"])*disp["zoom"] ),star["z"]*disp["zoom"] /4)
    
star = extractdatta()

    
    
def display():
    startd = startodisplay(star)
    for stars in startd:
        displayastar(stars)
        print('displaying ', stars)
    pygame.display.flip()
            
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                display()
            if event.key == pygame.K_w:
                disp["zoom"] += 0.1
                disp["xb"] = disp["xb"] * disp["zoom"]
                disp["xt"] = disp["xt"] / disp["zoom"]
                disp["yt"] = disp["yt"] / disp["zoom"]
                disp["yb"] = disp["yb"] * disp["zoom"]
                display()
            if event.key == pygame.K_x:
                disp["zoom"] -= 0.1
                disp["xb"] = disp["xb"] / disp["zoom"]
                disp["xt"] = disp["xt"] * disp["zoom"]
                disp["yt"] = disp["yt"] * disp["zoom"]
                disp["yb"] = disp["yb"] / disp["zoom"]
                display()
            if event.key == pygame.K_a:
                disp["zm"] += 5
                disp["zmax"] += 5
                display()
            if event.key == pygame.K_e:
                disp["zm"]-= 5
                disp["zmax"] -= 5
                display()
                
            if event.key == pygame.K_q:
                print("GOT IT")
                disp["xb"] -= 100
                disp["xt"] -= 100
                display()
            if event.key == pygame.K_d:
                print("GOT IT")
                disp["xb"] += 100
                disp["xt"] += 100
                display()
            if event.key == pygame.K_z:
                print("GOT IT")
                disp["yt"] -= 100
                disp["yb"] -= 100
                display()

            if event.key == pygame.K_s:
                print("GOT IT")
                disp["yt"] += 100
                disp["yb"] += 100
                display()
                

