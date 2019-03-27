import turtle
import shape
import label
import colors
import config
import button

def update_preview():
	global cclass_preview
	turtle.Screen().addshape("res/img/Avt/" + config.player_color + "/" + config.player_class + ".gif")
	cclass_preview.shape("res/img/Avt/" + config.player_color + "/" + config.player_class + ".gif")

def click_green(x, y):
	config.player_color = "Green"
	update_preview()

def click_blue(x, y):
	config.player_color = "Blue"
	update_preview()

def click_pink(x, y):
	config.player_color = "Pink"
	update_preview()

def click_orange(x, y):
	config.player_color = "Orange"
	update_preview()

def click_gray(x, y):
	config.player_color = "Gray"
	update_preview()

def click_cat(x, y):
	config.player_class = "Cat"
	update_preview()

def click_dog(x, y):
	config.player_class = "Dog"
	update_preview()

def click_chicken(x, y):
	config.player_class = "Chicken"
	update_preview()

def click_fox(x, y):
	config.player_class = "Fox"
	update_preview()

def click_pig(x, y):
	config.player_class = "Pig"	
	update_preview()

def show_class():
	#CONFIG DEFAULT VALUE

	config.player_class = "Fox"
	config.player_color = "Orange"

	path_icon = ["res/img/Avt/Green/Cat.gif", #Cat
	"res/img/Avt/Blue/Dog.gif", #Dog
	"res/img/Avt/Pink/Chicken.gif", #Chicken
	"res/img/Avt/Orange/Fox.gif", #Fox
	"res/img/Avt/Gray/Pig.gif"] #Pig

	for path in path_icon:
		turtle.Screen().addshape(path)

	ccolors= ["green",
	"blue",
	"pink",
	"orange",
	"gray"]

	global cclass_preview
	global cclass_title
	global cclass_items
	global cclass_colors

	cclass_title = label.Label("CHOOSE CLASS", colors.get("subti"), 0, 200, 36)

	cclass_items = []
	cclass_colors = []

	cclass_items.append(shape.Shape(path_icon[0], "", "white", 168, 100, 64, 64))
	cclass_items.append(shape.Shape(path_icon[1], "", "white", 84, 100, 64, 64))
	cclass_items.append(shape.Shape(path_icon[2], "", "white", 0, 100, 64, 64))
	cclass_items.append(shape.Shape(path_icon[3], "", "white", -84, 100, 64, 64))
	cclass_items.append(shape.Shape(path_icon[4], "", "white", -168, 100, 64, 64))

	cclass_preview = shape.Shape(path_icon[0], "", ccolors[0], 0, 0, 64, 64)
	config.player_class = "Cat"
	config.player_color = "Green"

	cclass_items[0].onclick(click_cat)
	cclass_items[1].onclick(click_dog)
	cclass_items[2].onclick(click_chicken)
	cclass_items[3].onclick(click_fox)
	cclass_items[4].onclick(click_pig)

	cclass_colors.append(shape.Shape("square", "", ccolors[0], -168, -100, 64, 64))
	cclass_colors.append(shape.Shape("square", "", ccolors[1], -84, -100, 64, 64))
	cclass_colors.append(shape.Shape("square", "", ccolors[2], 0, -100, 64, 64))
	cclass_colors.append(shape.Shape("square", "", ccolors[3], 84, -100, 64, 64))
	cclass_colors.append(shape.Shape("square", "", ccolors[4], 168, -100, 64, 64))

	cclass_colors[0].onclick(click_green)
	cclass_colors[1].onclick(click_blue)
	cclass_colors[2].onclick(click_pink)
	cclass_colors[3].onclick(click_orange)
	cclass_colors[4].onclick(click_gray)

def next_call():
	global cclass_next_btn
	global cclass_next_func

	global cclass_preview
	global cclass_title
	global cclass_items
	global cclass_colors

	for item in cclass_items:
		item.destroy()

	for item in cclass_colors:
		item.destroy()

	cclass_back_btn.destroy()
	cclass_next_btn.destroy()
	cclass_preview.destroy()
	cclass_title.destroy()

	turtle.update()
	try:
		cclass_next_func()
	except:
		pass

def next(func):
	global cclass_next_btn
	global cclass_next_func
	cclass_next_func = func
	cclass_next_btn = button.Button("NEXT", 100, -200, next_call)
	cclass_next_btn.use_enter()

def back_call():
	global cclass_next_btn
	global cclass_next_func

	global cclass_preview
	global cclass_title
	global cclass_items
	global cclass_colors

	for item in cclass_items:
		item.destroy()

	for item in cclass_colors:
		item.destroy()

	cclass_next_btn.destroy()
	cclass_back_btn.destroy()
	cclass_preview.destroy()
	cclass_title.destroy()

	turtle.update()

	try:
		cclass_back_func()
	except:
		pass

def back(func):
	global cclass_back_btn
	global cclass_back_func
	cclass_back_func = func
	cclass_back_btn = button.Button("BACK", -100, -200, back_call)
