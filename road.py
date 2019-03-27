import turtle
import shape
import colors
import config
import label
import time
import setup
from random import randint

turtle.Screen().addshape("res/img/Road/dust.gif")

def clear_scene():
	global painter
	global dust1
	global dust2

	painter.clear()

	dust1.destroy()
	dust2.destroy()
	# if (guse_dash):
		# for obj in scene_obj:
			# obj.destroy()

def draw_dash(painter, x, y):
	painter.penup()
	painter.goto(x, y)
	for i in range(200):
		painter.pendown()
		painter.forward(6)
		painter.penup()
		painter.forward(6)

def draw_scene():
	global painter
	global dust1
	global dust2
	global guse_dash
	global player_position
	global dest_point
	global start_point

	width = config.road_width
	height = config.road_height
	
	if (width < 800):
		width = 800
	if (width > setup.get_width() - 100):
		width = setup.get_width() - 100

	if (height < 400):
		height = 400
	if (height > setup.get_height() - 100):
		height = setup.get_height() - 100

	print("Road width: ", width)
	print("Road height: ", height)

	player_position = []
	dest_point = (width / 2)
	start_point = -(width / 2)

	space_y = height / 5
	half_space_y = space_y / 2
	cur_y = height / 2

	painter = turtle.Turtle()
	painter.color("white")
	painter.ht()
	painter.penup()

	painter.goto(-1200, cur_y)
	painter.pendown()
	painter.forward(2400)

	for i in range(1, 6):
		cur_y -= space_y
		painter.penup()
		painter.goto(-1200, cur_y)
		painter.pendown()
		painter.forward(2400)
		player_position.append(cur_y + half_space_y)
		draw_dash(painter, -1200, cur_y + half_space_y)


	painter.pensize(1)
	painter.right(90)
	for i in range(10):
		painter.penup()
		painter.goto(-(width / 2) + i + 25, height / 2)
		painter.pendown()
		painter.forward(height)
	for i in range(10):
		painter.penup()
		painter.goto(width / 2 + i, height / 2)
		painter.pendown()
		painter.forward(height)


	dust1 = shape.Shape("res/img/Road/dust.gif", "", "", 0, 275 + (height / 2), 1, 1)
	dust2 = shape.Shape("res/img/Road/dust.gif", "", "", 0, -276 - (height / 2), 1, 1)
	

 
def draw_dest(height):
	global scene_obj
	turtle.Screen().addshape("res/img/Road/tree.gif")
	turtle.Screen().addshape("res/img/Road/rock.gif")
	scene_obj = []
	for i in range(5):
		scene_obj.append(shape.Shape("res/img/Road/tree.gif", "", "", randint(-1200, 000), 75 + randint(height / 2, 300), 1, 1))
		scene_obj.append(shape.Shape("res/img/Road/tree.gif", "", "", randint(000, 600), 75 + randint(height / 2, 300), 1, 1))
		scene_obj.append(shape.Shape("res/img/Road/rock.gif", "", "", randint(000, 600), 75 + randint(height / 2, 300), 1, 1))
		scene_obj.append(shape.Shape("res/img/Road/rock.gif", "", "", randint(-1200, 000), 75 + randint(height / 2, 300), 1, 1))

	for i in range(5):
		scene_obj.append(shape.Shape("res/img/Road/tree.gif", "", "", randint(-1200, 000),    - randint(height / 2, 400), 1, 1))
		scene_obj.append(shape.Shape("res/img/Road/tree.gif", "", "", randint(000, 600),    - randint(height / 2, 400), 1, 1))
		scene_obj.append(shape.Shape("res/img/Road/rock.gif", "", "", randint(000, 600),    - randint(height / 2, 400), 1, 1))
		scene_obj.append(shape.Shape("res/img/Road/rock.gif", "", "", randint(-1200, 000),    - randint(height / 2, 400), 1, 1))