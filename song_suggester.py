import random

def get_suggestion(song_list):
	rand = random.randint(0, len(song_list) - 1)
	return song_list[rand]
