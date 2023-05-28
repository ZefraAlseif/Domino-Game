import random


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
            print("Temp Domino: "+temp_domino)
            print("Table lft: "+table_lft[0])
            print("Table right: "+table_rht[-1])
            if temp_domino.find(table_lft[0]) != -1 or temp_domino.find(table_rht[-1]) != -1:
                check = True
                break
        return check     
    
    # Check if the move made is a valid move via domino rules
    def valid_move(table,chosen_dominom,chosen_side):
        
        pass
    # Making a move (Player Move)
    def make_move(player_dominos,current_turn,table):
        print("Current Table: \n", table)
        chosen_domino = input(f"Choose Domino (Ex. 1-2): {player_dominos[current_turn][1:]}\n")
        chosen_side = input("Choose which side (Left or Right *Beginning does not Matter): \n")
        player_dominos[current_turn].remove(chosen_domino)
        return chosen_domino,chosen_side
    # Update the playing table with the most recent move
    def update_table(table,chosen_domino,chosen_side):
        if chosen_side == "Left" or table == []:
            table.insert(0,chosen_domino)
        else:
            table.insert(len(table),chosen_domino)
    # Temporary game run
    table = []
    sp = build_pile()  # starting pile reference
    print(sp)
    ap = players(random.randint(2, 4))  # active player reference
    print(ap)
    pd = pick_dominos(sp, ap)  # each player dominos reference
    turn = 0
    print(pd)
    cm = True
    count = 0;
    while (count < 4):
        if table != []:
            check_move = can_move(pd,turn,table)
        else:
            check_move = True 
        if check_move:       
            chosen_domino, chosen_side = make_move(pd,turn,table)
            update_table(table,chosen_domino,chosen_side)
            turn = next_turn(turn)
            count = 0
        else: 
            print("Skipped turn of: ",pd[turn][0])
            turn = next_turn(turn)
            count +=1
            
        
        
