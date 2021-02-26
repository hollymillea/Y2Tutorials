import sheet1 as s1

class TicTacToe():
    # Constructor function
    def __init__(self):
        print("\nNEW GAME")
        # Properties
        self.Board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.EmptyCells = [0,1,2,3,4,5,6,7,8]
        self.Turn = 'X'
        self.Winner = None
        self.StatesX = []
        self.StatesO = []


    # Methods

    #########################
    # Functions to complete
    #########################

    def RandomTurn(self):
        Position = s1.GetRandomElement(self.EmptyCells)
        self.Board[Position] = self.Turn
        return


    def HumanTurn(self):
        # Ask the user (you) to input a number/position
        print("Please input a number from 0-8 corresponding to the position in which you wish to play:")
        Input = input()
        # If the input is not a number between 0 and 8 ask again
        if (len(Input) != 1) or (ord(Input) < 48) or (ord(Input) > 56):
            print("Incorrect input. Please try again.")
            self.HumanTurn()
            return
        # Turn the input from a string into an integer
        Position = int(Input)

        ###############
        # Finish code: 
        ###############
        # If the cell is empty, place a marker in the cell
        if (Position in self.EmptyCells):
            self.Board[Position] = self.Turn
        # If this cell is already filled, run the function again to ask the user again
        else:
            print("This cell is already filled. Please try again.")
            self.HumanTurn()


    def Update(self):
        # Update the empty cells
        self.EmptyCells = s1.GetEmptyCells(self.Board)
        # Swap turns and save the current board (in string format) under the player's state list
        State = s1.ListToString(self.Board)
        if (self.Turn == 'X'):
            self.StatesX.append(State)
            self.Turn = 'O'
        elif self.Turn == 'O':
            self.StatesO.append(State)
            self.Turn = 'X'
        # Check to see if the game is over yet
        self.IsGameOver()
        return


    def HumanVsRandom(self):
        # While the game is not over yet
        while self.Winner == None:
            print(self)
            print(self.Turn + "'s turn:")
            if self.Turn == 'X':
                self.HumanTurn()
            elif self.Turn == 'O':
                self.RandomTurn()
            self.Update()
        print(self)
        print(self.Winner + " wins!")
        return



    #########################
    # Given functions
    #########################

    # Function which prints out the board
    # Call this function using 'print(self)'
    def __str__(self):
        Board = self.Board
        # Printing upper border
        print("╔═══╦═══╦═══╗")
        # Printing the first row
        print('║', Board[0], '║', Board[1], '║', Board[2], '║')
        print("╠═══╬═══╬═══╣")
        # Second row
        print('║', Board[3], '║', Board[4], '║', Board[5], '║')
        print("╠═══╬═══╬═══╣")
        # Third row
        print('║', Board[6], '║', Board[7], '║', Board[8], '║')
        # Lower border
        print("╚═══╩═══╩═══╝")
        return ''


    def IsGameOver(self):
        Board = self.Board
        # Check to see if we have any three in a row
        # The rows
        Row1 = Board[0] + Board[1] + Board[2]
        Row2 = Board[3] + Board[4] + Board[5]
        Row3 = Board[6] + Board[7] + Board[8]
        # The columns
        Col1 = Board[0] + Board[3] + Board[6]
        Col2 = Board[1] + Board[4] + Board[7]
        Col3 = Board[2] + Board[5] + Board[8]
        # The diagonals
        Diag1 = Board[0] + Board[4] + Board[8]
        Diag2 = Board[2] + Board[4] + Board[6]

        Threes = [Row1, Row2, Row3, Col1, Col2, Col3, Diag1, Diag2]
        
        if 'XXX' in Threes:
            self.Winner = 'X'
        elif 'OOO' in Threes:
            self.Winner = 'O'
        
        # Check to see if the board is full
        elif self.EmptyCells == []:
            self.Winner = 'Tie'


#######################
# TESTING
# - Uncomment one at a time (and recomment them when you move on to the next test)
#######################

#Game = TicTacToe()
#print(Game)

# Task 1:
#Game.RandomTurn()
#print(Game)

# Task 2:
#Game.HumanTurn()
#print(Game)

# Task 3:
#print("BEFORE")
#print("Board: ", Game.Board, "\nEmpty Cells: ", Game.EmptyCells, "\nTurn: ", Game.Turn, "\nWinner: ", Game.Winner, "\nStatesX: ", Game.StatesX, "\nStatesO: ", Game.StatesO)
#Game.RandomTurn()
#Game.Update()
#print("\nAFTER")
#print("Board: ", Game.Board, "\nEmpty Cells: ", Game.EmptyCells, "\nTurn: ", Game.Turn, "\nWinner: ", Game.Winner, "\nStatesX: ", Game.StatesX, "\nStatesO: ", Game.StatesO)

# Task4:
Game = TicTacToe()
Game.HumanVsRandom()