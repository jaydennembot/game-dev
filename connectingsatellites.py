import pgzrun
import random
import time

WIDTH=800
HEIGHT=600

satellites=[]
lines=[]
next_satellite=0
start_time=0
end_time=0
total_time=0
number_of_satellite=9

def create_satellite():
    global start_time
    for i in range (number_of_satellite):  
        satellite = Actor("stellite.png")
        satellite.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        satellites.append(satellite)
    start_time=time.time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    number=1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number+=1
    
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
    
    if next_satellite < number_of_satellite :
        total_time=time.time()-start_time
        screen.draw.text(str(round(total_time,1)),(WIDTH/2,10),fontsize=30)
    
    else :
        screen.draw.text(str(round(total_time,1)),(WIDTH/2,10),fontsize=30)

def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellite :
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite = next_satellite + 1
        else:
            lines = []
            next_satellite = 0
create_satellite()
pgzrun.go()
    
    
        


        

    




















































  