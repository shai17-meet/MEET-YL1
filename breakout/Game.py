from turtle import *
class Ball (Turtle):
	def __init__(self, color, radius, x,y, dx,dy):
		Turtle.__init__(self)
		self.penup()		
		self.color(color)
		self.shapesize(radius,radius,2)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
	
	def move (self):
		self.goto(self.xcor()+self.dx, self.ycor()+self.dy)
		

class Bricks (Turtle):
	def __init__(self, color, height, width, x, y):
		Turtle.__init__(self)
		self.penup()
		self.color(color)
		self.shape('square')
		self.height=height
		self.width=width
		self.shapesize(width,height,2)
		self.goto(x,y)


	

	

class Paddle (Turtle):
	def __init__(self, color, size, shape, x,y, dx,dy):
		Turtle.__init__(self)
		self.color = color
		self.size = size
		self.shape = shape
		self.x,y = x,y
		self.dx,dy = dx,dy
		
	


