import shape
import label
import config
import colors
import turtle
import os
from random import randint

class Character:
	DICT_SPEED = {"Fox": 9,
	"Dog": 10,
	"Cat": 111,
	"Pig": 2,
	"Chicken": 4}
	DICT_MIN_SPEED = {"Fox": 5,
	"Dog": 4,
	"Cat": 5,
	"Pig": 0,
	"Chicken": 2}

	
	def __init__(self, charclass, color, name, x, y):

		self.__anim_stand = [0, 1]
		self.__anim_run = [2, 5]
		self.__anim_runback = [6, 9]
		self.__anim_win = [10, 11]
		self.__anim_lose = [12, 13]
		self.__anim_list = []
		self.__anim_ind = 0
		self.__anim_stick = 0
		self.__anim_start = 0
		self.__anim_end = 0
		self.__anim_delay = 0



		self.__load_animation("res/img/" + charclass + "/animation.txt", color)

		if (color is "Blue"):
			color = "#55aaff"
		elif (color is "Green"):
			color = "#00fcb9"
		elif (color is "Gray"):
			color = "#A0A0A0"

		self.__char_name = label.Label(name, color.lower(), x, y + 65)
		self.__char_shape = shape.Shape(self.__anim_list[0], "", "", x, y + 15, 64, 64)

		self.__max_speed = self.DICT_SPEED[config.player_class]
		self.__min_speed = self.DICT_MIN_SPEED[config.player_class]

		self.name = name
		self.color = color
		self.time = 0.0
		self.win = 0
		self.lose = 0
		self.__pause = True
		self.__runback = False

		# print(shape_name)

	def destroy(self):
		self.__char_shape.destroy()
		self.__char_name.destroy()
		del self.__char_shape
		del self.__char_name
		del self.__anim_stand
		del self.__anim_run
		del self.__anim_runback
		del self.__anim_win
		del self.__anim_lose
		del self.__anim_list
		del self


	def get_x(self):
		return self.__char_shape.get_x()

	def get_y(self):
		return self.__char_shape.get_y()

	def forward(self):
		dist = randint(2, self.__max_speed)
		if (not self.__pause):
			if (self.__runback):
				self.__char_shape.forward(-dist)
				self.__char_name.set_x(self.__char_name.get_x() - dist)
				self.__char_name.update()
			else:
				self.__char_shape.forward(dist)
				self.__char_name.set_x(self.__char_name.get_x() + dist)
				self.__char_name.update()

	def set_animation(self, animation):
		if (animation is "stand"):
			self.__anim_start = self.__anim_stand[0]
			self.__anim_end = self.__anim_stand[1]
			self.__anim_delay = 10
			self.__pause = True
			self.__runback = False
		elif (animation is "run"):
			self.__anim_start = self.__anim_run[0]
			self.__anim_end = self.__anim_run[1]
			if (config.player_class is "Dog"):
				self.__anim_delay = 4
			elif (config.player_class is "Pig"):
				self.__anim_delay = 7
			else:
				self.__anim_delay = 2
			self.__pause = False
			self.__runback = False
		elif (animation is "runback"):
			self.__anim_start = self.__anim_runback[0]
			self.__anim_end = self.__anim_runback[1]
			if (config.player_class is "Dog"):
				self.__anim_delay = 4
			elif (config.player_class is "Pig"):
				self.__anim_delay = 7
			else:
				self.__anim_delay = 2
			self.__pause = False
			self.__runback = True
		elif (animation is "win"):
			self.__anim_start = self.__anim_win[0]
			self.__anim_end = self.__anim_win[1]
			self.__anim_delay = 10
			self.__pause = True
			self.__runback = False
		elif (animation is "lose"):
			self.__anim_start = self.__anim_lose[0]
			self.__anim_end = self.__anim_lose[1]
			self.__anim_delay = 10
			self.__pause = True
			self.__runback = False
		self.__char_shape.clear()
		self.__char_shape.shape(self.__anim_list[self.__anim_start])

	def run_animation(self):
		# print("Current: ", self.__anim_ind)
		if (self.__anim_stick >= self.__anim_delay):
			self.__anim_stick = 0

			if (self.__anim_ind > self.__anim_end or self.__anim_ind < self.__anim_start):
				self.__anim_ind = self.__anim_start
			
			self.__char_shape.shape(self.__anim_list[self.__anim_ind])
			self.__anim_ind += 1
		self.__anim_stick += 1

		self.forward()

	def __load_animation(self, filename, color):
		file = open(filename, "r")
		data = file.readlines()
		screen = turtle.Screen()
		for dat in data:
			if (dat[0] is not "#"):
				shape_name = "res/img/" + config.player_class + "/" + color + "/" + dat[:-1]
				# print(shape_name)
				self.__anim_list.append(shape_name)
				screen.addshape(shape_name)
		# print(len(self.__anim_list))

	def load_profile(self):
		
		path = "data/" + self.name + ".txt"
		if os.path.isfile(path):
			file = open(path, "r")
			data = file.readlines()
			self.win = int(data[0])
			self.lose = int(data[1])
			file.close()

	def save_profile(self):
		path = "data/" + self.name + ".txt"

		if not os.path.exists(os.path.dirname(path)):
		    try:
		        os.makedirs(os.path.dirname(path))
		    except OSError as exc: # Guard against race condition
		        if exc.errno != errno.EEXIST:
		            raise


		file = open(path, "w")
		file.write(str(self.win) + "\n")
		file.write(str(self.lose))
		file.close()
	def getKey(self):
		return self.time