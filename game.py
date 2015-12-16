from meet import *
import random
import time
cells=[]
get_screen_width()
get_screen_height()
p=0

for i in range(10):
    m = random.randint(1, 2)
    n = random.randint(1, 2)
    radius = random.randint(1, 50)
    x = random.randint(int(-get_screen_width()), int(get_screen_width()))
    y = random.randint(-get_screen_height(), get_screen_height())
    if(m == 1):
        dx = -(random.random())
    else:
        dx = random.random()
    if(n == 1):
        dy = -(random.random())
    else:
        dy = random.random()   
    cell_list = {"x":x,"y":y,"radius":radius,"dx":dx,"dy":dy,"color":"blue"}
    cell = create_cell(cell_list)
    cells.append(cell)

user_cell={"x":0,"y":0,"radius":20,"dy":2,"dx":2,"color":"red"}
z=create_cell(user_cell)
cells.append(z)

alive = True
while alive:
	move_cells(cells)
	for cell in cells:
		if(cell.xcor()>get_screen_width()):
			cell.set_dx(cell.get_dx() * -1)
		if(cell.xcor()<0-get_screen_width()):
			cell.set_dx(cell.get_dx() * -1)
	for cell in cells:
		if(cell.ycor()>get_screen_height()):
			cell.set_dy(cell.get_dy() * -1)
		if(cell.ycor()<0-get_screen_height()):
			cell.set_dy(cell.get_dy() * -1)
	for cell in cells:
		for other in cells:
			distance = ((cell.xcor()-other.xcor())**2+(cell.ycor()-other.ycor())**2)**0.5
			if distance < cell.get_radius():
				if cell.get_radius() > other.get_radius():
					if other == z:
						write('Game over!',align='center',font=("Arial",50,'bold'))
					cell.set_radius(cell.get_radius()+other.get_radius()/20)
					other.goto(get_random_x(),get_random_y())
					
	x,y=get_user_direction(z)
	z.set_dx(x)
	z.set_dy(y)
	
