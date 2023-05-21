import random
class Logic:
    
    def __init__(number_players) -> None:
        active_players = []
        for i in range(1,number_players):
            active_players.append([f'Player {i}'])
        for i in range(4-number_players,4):
            active_players.append([f'Computer Player {i}'])
        return active_players
    
    # Builds the starting pile & randomizes it
    def build_pile():
        start_pile = []
        for i in range(0,10): # 6 set range to range(0,7)
            for j in range (i,10): # 6 set range to range(i,7)
                start_pile.append(f'{i}-{j}')
        random.shuffle(start_pile)
        return start_pile
    
    # Pick the dominos for each player
    def pick_dominos(start_pile,active_players):
        for i in active_players:
            for j in range(0,10):
                temp_domino = start_pile.pop()
                i.append(temp_domino)
        return active_players
    
    def make_move():
        
        pass
    
    sp = build_pile()
    print(sp)
    ap = __init__(random.randint(1,4))
    print(ap)
    print(pick_dominos(sp,ap))
    

