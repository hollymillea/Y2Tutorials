
#############################
# TASK 1
#############################
def Swap(List,i,j):
    # If we are swapping the elements in List = [2,3] the list would be updated as so:
    # List = [2,3]
    # List = [5,3]
    # List = [5,2]
    # List = [3,2]
    List[i] = List[i] + List[j]
    List[j] = List[i] - List[j]
    List[i] = List[i] - List[j]
    return List


#############################
# TASK 2
#############################
def FindPairSum(List, X):
    N = len(List)
    # Our left point will only move right and our right pointer will only move left through the list
    LeftPointer = 0
    RightPointer = N-1

    Run = True
    while (Run):
        Number = List[LeftPointer] + List[RightPointer]
        # If our pointers point to the same element, then we have reach the middle (ish) and do not have any pair sums
        if (LeftPointer == RightPointer):
            return False
        # If we have a pair sum, return True (we can stop looking)
        elif (Number == X):
            return True
        # If our sum is too small, we want to increase our sum, so move the left pointer up one
        elif (Number < X):
            LeftPointer += 1
        # If our sum is too big, we want to decrease our sum, so move the right pointer down one
        elif (Number > X):
            RightPointer -= 1
        

#############################
# TASK 3
#############################
def Fibonacci(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def FibonacciDP(n):
    # Save all the Fibonacci numbers up to n into a list (so they only have t obe computed once)
    FibNumbers = [1,1]

    for i in range(2,n):
        X = FibNumbers[i-1] + FibNumbers[i-2]
        FibNumbers.append(X)
    
    return FibNumbers[-1] # [-1] retrieves the last element


#############################
# TASK 4
#############################
def SubText(s1,s2):
    s1Letters = ListToDict(s1)
    s2Letters = ListToDict(s2)

    # Check that all letters in s1 are in s2 (and enough counts of them)
    for Key in s1Letters.keys():
        s1Value = s1Letters[Key]
        s2Value = s2Letters.get(Key,0)
        if s2Value < s1Value:
            return False
    return True

def ListToDict(List):
    Dict = dict()
    for X in List:
        Value = Dict.get(X,0)
        if Value == 0:
            Dict[X] = 1
        else:
            Dict[X] += 1
    return Dict



#############################
# EXTRA FUNCTIONS
#############################
# Input the function you want to time (including the inputs) as a string, e.g:
# TimeFunction('Add(1,2)')
def TimeFunction(FunctionCall):
    import time
    StartTime = time.time()
    eval(FunctionCall)
    EndTime = time.time()
    RunTime = EndTime - StartTime
    print("Your function '" + FunctionCall + "' took " + str(RunTime) + " seconds.")

TimeFunction('Fibonacci(40)')
TimeFunction('FibonacciDP(40)')