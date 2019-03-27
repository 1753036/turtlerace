import config
import character
import road
import random
import turtle
import time
import board
import colors
import setup
import button
# import matplotlib.pyplot as plt

list_state = ["run", "run", "stand", "stand", "runback", "run", "run", "run", "run", "run", "run"]
list_color = ["Orange", "Gray", "Green", "Pink", "Blue"]
list_char = [character.Character, character.Character, character.Character, character.Character, character.Character]
# char_state = ["stop", "stop", "stop", "stop", "stop"]

def random_state():
	# print("WTF")
	if (is_all_finished()):
		show_table()
		return

	for i in range(5):
		# print(list_finished[i])
		if (list_finished[i] == False):
			current_state = list_state[random.randint(0, len(list_state) - 1)]
			list_char[i].set_animation(current_state)

	try:
		turtle.ontimer(random_state, 1000)
	except:
		pass

	

def race_running():
	global race_winner
	global race_timer
	global list_finished

	if (bool_running == False):
		return

	start_stick = time.clock()
	# print(is_all_finished())
	for i in range(5):
		try:
			list_char[i].run_animation()
		except:
			pass

		if (list_finished[i]):
			continue

		if (list_char[i].get_x() < road.start_point):
			list_char[i].set_animation("run")
		elif (list_char[i].get_x() > road.dest_point):
			if (race_winner is "None"):
				race_winner = list_color[i]
				list_char[i].win += 1
				list_char[i].set_animation("win")
			else:
				list_char[i].lose += 1
				list_char[i].set_animation("lose")
			list_finished[i] = True
			list_char[i].time = "{0:.2f}".format(race_timer)

	cur_stick = (time.clock() - start_stick)
	delay_stick = 25 - (cur_stick * 1000)
	# print(delay_stick)
	if (delay_stick > 0):
		try:
			turtle.ontimer(race_running, int(delay_stick))
		except:
			pass
	else:
		
		race_running()
def race_clocking():
	if (bool_running == False):
		return
	global race_timer
	race_timer += 0.01
	turtle.ontimer(race_clocking, 10)

def setup_global():
	global list_finished
	global bool_running
	global race_winner
	global race_timer


	list_finished = [False, False, False, False, False]

	bool_running = True

	race_winner = "None"

	race_timer = 0.0

def setup_char():

	setup_global()

	road.draw_scene()

	random.shuffle(list_color)

	curname = config.player_color

	for i in range(5):
		if (config.player_color is list_color[i]):
			curname = config.player_name
		else:
			curname = list_color[i]
		list_char[i] = character.Character(config.player_class, list_color[i], curname, road.start_point, road.player_position[i])
		list_char[i].set_animation("stand")
		list_char[i].load_profile()

	setup.play_music("res/ad/Run.mp3", -1)
	race_running()
	turtle.ontimer(random_state, 1000)
	turtle.ontimer(race_clocking, 1000)

def is_winner():
	return race_winner == config.player_color

def is_all_finished():
	return list_finished[0] and list_finished[1] and list_finished[2] and list_finished[3] and list_finished[4]

def lead_btn_callback():
	global bool_running
	global list_char
	global list_finished

	bool_running = False
	lead_table.destroy()
	lead_btn.destroy()
	for item in list_char:
		item.save_profile()
		item.destroy()

	road.clear_scene()

	setup.show_menu()

def show_table():
	global lead_table
	global lead_btn
	global list_char

	if (is_winner()):
		setup.play_music("res/ad/Winner.mp3")
		lead_table = board.Board("YOU WIN", 0, 9, 3)
	else:
		setup.play_music("res/ad/Loser.mp3")
		lead_table = board.Board("YOU LOSE", 0, 9, 3)

	list_char.sort(key=lambda k: k.time)

	lead_table.set_color(0, 0, colors.get("title"))
	lead_table.set_text(0, 0, "NAME", 24)
	lead_table.set_color(0, 1, colors.get("title"))
	lead_table.set_text(0, 1, "TIME", 24)
	lead_table.set_color(0, 2, colors.get("title"))
	lead_table.set_text(0, 2, "WIN/LOSE", 24)

	for i in range(1, 6):
		lead_table.set_color(i, 0, list_char[i - 1].color)
		lead_table.set_text(i, 0, list_char[i - 1].name)

		lead_table.set_color(i, 1, list_char[i - 1].color)
		lead_table.set_text(i, 1, list_char[i - 1].time)

		lead_table.set_color(i, 2, list_char[i - 1].color)
		lead_table.set_text(i, 2, str(list_char[i - 1].win) + "/" + str(list_char[i - 1].lose))

	lead_table.update()

	lead_btn = button.Button("BACK TO MAIN MENU", 0, -200, lead_btn_callback)
	lead_btn.use_enter()

	show_piechart()


def show_piechart():
	try:
		labels = list_char[0].name, list_char[1].name, list_char[2].name, list_char[3].name, list_char[4].name
		sizes1 = [list_char[0].win, list_char[1].win, list_char[2].win, list_char[3].win, list_char[4].win]
		sizes2 = [list_char[0].lose, list_char[1].lose, list_char[2].lose, list_char[3].lose, list_char[4].lose]
		explode = (0, 0, 0.1, 0, 0)
		fig1, ax1 = plt.subplots()
		fig2, ax2 = plt.subplots()
		ax1.pie(sizes1, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
		ax1.axis("equal")
		ax2.pie(sizes2, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
		ax2.axis("equal")
		plt.show()
	except:
		pass
