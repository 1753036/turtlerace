import os.path

player_name = ""
player_class = ""
player_color = ""
player_score = 0

road_width = 800
road_height = 500

def load():
	global player_name
	global road_width
	global road_height

	if os.path.isfile("settings.cfg"):
		file = open("settings.cfg", "r")

		player_name = file.readline()[:-1]
		road_width = int(file.readline())
		road_height = int(file.readline())
		file.close()

def save():
	global player_name
	global road_width
	global road_height
	
	file = open("settings.cfg", "w")
	file.write(str(player_name) + "\n")
	file.write(str(road_width) + "\n")
	file.write(str(road_height))



	
