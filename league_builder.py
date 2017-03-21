import csv
import random

# Making the file a constant
FILE = 'soccer_players.csv'

def get_players():

	with open(FILE, newline='') as csvfile:

		# Get an iterator from the csv file
		reader = csv.DictReader(csvfile, delimiter=',')

		#Convert it to a list for ease of use
		players = list(reader)	

		# Generating the list for separate the experienced players from the new ones
		experienced_players = []
		new_players 		= []

		# Sampling the complete list shuffles the list, probably there's a better way but i'm trying to stick
		# and be creative with the things the course covered by now

		for player in random.sample(players,18):
			
			player_experience = (player['Soccer Experience'] == 'YES')

			if player_experience:
				experienced_players.append(player)
			else:
				new_players.append(player)

	return (experienced_players,new_players)

# This function generates the file with the teams and players, and also calls the welcome_letter function for each player in each team
# In this i decided to catch every parameter as all of them are dicts
def roaster_teams(dragons, sharks, raptors):

	with open('teams.txt','w') as file:

		# Create a dict to join all the teams and their details
		teams = {
			'dragons' : { 
					'players' 			  : dragons, 
					'team_name'			  : 'Dragons', 
					'date_first_practice' : 'March 30 at 9:00 am'
			},
			'sharks' : { 
					'players' 			  : sharks, 
					'team_name'			  : 'Sharks', 
					'date_first_practice' : 'March 31 at 10:00 am'
			},
			'raptors' : { 
					'players' 			  : raptors, 
					'team_name'			  : 'Raptoprs', 
					'date_first_practice' : 'April 1 at 11:00 am'
			},
		}

		# Breaking the tuple that returns .items for the dict and assigning them to two new variables
		for index, val in teams.items():

			# Adds the team name before looping and writing the player details
			file.write('// ' + val['team_name'])

			for player in val['players']:

				# Creating a dict for more clear string format
				player_data = {
					'name'        : player['Name'],
					'experience'  : player['Soccer Experience'],
					'guardian(s)' : player['Guardian Name(s)']
				}

				file.write("\n\t{name}, {experience}, {guardian(s)}".format(**player_data))

				# Generates the welcome letter for the guardians of the player
				welcome_letters(player = player, team_name = val['team_name'], date_first_practice =  val['date_first_practice'])

			# Adds some space before each team and it's players to make the file more readable
			file.write('\n\n')

#
# Catch the player data alone as it already is a dict		
def welcome_letters(player = None, **kwargs):

	# Lowercase and split the player name by the space to join it later and create the file name for the welcome letter to the player guardian(s)
	file_name = player['Name'].lower().split()
	file_name = '_'.join(file_name) + '.txt'

	# Make the content of the letter a dictionary to make the format more clear
	letter_content = {
		'team_name'			  : kwargs['team_name'],
		'guardian_names'      : player['Guardian Name(s)'],
		'player_name'	 	  : player['Name'],
		'date_first_practice' : kwargs['date_first_practice']
	}

	# Here is the creation of the welcome letter file
	with open(file_name,'w') as file:
		file.write('''Dear {guardian_names}, it's a pleasure to us let you know {player_name} has been accepted to be part of the {team_name} team, the date and time for the first practice is {date_first_practice}. We are looking forward to see you there. \n\nBryan, CEO of the {team_name} team.'''.format(**letter_content))


# Make sure the script doesn't execute when imported
# All of your logic and function should be called if __name__ == "__main__": block.
if __name__ == '__main__':

	# Getting the players
	experienced_players, new_players = get_players()

	# Make the lists for the teams
	dragons = []
	sharks  = []
	raptors = []

	# Extend the team with players data
	# There are 18 players, so each team should have 6 players, 3 of them experienced and 3 of them newbies
	# As we received the players separated and shuffled from the get_players() function, we are using slices to assing players to each team

	dragons.extend(experienced_players[0:3])
	dragons.extend(new_players[0:3])

	sharks.extend(experienced_players[3:6])
	sharks.extend(new_players[3:6])

	raptors.extend(experienced_players[6:9])
	raptors.extend(new_players[6:9])

	# Here the file with the teams and players is generated
	roaster_teams(dragons, sharks, raptors)

















