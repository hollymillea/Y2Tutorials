import sheet2 as s2

def Learn(n):
    return


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
#Play(100000,10)