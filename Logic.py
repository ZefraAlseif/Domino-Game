import random
# Self into all methods to be made accesible by other classes
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
        return active_players

    """
    Things that need to be added i.e(Version 1)
    """
    def next_turn(turn):
        if turn < 3:
            turn += 1
        else:
            turn = 0
        return turn

    # Check if Player has a domino that can be played:
    def can_move(player_dominos, current_turn, table):
        check = False
        table_lft = table[0]
        table_rht = table[-1]
        for i in range(1, len(player_dominos[current_turn])):
            temp_domino = player_dominos[current_turn][i]
            #print("Temp Domino: "+temp_domino)
            #print("Table lft: "+table_lft[0])
            #print("Table right: "+table_rht[-1])
            if temp_domino.find(table_lft[0]) != -1 or temp_domino.find(table_rht[-1]) != -1:
                check = True
                break
        return check

    # Check if the move made is a valid move via domino rules
    """def valid_move(table, chosen_domino, chosen_side):
        if table == [] and chosen_domino == "F":
            return "F", "F"
        elif table == [] and chosen_domino != "F":
            return chosen_domino, chosen_side
        elif chosen_side == "L" and chosen_domino[-1] == table[0][0]:
            return chosen_domino, chosen_side
        elif chosen_side == "L" and chosen_domino[0] == table[0][0]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            return chosen_domino, chosen_side
        elif chosen_side == "R" and chosen_domino[0] == table[-1][-1]:
            return chosen_domino, chosen_side
        elif chosen_side == "R" and chosen_domino[-1] == table[-1][-1]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            return chosen_domino, chosen_side
        else:
            return "F", "F"
    """

    # Making a move (Player Move)
    def make_move(player_dominos, current_turn, table):
        print("Current Table: \n", table)
        # Before choosing a domino determine if the player is a human or a computer
        if player_dominos[current_turn][0] != (f"Computer Player {current_turn+1}"):
            chosen_domino = input(f"Choose Domino (Ex. 1-2): {player_dominos[current_turn][1:]}\n")
            #chosen_side = input("Choose which side (L or R *Beginning does not Matter): \n")
            #chosen_side = chosen_side.capitalize()
        else:
            for i in range(1, len(player_dominos[current_turn])):
                temp_domino = player_dominos[current_turn][i]
                #print("Temp Domino: "+temp_domino)
                #print("Table lft: "+table_lft[0])
                #print("Table right: "+table_rht[-1])
                if table == []:
                    chosen_domino = temp_domino
                    break
                elif (temp_domino.find(table[0][0]) != -1 or temp_domino.find(table[-1][-1]) != -1):
                    chosen_domino = temp_domino
                    break
        if (player_dominos[current_turn].count(chosen_domino) != 1):
            chosen_domino = "F"
        return chosen_domino #chosen_side

    # Update the playing table with the most recent move
    def update_table(table, chosen_domino, chosen_side):
        if chosen_side == "L" or table == []:
            table.insert(0, chosen_domino)
        else:
            table.insert(len(table), chosen_domino)

    # Determine the score the winning player gets (this is for much later)
    def score(player_dominos,turn):
        points = 0
        del player_dominos[turn]
        for i in range(3):
            for dom in range(1,len(player_dominos[i])):
                temp_dom = player_dominos[i][dom]
                points += int(temp_dom[0]) + int(temp_dom[-1])
        return points

    # Check the winner when no-one can play anymore
    def check_winner(player_dominos):
        """
        player_dominos = [
            [player_dominos[0][1:]],
            [player_dominos[1][1:]],
            [player_dominos[2][1:]],
            [player_dominos[3][1:]]
        ] """
        sum = 1000;
        count = 0;
        for i in range(4):
            temp_sum = 0;
            temp_count= i;
            for dom in range(1,len(player_dominos[i])):
                temp_dom = player_dominos[i][dom]
                temp_sum += int(temp_dom[0]) + int(temp_dom[-1])
            if (temp_sum < sum):
                sum = temp_sum
                count = temp_count
        return count

    """
    Things needed to improve functionality of game (i.e Version 2)
    """
    # Use def valid_move to improve the functionality
    def valid_move2(table, chosen_domino,player):
        # Two conditions: Play in both sides or Only one side
        # Table is empty condition
        if table == [] and chosen_domino == "F":
            return chosen_domino, "F"
        elif table == [] and chosen_domino != "F":
            return chosen_domino, "L" 
        # Play in both sides
        elif chosen_domino[-1] == table[0][0] and chosen_domino[0] == table[-1][-1]:
            if player != (f"Computer Player {player[-1]}"):
                chosen_side = input("Choose which side (L or R *Beginning does not Matter): \n")
                chosen_side = chosen_side.capitalize()
                return chosen_domino, chosen_side
            else:
                print("Test Achieved")
                chosen_side = random.choice(["L","R"])
                return chosen_domino, chosen_side
        elif chosen_domino[0] == table[0][0] and chosen_domino[-1] == table[-1][-1]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            if player != (f"Computer Player {player[-1]}"):
                chosen_side = input("Choose which side (L or R *Beginning does not Matter): \n")
                return chosen_domino, chosen_side
            else:
                print("Test Achieved")
                chosen_side = random.choice(["L","R"])
                return chosen_domino, chosen_side
        # Can only be played on one side or both ends are the same
        elif chosen_domino[-1] == table[0][0]:
            return chosen_domino, "L"
        elif chosen_domino[0] == table[0][0]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            return chosen_domino, "L"
        elif chosen_domino[0] == table[-1][-1]:
            return chosen_domino, "R"
        elif chosen_domino[-1] == table[-1][-1]:
            chosen_domino = str(chosen_domino[-1]+"-"+chosen_domino[0])
            return chosen_domino, "R"
        # In case none of the conditions are met
        else:
            return "F", "F"  
    
    # *Temporary game run
    
    #table = []
    #sp = build_pile()  # starting pile reference
    # print(sp)
    ap = players(2) #random.randint(2, 4))  # active player reference
    player_scores= {f"{ap[0][0]} score":0,
                    f"{ap[1][0]} score":0,
                    f"{ap[2][0]} score":0,
                    f"{ap[3][0]} score":0,}
    print(player_scores)
    #pd = pick_dominos(sp, ap)  # each player dominos reference
    turn = 0  # Starting player turn
    # print(pd)
    count = 0  # Determine how many players where skipped
    game_over = False  # Determines when the game ends
    winner = ""  # Stores the player that has Won
    sc = 0  # How many points does the winning player obtain
    # (count < 4 or (len(pd[0]) or len(pd[1]) or len(pd[2]) or len(pd[3])) == 1):
    winner = ap[3][0]
    while(player_scores[f"{winner} score"] < 100):
        table = []
        ap = players(2)
        sp = build_pile()  # starting pile reference
        pd = pick_dominos(sp, ap)  # each player dominos reference
        game_over = False  # Determines when the game ends
        winner = ""  # Stores the player that has Won
        sc = 0  # How many points does the winning player obtain
        count = 0
        while (game_over == False):
            if table != []:  # Check if the game is not at the starting position
                # Check if the player can make a move
                check_move = can_move(pd, turn, table)
            else:
                check_move = True
            if check_move and table == []:
                # Allow the user to choose the domino
                chosen_domino = make_move(pd, turn, table)
                correct_domino, correct_side = valid_move2(table, chosen_domino,pd[turn][0])  # Check if the move is valid
                if correct_domino and correct_side != "F":  # If the move is valid perform block
                    # Remove domino the players hand
                    pd[turn].remove(chosen_domino)
                    # Update the table
                    update_table(table, correct_domino, correct_side)
                    turn = next_turn(turn)  # Go to the next turn
                    count = 0  # Counter of people skipped
                else:
                    # Invalid move was made
                    print(f"Wrong move and side combination please try again: ")
            elif check_move:
                # Allow the user to choose the domino
                chosen_domino = make_move(pd, turn, table)
                correct_domino, correct_side = valid_move2(table, chosen_domino,pd[turn][0])  # Check if the move is valid
                if correct_domino and correct_side != "F":  # If the move is valid perform block
                    # Remove domino the players hand
                    pd[turn].remove(chosen_domino)
                    # Update the table
                    update_table(table, correct_domino, correct_side)
                    turn = next_turn(turn)  # Go to the next turn
                    count = 0  # Counter of people skipped
                else:
                    # Invalid move was made
                    print(f"Wrong move and side combination please try again: ")
            else:
                print("Skipped turn of: ", pd[turn][0])
                turn = next_turn(turn)
                count += 1
            if (count == 4):  # Checks the condition that the count is equal to 4 and ends the game
                game_over = True
                turn = check_winner(pd)
                winner = pd[turn][0]
            # Checks the condition that a player does not have any more pieces
            elif (pd[turn][-1] == pd[turn][0]):
                game_over = True
                winner = pd[turn][0]
        sc = score(pd,turn) / 2
        player_scores[f"{winner} score"] += int(sc) 
        print(player_scores)
        print(f"The winner is {winner} and got {sc} points")
        print("Turn: ",turn)  
    
     