import os
import turtle

# Class Label
# 	shape.Shape( shapeName, 		-> "square, circle, turtle..."
#		         borderColor, 		-> "hex code, red, green, blue..."
#				 backgroundColor, 	-> "hex code, red, green, blue..."
#		         x, y, 				-> Descartes coordinate system
#		         w, h, 				-> 300, 400 -> 300x400 pixels
#		         borderWidth = 1): 	-> 1 pixel as default
# Ví dụ:
#	squareShape = shape.Shape("square", 
#                             "transparent", 
#                             "#000000", 
#                             0, 0, 
#                             300, 400)
# 	squareShape.destroy()

class Shape:
	def __init__(self, shape_name, \
		border_color, background_color, \
		x, y, \
		w, h, \
		border_width = 1):

		self.__shape = turtle.Turtle()
		self.__shape.hideturtle()
		self.__shape.shape(shape_name)
		self.__shape.resizemode("auto")
		self.__shape.penup()
		self.set_loc(x, y)
		self.set_color(border_color, background_color)
		self.set_size(w, h, border_width)

	def destroy(self):
		self.__shape.hideturtle()
		self.__shape.clear()
		turtle.update()
		del self.__shape
		del self


	def set_color(self, border_color, background_color):
		self.__shape.color(border_color, background_color)
		turtle.update()

	def set_loc(self, x, y):
		self.__shape.hideturtle()
		self.__shape.goto(x, y)
		self.__shape.showturtle()
		turtle.update()

	def set_size(self, w, h, border_width):
		self.__shape.shapesize(h / 20, w / 20, border_width)
		turtle.update()

	def onclick(self, turn):
		self.__shape.onclick(turn)
		
	def forward(self, dis):
		self.__shape.forward(dis)
		turtle.update()

	def clear(self):
		self.__shape.clear()
		turtle.update()

	def shape(self, shape_name):
		try:
			self.__shape.clear()
			self.__shape.shape(shape_name)
			turtle.update()
		except:
			pass

	# Descartes
	#       90
	#       |
	#180---- ---- 0
	#       |
	#      270

	def set_y(self, y):
		self.__shape.goto(self.get_x(), y)

	def set_x(self, x):
		self.__shape.goto(x, self.get_y())

	def get_x(self):
		return self.__shape.position()[0]

	def get_y(self):
		return self.__shape.position()[1]

	def get_w(self):
		return self.__shape.shapesize()[1] * 20

	def get_h(self):
		return self.__shape.shapesize()[0] * 20
