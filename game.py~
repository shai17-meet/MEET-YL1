from meet import *
import random
cells=[]
get_screen_width()
get_screen_height()
p=0
while p<50:
	cell1={"x":get_random_x(),"y":get_random_y(),"radius":random.randint(0,30),"dy":0,"dx":random.random(),"color":"blue"}
	z=create_cell(cell1)
	cells.append(z)
	p+=1

while True:
	move_cells(cells)
	for cell in cells:
		if(cell.xcor()>get_screen_width()):
			cell.set_dx(cell.get_dx() * -1)
		if(cell.xcor()<0-get_screen_width()):
			cell.set_dx(cell.get_dx() * -1)

