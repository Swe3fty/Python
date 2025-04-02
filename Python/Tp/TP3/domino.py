#===============Create a list of dominoes================
#return : a liste of tuples of dominoes
def make_dominoes():
    dominoes = []
    for i in range(7):
        for j in range(i,7): #(start, stop) to i, j to avoid duplicates like (2,3) and (3,2)
            dominoes.append((i, j))
    return dominoes

#===============For a deck given, we take a random dominoes================
#dominoes taken are removed from the deck (pioche)
#param dominoes_stack : list of tuples represent the deck (pioche)
#param nb_dominoes : number of dominoes to take
#return : list of dominoes taken

def take_dominoes(dominoes_stack, nb_dominoes):
    import random
    if dominoes_stack == [] or nb_dominoes == 0:
        return []
    dominoes_taken = []
    for i in range(nb_dominoes):
        domino = random.choice(dominoes_stack)
        dominoes_stack.remove(domino)
        dominoes_taken.append(domino)
    return dominoes_taken

#===============Give dominoes to players================
#param game_date : dictionnary that contains the game data
#param dominoes : list of tuples that represent the dominoes to give to a player
#param player_id : string that has the id of the player

def give_dominoes(game_data, dominoes, player_id):
    game_data['players'][player_id] += dominoes
    return game_data

#===============Put the dominoes in the deck and give 6 dominoes to each player======#
#Call function make_dominoes, take_dominoes and give_dominoes
#param : game_data : a dictionnary that contain information on the game, it is modified in this function
def init_game(game_data):
    dominoes_deck = make_dominoes()
    dominoes_taken1 = take_dominoes(dominoes_deck,6)
    dominoes_taken2 = take_dominoes(dominoes_deck,6)
    game_data['stack'] = dominoes_deck[:]  # Initialize the stack with all dominoes
    give_dominoes(game_data, dominoes_taken1, 'p1')
    give_dominoes(game_data, dominoes_taken2, 'p2')
    

#==============Show the informations of dominoes the player has===========#
#param game_data : dictionnary that contain information on the game
#param player_id : id of the player
def display_dominoes(game_data, player_id):
    print("***Player", player_id)
    print(game_data['players'][player_id])

#==============Show the state of the board================================#
def display_board(game_data):
    print("*** Board")
    print(game_data['board'])

#=============Show the state of the deck============#
def display_stack(game_data):
    print("***Stack status : 16 elements***")
    print(game_data['stack'])

#=============Permits to know if the domino can be placed on the board for a given position===========#
#param board_dominoes
#param position ('r' or 'l') of the domino the place on the board
#return True if we can place else False
def is_domino_possible(board_dominoes, domino, position):
    inverted_domino = (domino[1],domino[0])
    result1 = 0
    result2 = 1
    if (board_dominoes== []):
        return True
    if position == 'r':
        result1 = board_dominoes[-1][1] == domino[0] #result = board_dominoes[-1][1] in domino and return result is the same 
        result2 = board_dominoes[-1][1] == inverted_domino[0]
        if(result1 == True):
            return True
        else :
            return True
        
    elif position == 'l':
        result1 = board_dominoes[0][0] == domino[1]
        result2 = board_dominoes[0][0] == inverted_domino[0]
    return False

#==============Place the domino on the board of it's possible=========#
#uses is_domino_possible
#return true or false if the domino can be placed
def put_domino_on_board(board_dominoes, domino, position):
    result = is_domino_possible(board_dominoes, domino, position)
    inverted_domino = (domino[1],domino[0])
    if result == False:
        return False
    elif position == 'r':
        board_dominoes.append(domino)
    elif position == 'l':
        board_dominoes.insert(0,domino)
    return True

#===============Test of the program================#
def tests():
    dominoes_stack = make_dominoes()
    assert len(dominoes_stack) == 28    

    assert len(dominoes_stack) == len(set(dominoes_stack)) #no duplicates

    dominoes_taken = take_dominoes(dominoes_stack, 2)
    assert len(dominoes_taken) == 2
    assert len(dominoes_taken[0]) == 2 and len(dominoes_taken[1]) == 2
    assert len(dominoes_stack) == 26

    #Limit case, no dominoes in the deck
    dominoes_stack = []
    assert take_dominoes(dominoes_stack, 1) == []

    game_data = {
        'players': {
            'p1': [],
            'p2': []
        },
        'board': [],
        'stack': []
    }
    give_dominoes(game_data, [(1,2), (2,3)], 'p1')
    assert game_data['players']['p1'] == [(1,2), (2,3)]
    assert game_data['players']['p2'] == []
    give_dominoes(game_data, [(2,6)], 'p1')
    assert game_data['players']['p1'] == [(1,2), (2,3), (2,6)]

    print("*******All tests passed*******")
#=================================================#
def main():
    game_data = {
        'players' : {
            'p1' : [],
            'p2' : []  
        },
        'board' : [],
        'stack' : []
    } 
    init_game(game_data)
    display_stack(game_data)
    display_dominoes(game_data, 'p1')
    display_dominoes(game_data, 'p2')
    display_board(game_data) #the board has to be empty    

#==================================================#
def test_unitaires():
    assert is_domino_possible([], (1,1),'abcd')
    assert is_domino_possible([], (1,1),'r')
    assert is_domino_possible([], (1,1),'l')
    assert is_domino_possible([(1,2),(2,2),(2,4)],(3,1),'l') 
    assert is_domino_possible([(1,2),(2,2),(2,4)],(1,3),'l')
    assert not is_domino_possible([(1,2),(2,2),(2,4)],(4,3),'l')
    assert is_domino_possible([(1,2),(2,2),(2,4)],(1,4),'r')
    assert is_domino_possible([(1,2),(2,2),(2,4)],(4,1),'r')
    assert not is_domino_possible([(1,2),(2,2),(2,4)],(1,3),'r')
    
    board = []
    assert put_domino_on_board(board, (1,1), 'r')
    assert board == [(1,1)]
    board = [(1,3)]
    assert not put_domino_on_board(board, (1,1), 'r')
    board = [(1,3)]
    assert put_domino_on_board(board, (2,1), 'l')
    assert board == [(2,1),(1,3)]
    board = [(1,3)]
    assert put_domino_on_board(board, (1,2), 'l')
    assert board == [(2,1),(1,3)]


tests()
main()
test_unitaires()