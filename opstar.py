import pygame 
import time
import json
import math
disp = {
    "xt" : 0 ,
    "yt" : 0 ,
    "xb" : 1080,
    "yb" : 1920,
    "dm"  : 50,
    "dmax": 55,
    "zoom" : 1,
    "fov" : 70,
    "rotation" : 0
    }

plan = {
    "normal" : (0, 1, 0),
    "firstpoint" : (0, 5, 0),
    "equation" : "y = 5"
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



def getprojectedpos(point):
    x = (point["x"]/point["z"]+plan["firstpoint"][1])*disp["fov"]+disp["xb"]/2
    y = (point["y"]/point["z"]+plan["firstpoint"][1])*disp["fov"]+disp["yb"]/2
    return x, y

def startodisplay():
    for star in allstar:
        posinscreen = getprojectedpos(star)
        if posinscreen[0] < disp["xb"] and posinscreen[0] > disp["xt"] and posinscreen[1] < disp["yb"] and posinscreen[1] > disp["yt"]:
            print(posinscreen)




allstar = extractdatta()

startodisplay()