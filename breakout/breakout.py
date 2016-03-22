from Game import *
from turtle import *
tracer(0)
screen=getscreen()
canvas=getcanvas() 
CANVAS_WIDTH = canvas.winfo_width() 
CANVAS_HEIGHT = canvas.winfo_height() 
brickslist=[]

def get_screen_width():
	global CANVAS_WIDTH
	return int(CANVAS_WIDTH/2-10)


def get_screen_height():
	global CANVAS_HEIGHT
	return int(CANVAS_HEIGHT/2-5)
ball1=Ball("orange",1,0,70,0.7,-0.7)
f=0
z=-310
while(f<14):
	brick=Bricks("brown",2,1,z,280)
	z+=47
	f+=1
	brickslist.append(brick)
k=0
z=-310
while(k<14):
	brick=Bricks("brown",2,1,z,250)
	z+=47
	k+=1
	brickslist.append(brick)
p=0
z=-310
while(p<14):
	brick=Bricks("brown",2,1,z,220)
	z+=47
	p+=1
	brickslist.append(brick)
q=0
z=-310
while(q<14):
	brick=Bricks("brown",2,1,z,190)
	z+=47
	q+=1
	brickslist.append(brick)
w=0
z=-310
while(w<14):
	brick=Bricks("brown",2,1,z,160)
	z+=47
	w+=1
	brickslist.append(brick)
e=0
z=-310
while(e<14):
	brick=Bricks("brown",2,1,z,130)
	z+=47
	e+=1
	brickslist.append(brick)
while True:
	ball1.move()
	if(ball1.xcor()>get_screen_width()):
		ball1.dx*=-1
	if(ball1.xcor()<-get_screen_width()):
		ball1.dx*=-1
	if(ball1.ycor()>get_screen_height()):
		ball1.dy*=-1
	if(ball1.ycor()<-get_screen_height()):
		ball1.dy*=-1
	for brick in brickslist:
		if(ball.ycor+ball.radius>=brick.ycor-brick.height/2)and(ball.ycor-ball.radius>=brick.ycor+brick.height/2)and(ball.xcor+ball.radius>=brick.xcor - brick.width/2)and(ball.xcor-ball.radius>=brick.xcor+brick.width/2):  -------------> fix the - and +
			ball1.dx*=-1
			ball1.dy*=-1


	screen.update()

