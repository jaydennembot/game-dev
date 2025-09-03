import pgzrun
import random


WIDTH=800
HEIGHT=600

CENTRE_X=WIDTH/2
CENTRE_y=HEIGHT/2
CENTRE=(CENTRE_X,CENTRE_y)
FINAL_LEVEL=7
START_SPEED=10
ITEMS=["chips","plasticbag","battery","bottle"]

game_over=False
game_complete=False
current_level=1

items=[]
animations=[]

def draw():
    global items,current_level,game_over,game_complete
    screen.clear()
    screen.blit("greenphotoimg",(0,0))
    if game_over:
        display_message("game_over","try_again")
    elif game_complete:
        display_message("you won","well done")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTRE, color="white")
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTRE_X, CENTRE_y + 30), color="white")    

def get_option_to_create(number_of_extra_items):
    items_to_create=["paperbag"]
    for i in range(number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
        item=Actor(i+"img")
        new_items.append(item)
    return new_items
    
def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos=(index+1)*gap_size 
        item.x=new_x_pos

def animate_items(item_to_animate):
    global animations 
    for item in item_to_animate:
        duration=START_SPEED-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration,on_finished=handled_game_over,y=HEIGHT)

def handled_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items,current_level
    for item in items:
        if item.collidepoint(pos):
            if "paperbag" in item.image:
                handled_game_complete()            
            else:
                handled_game_over()

def handled_game_complete():
    global current_level,items,animations,game_complete
    stop_animation(animations)
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level+=1
        items=[]
        animations=[]

def stop_animation(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
            
pgzrun.go()
