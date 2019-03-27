import button
import label
import shape
import colors
import turtle
import sys
import simpleaudio

PATH_MENU_CHAR1 = [
"res/img/Cat/Blue/Cat---Design-1.gif",
"res/img/Cat/Blue/Cat---Design-2.gif"]
PATH_MENU_CHAR2 = [
"res/img/Chicken/Gray/Chicken---Design-1.gif", 
"res/img/Chicken/Gray/Chicken---Design-2.gif"]
PATH_MENU_CHAR3 = [
"res/img/Dog/Green/Dog---Design-1.gif", 
"res/img/Dog/Green/Dog---Design-2.gif"]
PATH_MENU_CHAR4 = [
"res/img/Fox/Orange/Fox---Design-1.gif", 
"res/img/Fox/Orange/Fox---Design-2.gif"]
PATH_MENU_CHAR5 = [
"res/img/Pig/Pink/Pig---Design-1.gif", 
"res/img/Pig/Pink/Pig---Design-2.gif"]

PATH_MENU_TIT_BG = "res/img/Else/menu_titbg.gif"

turtle.Screen().addshape(PATH_MENU_TIT_BG)

turtle.Screen().addshape(PATH_MENU_CHAR1[0])
turtle.Screen().addshape(PATH_MENU_CHAR2[0])
turtle.Screen().addshape(PATH_MENU_CHAR3[0])
turtle.Screen().addshape(PATH_MENU_CHAR4[0])
turtle.Screen().addshape(PATH_MENU_CHAR5[0])

turtle.Screen().addshape(PATH_MENU_CHAR1[1])
turtle.Screen().addshape(PATH_MENU_CHAR2[1])
turtle.Screen().addshape(PATH_MENU_CHAR3[1])
turtle.Screen().addshape(PATH_MENU_CHAR4[1])
turtle.Screen().addshape(PATH_MENU_CHAR5[1])

def callback1():
    destroy_main_menu()
    menu_calls[0]()

def callback2():
    destroy_main_menu()
    menu_calls[1]()

def callback3():
    destroy_main_menu()
    menu_calls[2]()

def callback4():
    sys.exit(0)

def menu_char_anim():
    global menu_runan

    if (menu_visib):
        if (menu_runan > 1):
            menu_runan = 0
        try:
            menu_chars[0].shape(PATH_MENU_CHAR1[menu_runan])
        except:
            pass

        try:
            menu_chars[1].shape(PATH_MENU_CHAR2[menu_runan])
        except:
            pass

        try:
            menu_chars[2].shape(PATH_MENU_CHAR3[menu_runan])
        except:
            pass

        try:
            menu_chars[3].shape(PATH_MENU_CHAR4[menu_runan])
        except:
            pass

        try:
            menu_chars[4].shape(PATH_MENU_CHAR5[menu_runan])
        except:
            pass

        menu_runan += 1
        turtle.ontimer(menu_char_anim, 500)

def destroy_main_menu():
    global menu_visib
    menu_visib = False

    for item in menu_items:
        item.destroy()
    for item in menu_chars:
        item.destroy()
    for item in menu_calls:
        del item

    menu_titbg.destroy()
    menu_title.destroy()
    menu_subti.destroy()

def show_main_menu(f1, f2, f3):
    global menu_title
    global menu_subti
    global menu_calls
    global menu_items
    global menu_titbg
    global menu_chars
    global menu_visib
    global menu_runan

    menu_runan = 0
    menu_visib = True
    menu_titbg = shape.Shape(PATH_MENU_TIT_BG, "", "", 0, 235, 1, 1)
    menu_title = label.Label("TURTLE RACE", colors.get("title"), 0, 250, 48)
    menu_subti = label.Label("THE BEST BETTING GAME", colors.get("subti"), 150, 200, 18)

    menu_calls = [f1, f2, f3]

    menu_items = [
    button.Button(" START ",    0,  30, callback1),
    button.Button(" SETTINGS ", 0, -30, callback2),
    button.Button(" ABOUT ",    0, -90, callback3),
    button.Button(" EXIT ",     0, -150, callback4)]

    menu_chars = [
    shape.Shape(PATH_MENU_CHAR1[0], "", "", 0, 350, 1, 1),
    shape.Shape(PATH_MENU_CHAR2[0], "", "", -400, 200, 1, 1),
    shape.Shape(PATH_MENU_CHAR3[0], "", "", 400, 0, 1, 1),
    shape.Shape(PATH_MENU_CHAR4[0], "", "", -300, -200, 1, 1),
    shape.Shape(PATH_MENU_CHAR5[0], "", "", 300, -200, 1, 1),]

    menu_char_anim()