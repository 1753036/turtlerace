import turtle
import sys
import menu
import character
import button
import label
import colors
import lineedit
# import config
import time
import board
import road
import race
import shape
import chooseclass
import playsound

from pygame import mixer

from random import randint
from random import shuffle

def init():
    turtle.setup(1400, 800)
    turtle.tracer(0, 0)
    screen = turtle.Screen()
    screen.bgcolor("#202020")

def get_width():
    return turtle.window_width()

def get_height():
    return turtle.window_height()

def play_music(path, loop=1):
	# pygame.mixer.pre_init(44100, -16, 2, 2048)
	# pygame.init()
	mixer.init()
	mixer.music.load(path)
	mixer.music.play(loop)

def show_choose_class():
	# print("WTF")
	chooseclass.show_class()
	chooseclass.next(race.setup_char)
	chooseclass.back(show_menu)

def set_savebtn_callback():
	config.player_name = set_edname.get_value()
	config.road_width = set_edwid.get_value()
	config.road_height = set_edhei.get_value()
	config.save()

	set_title.destroy()
	set_edname.destroy()
	set_edwid.destroy()
	set_edhei.destroy()
	set_savebtn.destroy()

	show_menu()

def show_settings():
	global set_title
	global set_edname
	global set_edwid
	global set_edhei
	global set_savebtn

	set_title = label.Label("SETTINGS", colors.get("subti"), 0, 150, 36)
	set_edname = lineedit.LineEdit(0, 60, config.player_name)
	set_edwid = lineedit.LineEdit(0, 0, config.road_width, True)
	set_edhei = lineedit.LineEdit(0, -60, config.road_height, True)
	set_savebtn = button.Button("SAVE AND BACK", 0, -150, set_savebtn_callback)
	set_savebtn.use_enter()

def about_btn_callback():
	about_title.destroy()
	for item in about_text:
		item.destroy()
	about_btn.destroy()

	show_menu()

def show_about():
    global about_title
    global about_text
    global about_btn

    about_title = label.Label("ABOUT", colors.get("subti"), 0, 150, 36)
    about_text = []
    about_text.append(label.Label("Turtle race is a betting game and designed for single player.", colors.get("fg"), 0, 100))
    about_text.append(label.Label("As long as posible, you can play this game for 1000 minutes, or 1000 years... ", colors.get("fg"), 0, about_text[0].get_y() - 30))
    about_text.append(label.Label("The first, it was made for the mid-term project.", colors.get("fg"), 0, about_text[1].get_y() - 30))
    about_text.append(label.Label("You can download the source from github, don't worry about the license, it's FREE.", colors.get("fg"), 0, about_text[2].get_y() - 30))
    about_text.append(label.Label("Developer: Thai Chi Cuong, Tran Nguyen Quynh Anh, Dinh Le Trieu Duong, Phan Vo Minh Huy, Nguyen Hoang Huy.", colors.get("fg"), 0, about_text[3].get_y() - 30))
    about_text.append(label.Label("Designer: Tran Nguyen Quynh Anh.", colors.get("fg"), 0, about_text[4].get_y() - 30))
    about_btn = button.Button("BACK TO MAIN MENU", 0, -150, about_btn_callback)
    about_btn.use_enter()

def show_menu():
	play_music("res/ad/Menu.mp3", -1)
	menu.show_main_menu(show_choose_class, show_settings, show_about)
	# playsound.playsound("res/ad/Menu.mp3", True)
