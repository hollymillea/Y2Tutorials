import sheet2 as s2

def Learn(n):
    # Initialise both the SVs
    StateValuesX = {}
    StateValuesO = {}
    # For each learning iteration
    for i in range(n):
        # Play a game
        Game = s2.TicTacToe()
        #Game.HumanVsRandom()
        Game.ComputerVsComputer(StateValuesX,StateValuesO,PrintGame=False)
        # Updating the SVs - +1 for the winner and -1 for the loser
        if Game.Winner == 'X':
            StateValuesX = UpdateSVs(StateValuesX, Game.StatesX, 1)
            StateValuesO = UpdateSVs(StateValuesO, Game.StatesO, -1)
        if Game.Winner == 'O':
            StateValuesO = UpdateSVs(StateValuesO, Game.StatesO, 1)
            StateValuesX = UpdateSVs(StateValuesX, Game.StatesX, -1)
    #print(StateValuesX)
    #print(StateValuesO)
    return StateValuesO


def UpdateSVs(StateValues, States, Score):
    # Our learning parameter
    Alpha = 0.2
    # Iterate through the states backwards updating the states
    VSt1 = Score
    for State in reversed(States):
        VSt = StateValues.get(State, 0)
        Value = VSt + (Alpha * (VSt1 - VSt))
        StateValues[State] = Value
        VSt1 = Value
    return StateValues


def Play(TrainingN, TestingN):
    SVs = Learn(TrainingN)
    for i in range(TestingN):
        Game = s2.TicTacToe()
        Game.HumanVsComputer(SVs,PrintGame=True)

# Testing Learn():
#Play(1,0)

# Testing whole game play once completed:
Play(10000,10)