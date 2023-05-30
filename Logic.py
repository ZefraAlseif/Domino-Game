import random

## Self into all methods to be made accesible by other classes
class Logic:
    # Builds the number of players list (Human Players & Computer players) total of 4
    def players(number_players):
        active_players = []
        for i in range(1, number_players):
            active_players.append([f"Player {i}"])
        for i in range(number_players, 5):
            active_players.append([f"Computer Player {i}"])
        return active_players

    # Builds the starting pile & randomizes it
    def build_pile():
        start_pile = []
        for i in range(0, 10):  # 6 set range to range(0,7)
            for j in range(i, 10):  # 6 set range to range(i,7)
                start_pile.append(f"{i}-{j}")
        random.shuffle(start_pile)
        return start_pile

    # Pick the dominos for each player
    def pick_dominos(start_pile, active_players):
        for i in active_players:
            for j in range(0, 10):
                temp_domino = start_pile.pop()
                i.append(temp_domino)
        """dict_players = {
            active_players[0][0]: active_players[0][1:],
            active_players[1][0]: active_players[1][1:],
            active_players[2][0]: active_players[2][1:],
            active_players[3][0]: active_players[3][1:],
        }"""
        return active_players

    """
    For now the game will start with Player 1 and will progress towards the last player on the list and the loop again.
    """
    def next_turn(turn):
        if turn < 3:
            turn += 1
        else:
            turn = 0 
        return turn
    
    # Check if Player has a domino that can be played:
    def can_move(player_dominos,current_turn,table):
        check = False
        table_lft = table[0]
        table_rht = table[-1]
        for i in range (1,len(player_dominos[current_turn])):
            temp_domino = player_dominos[current_turn][i]
            #print("Temp Domino: "+temp_domino)
            #print("Table lft: "+table_lft[0])
            #print("Table right: "+table_rht[-1])
            if temp_domino.find(table_lft[0]) != -1 or temp_domino.find(table_rht[-1]) != -1:
                check = True
                break
        return check     

    # Check if the move made is a valid move via domino rules
    def valid_move(table,chosen_domino,chosen_side):
        if table == [] and chosen_domino  == "F":
            return "F","F"
        elif table == [] and chosen_domino != "F":
            return chosen_domino, chosen_side
        elif chosen_side == "L" and chosen_domino[-1] == table[0][0]:
            return chosen_domino, chosen_side
        elif chosen_side == "L" and chosen_domino[0] == table[0][0]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            return chosen_domino,chosen_side
        elif chosen_side == "R" and chosen_domino[0] == table[-1][-1]:
            return chosen_domino, chosen_side
        elif chosen_side == "R" and chosen_domino[-1] == table[-1][-1]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            return chosen_domino, chosen_side
        else:
            return "F","F"
    
    # Making a move (Player Move)
    def make_move(player_dominos,current_turn,table):
        print("Current Table: \n", table)
        chosen_domino = input(f"Choose Domino (Ex. 1-2): {player_dominos[current_turn][1:]}\n")
        chosen_side = input("Choose which side (L or R *Beginning does not Matter): \n")
        chosen_side = chosen_side.capitalize()
        if (player_dominos[current_turn].count(chosen_domino) !=1):
            chosen_domino = "F"
        return chosen_domino,chosen_side
    
    # Update the playing table with the most recent move
    def update_table(table,chosen_domino,chosen_side):
        if chosen_side == "L" or table == []:
            table.insert(0,chosen_domino)
        else:
            table.insert(len(table),chosen_domino)
    
    # Determine winner and their score (this is for much later)
    def score(player_dominos):
        for i in range (1,len(player_dominos[0])):
            pass
    pass
        
    # *Temporary game run 
    table = []
    sp = build_pile()  # starting pile reference
    #print(sp)
    ap = players(random.randint(2, 4))  # active player reference
    #print(ap)
    pd = pick_dominos(sp, ap)  # each player dominos reference
    turn = 0 # Starting player turn
    #print(pd)
    count = 0; # Determine how many players where skipped
    while (count < 4 or (len(pd[0]) or len(pd[1]) or len(pd[2]) or len(pd[3])) == 1):
        if table != []: # Check if the game is not at the starting position
            check_move = can_move(pd,turn,table) # Check if the player can make a move
        else:
            check_move = True 
        if check_move and table == []:       
            chosen_domino, chosen_side = make_move(pd,turn,table) # Allow the user to choose the domino
            correct_domino, correct_side = valid_move(table,chosen_domino,chosen_side) # Check if the move is valid
            if correct_domino and correct_side != "F": # If the move is valid perform block
                pd[turn].remove(chosen_domino) # Remove domino the players hand
                update_table(table,correct_domino,correct_side) # Update the table
                turn = next_turn(turn) # Go to the next turn
                count = 0 # Counter of people skipped 
            else:
                # Invalid move was made
                print(f"Wrong move and side combination please try again: ") 
        elif check_move:
            chosen_domino, chosen_side = make_move(pd,turn,table) # Allow the user to choose the domino
            correct_domino, correct_side = valid_move(table,chosen_domino,chosen_side) # Check if the move is valid
            if correct_domino and correct_side != "F": # If the move is valid perform block
                pd[turn].remove(chosen_domino) # Remove domino the players hand
                update_table(table,correct_domino,correct_side) # Update the table
                turn = next_turn(turn) # Go to the next turn
                count = 0 # Counter of people skipped 
            else:
                 # Invalid move was made
                print(f"Wrong move and side combination please try again: ") 
        else: 
            print("Skipped turn of: ",pd[turn][0])
            turn = next_turn(turn)
            count +=1
     
            
        
        
