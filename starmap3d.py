import pygame 
import time
import json
import math
import sympy as sp
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

mainloop = True

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

def vectorexpressionfromline(vector1, vector2, ):
    return (vector1[0] - vector2[0], vector1[1] - vector2[1], vector1[2] - vector2[2])

def distance_3d(point1, point2):
    return math.sqrt(
        (point2[0] - point1[0])**2 +
        (point2[1] - point1[1])**2 +
        (point2[2] - point1[2])**2
    )

def parametricequation(pointA, pointB):
    vectorAB = vectorexpressionfromline(pointA, pointB)
    t = sp.symbols('t')
    equation = vectorAB[1] * t - 5

    solution = sp.solve(equation, t)

    x = (vectorAB[0] * round(solution[0]))
    y = (vectorAB[1] * round(solution[0]))
    z = (vectorAB[2] * round(solution[0]))
    return x, y, z
    
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
    i = 0
    for star in data:
        arct = math.atan2(star["x"], star["y"])

        if arct < disp["rotation"] + disp["fov"] * (math.pi / 180) and arct > disp["rotation"] and distance_3d((star["x"], star["y"], star["z"]), (0, 0, 0))< 50:
            i += 1
            print(i)
            pos = parametricequation((0, 0, 0), (star["x"], star["y"], star["z"]))
            todislay.append((star, pos))
    print('number of it', i)
    print(todislay)
    
    return todislay

def display():
    startd = startodisplay(star)
    for stars in startd:
        if stars[1][0] > disp["xt"] and stars[1][0] < disp["xb"] and stars[1][1] > disp["yt"] and stars[1][1] < disp["yb"]:   
            displayastar(stars)
            print('displaying', stars)

        else:
            print('not displaying', stars)
        
    pygame.display.flip()
    
def displayastar(star):
    
    midpoint = ((star[1][0] - disp["xt"])*disp["zoom"] , (star[1][1] - disp["yt"])*disp["zoom"] )
    midpoint = (int(midpoint[0]), int(midpoint[1]))
    print("IST DISPLAIING", (star[0]["K"]["r"]*100, star[0]["K"]["g"]*100, star[0]["K"]["b"]*100), midpoint, abs(int(star[1][2]*disp["zoom"])))
    pygame.draw.circle(window, (star[0]["K"]["r"]*100, star[0]["K"]["g"]*100, star[0]["K"]["b"]*100), midpoint,   abs(int(star[1][2]*disp["zoom"])))
    


star = extractdatta()

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                display()
            if event.key == pygame.K_d:
                displayastar(({'i': 9038, 'n': 'HD223778', 'x': 10.551583146596888, 'y': 0.08990598671314076, 'z': 2.7185887927471972, 'p': 10.89654601284485, 'N': 0.26695005573224595, 'K': {'r': 1, 'g': 0.666, 'b': 0.419}}, (590.888656209426, 5.03473525593588, 152.240972393843)))
                pygame.display.flip()

            if event.key == pygame.K_q:
                disp["rotation"] =- 1
                display()
