tab = [ 0, 0, 0,
        0, 0, 0,
        0, 0, 0]
	
# player 1: player = 1
# player 2: player = -1
player = 1

# winning combinations
win = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

# checks if one player won, if there are empty cells or if it's draw 
def gameState(tab):
	for i in win:
		if tab[i[0]] == 1 and tab[i[1]] == 1 and tab[i[2]] == 1:
			return 1
		if tab[i[0]] == -1 and tab[i[1]] == -1 and tab[i[2]] == -1:
			return -1
	draw = True
	for i in tab:
		if i == 0:
			draw = False
	if draw:
		return 0
	return -2
	
# recursive method to check possibility branches
def search(tab, player, t):
	#if t < 5:
		#print("\t"*t + "tab: " + str(tab))
	state = gameState(tab)
	if state != -2:
		#if t < 5:
			#print("\t"*t + "endState: " + str(state))
		return (state*player, -1)
		
	# list_best[0] contains best result and list_best[1:] moves to get this result
	list_best = [-2]
	for cell in range(len(tab)):
		if tab[cell] == 0:
			tab[cell] = player
			
			# val is best value found by one child call
			val = -search(tab, - player, t + 1)[0]
			
			if val > list_best[0]:
				list_best = [val, cell]
			elif val == list_best[0]:
				list_best.append(cell)
			
			# reset tab
			tab[cell] = 0
	#if t < 5:
		#print("\t"*t + "list_best: " + str(list_best))
	return list_best
	
# Start the recursive loop
res = search(tab, player, 0)

# See who won: res[0] == -1 means starting player lost, not player 1 lost
winner = res[0]*player

# Print output
if player == 1:
	print("Player 1 start.")
elif player == -1:
	print("Player 2 start.")

if winner == 0:
	print("It's a draw !")
else:
	# winner_number does 1 -> 1 and -1 -> 2
	winner_number = int(winner*-0.5 + 1.5)
	print("Player " + str(winner_number) + " wins !")

# Where you can play is displayed as numbers corresponding to this:
#|1|2|3|
#|4|5|6|
#|7|8|9|

str_poss = str(res[1] + 1)
for i in range(2, len(res)):
	str_poss += ", " + str(res[i] + 1)
if (winner != -player):
	print("You can play " + str_poss)
	
