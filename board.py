import turtle

import label
import shape
import colors

import config

class Board:
    class __Row:        
        def __init__(self, y, cols, width):
            self.__labels = []
            self.__icons = []
            self.__width = width
            self.__cols = cols
            self.__perx = self.__width / (self.__cols - 1)
            self.__x =  -((self.__width) / 2)
            self.__y = y
            
            
            for i in range(self.__cols):
                self.__labels.append(label.Label("", colors.get("lead_fg"), self.__x, self.__y))
                self.__labels[i].align("center")
                self.__x += self.__perx

        def update(self):
            for item in self.__labels:
                item.update()

            for icon in self.__icons:
                icon.update()

        def set_text(self, col, text, size = 13):
            self.__labels[col].set_text(text)
            self.__labels[col].set_size(size)

        def set_color(self, col, color):
            self.__labels[col].set_color(color)
        
        def set_icon(self, col, icon):
            self.__icons.append(shape.Shape(icon, 
            colors.get("lead_border"), colors.get("lead_bg"), 
            self.__labels[col].get_x() - 32, self.__y, 32, 32, 1))
        
        def align(self, col, alignment):
            self.__labels[col].clear()
            self.__labels[col].align(alignment)
            

        def destroy(self):
            for lab in self.__labels:
                lab.destroy()
            for icon in self.__icons:
                icon.destroy()
        

    """
    
    """
    def __init__(self, title, x, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__width = 600
        self.__height = 400
        self.__items = []
        self.__space_y = -self.__height / self.__rows
        self.__y = 200 + self.__space_y
        
        self.__title_text = title
        self.__draw_title()
        self.__draw_items()

    def update(self):
        self.__title.update()
        for item in self.__items:
            item.update()

    def destroy(self):
        self.__title.destroy()
        for item in self.__items:
            item.destroy()

    def __draw_title(self):
        title_color = colors.get("lead_title_fg")
        if (self.__title_text is "YOU WIN"):
            title_color = "#AAFF50"
        self.__title = label.Label(
        self.__title_text, 
        title_color, 
        0, 250, 72)

    def __draw_items(self):
        for i in range(self.__rows):
            self.__items.append(self.__Row( self.__y, self.__cols, self.__width))
            self.__y += self.__space_y

    def set_text(self, row, col, text, size = 15):
        self.__items[row].set_text(col, text, size)
    
    def set_color(self, row, col, color):
        if (color is "Blue"):
            color = "#55aaff"
        elif (color is "Green"):
            color = "#00fcb9"
        elif (color is "Gray"):
            color = "#A0A0A0"
        self.__items[row].set_color(col, color)

    def set_icon(self, row, col, icon):
        self.__items[row].set_icon(col, icon)
    
    def align(self, row, col, alignment):
        self.__items[row].align(col, alignment)







