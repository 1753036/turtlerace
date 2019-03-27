import turtle
import time
# Class Label
#   label.Label(text,       -> "ABC, XYZ"
#               color,      -> "hex code, red, green, blue, ..."
#               x, y,       -> Descartes coordinate system
#               size = 12): -> 12pt as default
# Ví dụ:
#   label.Label("I love you:3", "red", 0, 0)
class Label:
    DEFAULT_FONT_NAME = "Arial"
    DEFAULT_STYLE = "bold"


    def __init__(self, text, color, x, y, size = 14):
        self.__alignment = "center"
        self.__label = turtle.Turtle()
        self.__label.hideturtle()
        self.__label.penup()
        self.__label.goto(x, y - (size * 2) / 3)
        self.__defsize = size
        self.__animup = False
        self.set_color(color)
        self.set_text(text)
        self.set_size(size)
        self.update()
        
    def update(self):
        self.__label.clear()
        self.__label.color(self.__color)
        self.__label.write(self.__text, False, self.__alignment, self.__font)
        
    def clear(self):
        self.__label.clear()

    def destroy(self):
        self.__label.clear()
        del self.__label
        del self.__text
        del self.__color
        del self.__font
        del self.__alignment
        del self

    def grown_up(self):
        self.__animup = True
        self.clear()
        for i in range(1, 20):
            self.set_size(self.__font[1] + 1)
            self.update()

    def grown_down(self):
        self.set_size(self.__defsize)
        self.update()


    def align(self, alignment):
        if (alignment == "center" and
            alignment != "left" and
            alignment != "right"):
            alignment = "center"
        self.__alignment = alignment
        self.update()

    def set_text(self, text):
        self.__text = text

    def set_color(self, color):
        if (color == "" or color == "transparent"):
            color = "black"
        self.__color = color

    def set_size(self, new_size):
        self.__font = (self.DEFAULT_FONT_NAME, new_size, self.DEFAULT_STYLE)

    def get_x(self):
        return self.__label.position()[0]

    def get_y(self):
        return self.__label.position()[1]

    def set_x(self, x):
        self.__label.goto(x, self.get_y())

    def set_y(self, y):
        self.__label.goto(self.get_x(), y)