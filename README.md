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
 
