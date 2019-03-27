import turtle
import threading

func_motion = []
func_click = []
func_release = []
func_key = []
func_enter = []

def init():
    global canvas
    canvas = turtle.getcanvas()
    canvas.bind("<Button-1>", mouse_click)
    canvas.bind("<ButtonRelease-1>", mouse_release)
    canvas.bind("<Motion>", mouse_motion)
    canvas.bind_all("<Key>", key_press)

def mouse_motion(event):
    global func_motion

    for func in func_motion:
        if (func != None):
            func(event)

def mouse_click(event):
    global func_click

    for func in func_click:
        if (func != None):
            func(event)

def mouse_release(event):
    global func_release

    for func in func_release:
        if (func != None):
            func(event)

def key_press(event):
    global func_key
    if (event.keycode == 36):
        for func in func_enter:
            if (func != None):
                func()
    for func in func_key:
        if (func != None):
            func(event)

def bind_motion(func):
    global func_motion
    func_motion.append(func)

def unbind_motion(func):
    global func_motion
    func_motion.remove(func)

def bind_click(func):
    global func_click
    func_click.append(func)

def unbind_click(func):
    global func_click
    func_click.remove(func)

def bind_release(func):
    global func_release
    func_release.append(func)

def unbind_release(func):
    global func_release
    func_release.remove(func)

def bind_key(func):
    global func_key
    func_key.append(func)

def unbind_key(func):
    global func_key
    func_key.remove(func)

def bind_enter(func):
    global func_enter
    func_enter.append(func)

def unbind_enter(func):
    global func_enter
    func_enter.remove(func)