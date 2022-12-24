import random

class TicTacToe:
#the similiar to a list in C

    def __init__(self):
        self.board = []
    #initializes the list
    
    def create_board(self):
    #creating the board
        for i in range (3):
        #in range 3 because it's 3 lines
            row = []
            for j in range (3):
            #in range 3 because it's 3 columns
                row.append('-')
            self.board.append(row)
        
    def first_player(self):
    #choose what player is going to start
        return random.randint(1,2)
        #first = random.randint(1,2)
        #print(first)
        #return(first)
    
    def print_board(self):
    #printing the board
        for row in self.board:
        #getting the row in the list
            for spot in row:
                print(spot, end="  ")
            #I called space just to identify, and put a space between the -    
            print()
            #putting a newline
    
    def put_spot(self, row, column, player):
    #inserts the X or O in the right spot
        self.board[row][column] = player

    def player_win(self, player):
    #check if the player won
        win = None
        #the lenght of the board
        n = len(self.board)
        
        #check if won by column
        for column in range(n):
            win = True
            for row in range(n):
                if self.board[column][row] != player:
                    win = False
                    break
            if win:
                return win
        
        #check if won by row
        for row in range(n):
            win = True
            for column in range(n):
                if self.board[column][row] != player:
                    win = False
                    break
            if win:
                return win

        #check if won by diagonal
        #in diagonals we can win 2 different ways
        #1 1 / 2 2 / 3 3
        win = True
        for spots in range(n):
            if self.board[spots][spots] != player:
                win = False
                break
        if win:
            return win  
            
        #1 3 / 2 2 / 3 1
        win = True
        for spots in range(n):
            if self.board[spots][n - 1 - spots] != player:
                #3 1 / 2 2 / 1 3
                    #- - - \0
                    #- - - \0
                    #- - - \0
                win = False
                break
        if win:
            return win
        return False

    def game_draw(self):
        for row in self.board:
            for spot in row:
                if spot == '-':
                    return False
        return True

    def swap_player(self, player):
        return 'O' if player == 'X' else 'X'

    def start(self):
        self.create_board()
        #print(self.board)
        player = 'X' if self.first_player() == 1 else 'O'
        #print(player)
        while True:
            print()
            print("Player",player,"turn")
            print()

            self.print_board()
            
            print()
            row, column = list(map(int, input("Please enter a row and a column:").split()))
            #create a list to read the row and column, the map function applies each element in iterable and the .split divides the string in 2 substrings
            #print(row)
            #print(column)
            self.put_spot(row - 1, column - 1, player)
            #since the strings start with 0, we need to -1 so it goes to the right spot
            if self.player_win(player):
            #check if the player playing won
                print()
                print("Player",player,"wins!")
                #if it wins it will print which player won and breaks the cycle
                break
            if self.game_draw():
            #check if the game is draw
                print()
                print("Game Draw!")
                #if it is it will print game draw and breaks the cycle
                break
            player = self.swap_player(player)
        print()
        self.print_board()
        print()

#start the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()