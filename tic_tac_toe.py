while True:  
    ###### INITIAL CONDITIONS

    # player characters
    players = [' ', ' ']

    # vertical win conditions
    x1 = [0,0,0]
    x2 = [0,0,0]

    # horizontal win conditions
    y1 = [0,0,0]
    y2 = [0,0,0]

    # player 1 diagonal win conditions
    player1diag1 = [(0,0), (1,1), (2,2)]
    player1diag2 = [(0,2), (1,1), (2,0)]

    # player 2 diagonal win conditions
    player2diag1 = [(0,0), (1,1), (2,2)]
    player2diag2 = [(0,2), (1,1), (2,0)]

    # open spots on board
    free_spots = [0,1,2,3,4,5,6,7,8]

    # spots on board
    # use list comprehension
    db = [str(i) for i in range(1,10)]

    # coordinates of spots
    coords = [(0,2),(1,2),(2,2),(0,1),(1,1),(2,1),(0,0),(1,0),(2,0)]

    # the board
    board = '_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_'
    # "unpack" the contents of db as parameters leveraging the variadic nature of `str.format`
    current_board = board.format(*db)


    ######## GET READY TO PLAY

    print('WERLCOME TO TERK TWERK 2!')
    print(current_board)

    # player 1 set up
    players[0] = input('Player 1, choose yer symbol:')
    
    # prep for player 2 to make a different selection
    players[1] = players[0]

    # player 2 set up
    while players[0] == players[1]:
        p2 = input('Player 2, pick a differnt symbol then Player 1 okey?')
        if p2 != players[0]:
            players[1] = p2

    print(current_board)


    ######## THE GAME

    playing_game = True
    # give the while condition a more meaningful name, change it's value instead of breaking
    while playing_game:
        ## Player 1
        # only proceed if input is usable
        choice = 9
        while choice not in free_spots:
            choice_string = input('Player 1! Pick yer numbered spot.')
            while not choice_string.isnumeric():
                print('Pick a number...')
                choice_string = input()
            choice = int(choice_string) - 1

        # put player 1's symbol in place
        db[choice] = players[0]
        current_board = board.format(db[0], db[1], db[2], db[3], db[4], db[5], db[6], db[7], db[8])
        print(current_board)

        # remove input from free spots    
        free_spots.remove(choice)
        
        # prep for vertical win
        xwin = False
        x1[coords[choice][0]] += 1
        
        # prep for horizontal win
        ywin = False
        y1[coords[choice][1]] += 1

        # prep for diagonal win
        diagwin = False
        if coords[choice] in player1diag1:
            player1diag1.remove(coords[choice])
        if coords[choice] in player1diag2:
            player1diag2.remove(coords[choice])

        # see if it was a winning move        
        for x in x1:
            if x == 3:
                xwin = True
        for y in y1:
            if y == 3:
                ywin = True
        if player1diag1 == [] or player1diag2 == []:
            diagwin = True
        if xwin or ywin or diagwin:
            print("Player 1 wins!")
            playing_game = False
        if free_spots == []:
            print("Ert's a tie!")
            playing_game = False


        ## Player 2 goes
        # only proceed if input is usable
        while choice not in free_spots:
            choice_string = input('Player 2! Pick yer numbered spot.')
            while not choice_string.isnumeric():
                print('Pick a number...')
                choice_string = input()
            choice = int(choice_string) - 1

        # put player 2's symbol in place
        db[choice] = players[1]
        current_board = board.format(db[0], db[1], db[2], db[3], db[4], db[5], db[6], db[7], db[8])
        print(current_board)
        # remove input from correct    
        free_spots.remove(choice)
        
        
        # prep for vertical win
        xwin = False
        x2[coords[choice][0]] += 1
        
        # prep for horizontal win
        ywin = False
        y2[coords[choice][1]] += 1
        
        # prep for diagonal win
        diagwin = False
        if coords[choice] in player2diag1:
            player2diag1.remove(coords[choice])
        if coords[choice] in player2diag2:
            player2diag2.remove(coords[choice])
        
        
        # see if it was a winning move 
        
        for x in x2:
            if x == 3:
                xwin = True
        for y in y2:
            if y == 3:
                ywin = True
        if player2diag1 == [] or player2diag2 == []:
            diagwin = True

        if xwin or ywin or diagwin:
            print("Player 2 wins!")
            playing_game = False

        if free_spots == []:
            print("Ert's a tie!")
            playing_game = False
    
    ######## END OF GAME
    
    cont = input('Wanna keep playin, put Y.').lower()
    if cont != 'y':
        playing_game = False

######## BYE

print('Therks fer playin')
