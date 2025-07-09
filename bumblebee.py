import random
import pgzrun

HEIGHT=475
WIDTH=700

score=0
gameover=False

bee=Actor('bumblebee')
flower=Actor('flower')
bee.pos=50,50
flower.pos=(WIDTH/2,HEIGHT/2)

def draw():
    screen.clear()
    screen.blit("bggg",(0,0))
    
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(score),color="black",topleft=(10,10))

    if gameover:
        screen.fill("red") 
        screen.draw.text(" GAME OVER FINAL  SCORE IS  "+str(score),color="black",topleft=(10,10))  

def place(): 
    flower.y=random.randint(50,HEIGHT-50)                                                            
    flower.x=random.randint(50,WIDTH-50)
def time_up():
    global gameover
    gameover=True

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-7
    if keyboard.up:
        bee.y=bee.y-7
    if keyboard.down:
        bee.y=bee.y+7
    if keyboard.right:
        bee.x=bee.x+7
    
    flowers_collected=bee.colliderect(flower)
    
    if flowers_collected:
        score+=1
        place()
    
clock.schedule(time_up,60)    








pgzrun.go()

