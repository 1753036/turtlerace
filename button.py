import turtle
import label
import colors
import muievent
import shape
import time

turtle.Screen().addshape("res/img/Else/button.gif")

class Button:
    """
    Sử dụng để tạo button liên kết
    Hỗ trợ 3 trạng thái "normal", "hover", "active"
    """
    DEFAULT_FONT_SIZE = 14

    def __init__(self, text, x, y, callback, fontsize = 16):
        h = fontsize + 10
        w = len(text * fontsize)

        self.__autodest = False
        self.__use_enter = False
        self.__callback = callback
        self.__state = "btn_normal"
        self.__bgbtn = shape.Shape("res/img/Else/button.gif", "", "", x, y, 1, 1)
        self.__label = label.Label(text, "", x, y, fontsize)

        self.__color_by_state()

        self.__top_left = [
            x - (w / 2),
            y + (h / 2)]
        
        self.__bot_right = [
            x + (w / 2),
            y - (h / 2)]

        muievent.bind_click(self.__checkclick)
        muievent.bind_motion(self.__checkhover)
        muievent.bind_release(self.__checkrelease)

    def auto_destroy(self):
        self.__autodest = True

    def use_enter(self):
        self.__use_enter = True
        muievent.bind_enter(self.__checkenter)

    def destroy(self):
        if (self.__use_enter):
            muievent.unbind_enter(self.__checkenter)
        muievent.unbind_click(self.__checkclick)
        muievent.unbind_motion(self.__checkhover)
        muievent.unbind_release(self.__checkrelease)
        self.__bgbtn.destroy()
        self.__label.destroy()
        del self.__bgbtn
        del self.__callback
        del self.__state
        del self.__top_left
        del self.__bot_right
        del self.__label
        del self

    def __color_by_state(self):
        self.__label.set_color(colors.get(self.__state + "_fg"))
        self.__label.update()

    def __is_hover(self, mouse_x, mouse_y):
        return (mouse_x > self.__top_left[0] and 
                mouse_y < self.__top_left[1] and
                mouse_x < self.__bot_right[0] and
                mouse_y > self.__bot_right[1])

    def __checkhover(self, event):
        mouse_x = event.x - (turtle.window_width() / 2)
        mouse_y = (turtle.window_height() / 2) - event.y

        if (self.__is_hover(mouse_x, mouse_y)):
            if (self.__state is "btn_normal"):
                self.__state = "btn_hover"
                self.__color_by_state()
        else:
            if (self.__state is not "btn_normal"):
                self.__state = "btn_normal"
                self.__color_by_state() 
    
    def __checkclick(self, event):
        if (self.__state is "btn_hover"):
            self.__state = "btn_active"
            self.__color_by_state()

    def __checkrelease(self, event):
        mouse_x = event.x - (turtle.window_width() / 2)
        mouse_y = (turtle.window_height() / 2) - event.y
        if (self.__state == "btn_active" and 
            self.__is_hover(mouse_x, mouse_y)):
            self.__state = "btn_hover"
            self.__color_by_state()
            if (self.__callback != None):
                self.__callback()
            if (self.__autodest):
                self.destroy()
            
    def __checkenter(self):
        self.__state = "btn_active"
        self.__color_by_state()
        self.__state = "btn_normal"
        if (self.__callback != None):
            self.__callback()
        if (self.__autodest):
            self.destroy()
