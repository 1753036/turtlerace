import shape
import label
import colors
import turtle
import muievent
import time


class LineEdit:
    DEFAULT_WIDTH = 360
    DEFAULT_HEIGHT = 38
    DEFAULT_FONT_SIZE = 14
    MAX_CODE = 30
    def __init__(self, x, y, default_val, number_only = False):
        self.__selected = False
        self.__edited = False
        self.__default_val = default_val
        self.__string = str(self.__default_val)
        self.__entry = shape.Shape("square", colors.get("borders"), colors.get("borders"), x, y - 14, self.DEFAULT_WIDTH, 1, 0)
        self.__text = label.Label(self.__string, colors.get("fg"), x, y, self.DEFAULT_FONT_SIZE)
        self.__number_only = number_only
        self.__top_left = [
            x - (self.DEFAULT_WIDTH / 2),
            y + (self.DEFAULT_HEIGHT / 2)]

        self.__bot_right = [
            x + (self.DEFAULT_WIDTH / 2),
            y - (self.DEFAULT_HEIGHT / 2)]

        muievent.bind_click(self.__checkclick)
        muievent.bind_key(self.__checkkeypress)

    def destroy(self):
        muievent.unbind_click(self.__checkclick)
        muievent.unbind_key(self.__checkkeypress)
        self.__entry.destroy()
        self.__text.destroy()
        del self

    def get_value(self):
        self.__string = str(self.__string)
        if (self.__string[-1:] is "|"):
            self.__string = self.__string[:-1]
            
        if (self.__number_only):
            return int(self.__string)
        return (self.__string)

    def set_text(self, text):
        self.__string = text
        self.__update_field()
            
    def __update_field(self):
        # self.__string += "|"
        self.__text.set_text(self.__string)
        self.__text.update()

    def __is_hover(self, mouse_x, mouse_y):
        return (mouse_x > self.__top_left[0] and 
                mouse_y < self.__top_left[1] and
                mouse_x < self.__bot_right[0] and
                mouse_y > self.__bot_right[1])

    def __checkclick(self, event):
        mouse_x = event.x - (turtle.window_width() / 2)
        mouse_y = (turtle.window_height() / 2) - event.y
        if (self.__is_hover(mouse_x, mouse_y)):
            if (not self.__selected):
                self.__selected = True
                if (not self.__edited):
                    self.__string = ""
                self.__string += "|"
                self.__entry.set_color(colors.get("selected_bg"), colors.get("selected_bg"))
                self.__text.set_text(self.__string)
                self.__text.set_color(colors.get("selected_bg"))
                self.__text.update()
        elif (self.__selected):
            
            self.__selected = False
            if (not self.__edited):
                self.__string = self.__default_val
            else:
                self.__string = self.__string[:-1]
            self.__entry.set_color(colors.get("borders"), colors.get("borders"))
            self.__text.set_color(colors.get("fg"))
            self.__text.set_text(self.__string)
            self.__text.update()

    def __checkkeypress(self, event):
        if (self.__selected):
            if (self.__number_only):
                if (event.char >= "0" and event.char <= "9"):
                    if (len(self.__string) < self.MAX_CODE):
                        self.__edited = True
                        self.__string = self.__string[:-1]
                        self.__string += event.char
                        self.__string += "|"
                        self.__update_field()
            elif ((event.char >= "0" and event.char <= "9") or 
                (event.char >= "a" and event.char <= "z") or
                (event.char >= "A" and event.char <= "Z") or
                (event.keycode == 65)):
                if (len(self.__string) < self.MAX_CODE):
                    self.__edited = True
                    self.__string = self.__string[:-1]
                    self.__string += event.char
                    self.__string += "|"
                    self.__update_field()
            if (event.keycode == 22):
                self.__string = self.__string[:-2]
                self.__string += "|"
                self.__update_field()
                
                


            