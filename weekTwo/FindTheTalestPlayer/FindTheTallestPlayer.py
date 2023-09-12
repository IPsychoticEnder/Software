players = {}
max_height = 0
tallest_player = ""

for i in range(3):
    player_name = input("What is your name: ")
    player_height = input("What is your height: ")
    players[player_name] = int(player_height)

for player_name, player_height in players.items():
    if player_height > max_height:
        tallest_player = player_name
        max_height = player_height

print(f"The tallest player is: {tallest_player} with a height of {max_height}")
