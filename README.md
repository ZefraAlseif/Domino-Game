Domino Game will allow players to play the board game of the same name: for this project the pieces available will range from double-0 to double-9

- Main Class: {Run the game}

- Logic Class: {Game actions and Game Logic}
    # def players(number_players):
    - Takes the information regarding the number of active players and produces the number of human players that will be playing the game.
    - In addition it also provides the remainding players as computers in order to make sure that every game is comproside of 4 total players.
    # def build_pile():
    - It builds a list that acts as the pile of dominos on the table.
    - The function has a shuffle in order to make sure every pile at is randomized before the players select their dominos.
    # def pick_dominos(start_pile,active_players):
    - The list containing each player will be appended in order that each player receives 10 pieces each.
    # def next_turn(turn):
    - It determines the order of the players going from Player 1 to Player 4
    # def make_move(player_dominos,current_turn,table):
    - It makes a move by first displaying the current table or status of the game
    - It than displays the dominos available to the corresponding player and allows the player to choose which domino to play
    - Lastly it removes the chosen domino from the list and returns the domino that was chosen and then location where the domino will be played
    # def update_table(table,chosen_domino,chosen_side):
    - Updates the corresponding table or status of the game by inserting the chosen_domino in the side that it was chosen.

 * Things that need to be added:
    > (0) Match the dominos played i.e '2-3' '3-4' not '2-3' '4-3' [Completed]
    > (1) Check if any of the dominos the current player has is playable [Completed]
    > (2) Check if the domino and side the player chose equate to a correct value [Completed]
    > (3) End the game when no player has a domino to play or someone has ran out of dominos [Pending]


