import pygame
import time
import pgzrun

HEIGHT=800
WIDTH=800

marquee_box=Rect(0,0,700,80)
question_box=Rect(0,0,550,160)
time_box=Rect(0,0,150,160)
answer_box1=Rect(0,0,200,140)
answer_box2=Rect(0,0,200,140)
answer_box3=Rect(0,0,200,140)
answer_box4=Rect(0,0,200,140)
skip_box=Rect(0,0,150,280)

score=0
time_left=10
question_file_name="jaydenquiz.txt"
marquee_message=""
is_game_over=False
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0
question_index=0
#move ip means move in place
question_box.move_ip(20,100)
time_box.move_ip(600,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(600,270)
marquee_box.move_ip(0,0)

def draw():
    global marquee_message 
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"red")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(time_box,"red")
    screen.draw.filled_rect(answer_box1,"blue")
    screen.draw.filled_rect(answer_box2,"red")
    screen.draw.filled_rect(answer_box3,"blue")
    screen.draw.filled_rect(answer_box4,"red")
    screen.draw.filled_rect(skip_box,"blue")

    marquee_message="welcome to the Quiz master!!!"
    marquee_message=marquee_message+ f"q:{question_index} of {question_count}"
    
    screen.draw.textbox(marquee_message,marquee_box,color="blue")
    screen.draw.textbox(str(time_left),time_box,color="blue",shadow=(0.5,0.5),scolor="grey")
    screen.draw.textbox("SKIP",skip_box,color="red",angle=-90)
    screen.draw.textbox(question[0].strip(),question_box,color="red")
    index=1
    for answerbox in answer_boxes:
        screen.draw.textbox(question[index].strip(),answerbox,color="white")
        index+=1

def move_marquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left=WIDTH

def update():
    move_marquee()


def read_question_file():
    global question_count, questions
    q_file=open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count+=1
    q_file.close()    

def read_next_question():
    global question_index
    question_index+=1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
    
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,question,time_left,questions
    score += 1
    if questions:
        question=read_next_question()
        time_left=10
    else:game_over()
    
#if i dont want to end game change to read next question
                
        
def game_over():
    global question ,time_left, is_game_over
    message=f"nice try you lose\n you got {score} questions correct"
    question=[message,"-","-","-","-",5]
    time_left=0
    is_game_over=True

def skip_question():
    global question,time_left
    if questions and not is_game_over:
        question=read_next_question()
        time_left=30

    else:
        game_over()

def update_time_left():
    global time_left 
    if time_left:
        time_left-=1
    else:
        game_over()

read_question_file()
question=read_next_question()
clock.schedule_interval(update_time_left,1)

pgzrun.go()

