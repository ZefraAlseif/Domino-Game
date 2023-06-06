Domino Game will allow players to play the board game of the same name: for this project the pieces available will range from double-0 to double-9

# Main Class: {Run the game}

# Logic Class: {Game actions and Game Logic}
`def players(number_players):`
   - Takes the information regarding the number of active players and produces the number of human players that will be playing the game.
   - In addition it also provides the remainding players as computers in order to make sure that every game is comproside of 4 total players.

`def build_pile():`
   - It builds a list that acts as the pile of dominos on the table.
   - The function has a shuffle in order to make sure every pile at is randomized before the players select their dominos.

`def pick_dominos(start_pile,active_players):`
   - The list containing each player will be appended in order that each player receives 10 pieces each.

`def next_turn(turn):`
   - It determines the order of the players going from Player 1 to Player 4

`def make_move(player_dominos,current_turn,table):`
   - It makes a move by first displaying the current table or status of the game
   - It than displays the dominos available to the corresponding player and allows the player to choose which domino to play
   - Lastly it removes the chosen domino from the list and returns the domino that was chosen and then location where the domino will be played

`def update_table(table,chosen_domino,chosen_side):`
   - Updates the corresponding table or status of the game by inserting the chosen_domino in the side that it was chosen.

`def can_move(player_dominos,current_turn,table):`
   - It checks that the player has piece that can be played
   - The function accomplishes this by looking into the last and first piece in the table 

`def valid_move(table,chosen_domino,chosen_side):` [Version-1]
   - This function checks that the move that the individual played is a valid move
   - It does this by taking into account the chosen side and chosen domino match the table value

`def score(player_dominos,turn):`
   - This function takes the last turn and all of the remainding dominos
   - It then removes the winning player from the list and adds up the points from each player

`def check_winner(player_dominos):`
   - This function activates when the game ends via the condition that no player can make a move
   - The function takes all of the players and their corresponding dominos to perform a check to see which player has the least amount of points.

`def valid_move2(table,chosen_domino):` [Version-2]
   - This function checks that the move that the individual played is a valid move
   - Different from Version 1 the function now determines which side the domino will go to without rquiring the users input.

 # Things that need to be added: (Version-1)
> Match the dominos played i.e '2-3' '3-4' not '2-3' '4-3' [Completed]

> Check if any of the dominos the current player has is playable [Completed]

> Check if the domino and side the player chose equate to a correct value [Completed]

> End the game when no player has a domino to play or someone has ran out of dominos [Completed]
# Things needed to improve functionality of game (Version-2)
> Add a function that determines where the domino the user chose has to be played. Hence no need to input the side that the user wants to play. However, when the domino can be played in both sides ask the user will be asked which side he would like to play [Completed]

> Add an AI function in order to make sure that the computer is capable of making moves on its own. For this case only focus on adding the functionality, later will try to introduce machine learning to make the AI more formidable [Completed]

> Introduce the ability to play until the winning player has reached a score of 100, this means that there must be a score keeper for each player in the game [Pending]

> Introduce two game modes, solo play and team play. Solo play is the first iteration of the game and team play will allow for score to be shared between teams [Pending]




