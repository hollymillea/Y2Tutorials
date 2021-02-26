import random

# Given a list of strings, this function outputs a singular concatenated string
# i.e: ['A','B','C'] -> 'ABC'
def ListToString(InputList):
    OutputString = ''
    for Letter in InputList:
        OutputString = OutputString + Letter
    # Can also use:
    #OutputString = ''.join(InputList)
    return OutputString


# Given a list of strings, this function will return a list of indices in which the elements which only contain a space
# i.e: [' ','B','C',' '] -> [0,3]
def GetEmptyCells(InputList):
    OutputList = []
    n = len(InputList)
    for i in range(n):
        if InputList[i] == ' ':
            OutputList.append(i)
    # Can also use:
    #OutputList = [ i for i in range(len(InputList)) if InputList[i] == ' ' ]
    return OutputList


# Given a list, return an element from that list chosen at random
def GetRandomElement(InputList):
    n = len(InputList)
    # Length - 1 because we index from 0
    Index = random.randint(0,n-1)
    return InputList[Index]


# Given a list of floats, this function will return the index (in list form) of the element with the highest value.
# If multiple elements have the same value, then this function should return a list of the correspodning indices.
# i.e: [0,8,20,5] -> [2]
#      [7,2,5,7,5] -> [0,3]
def MaxIndices(InputList):
    # Initialise the output
    OutputList = []
    # Find the maximum value first
    MaxValue = max(InputList)
    # Find all the indices with this value
    n = len(InputList)
    for i in range(n):
        if InputList[i] == MaxValue:
            OutputList.append(i)
    # Can also use:
    #OutputList = [ i for i in range(len(InputList)) if InputList[i] == max(InputList) ]
    return OutputList


# TESTING
print( ListToString(['A','B','C']) == 'ABC' )
print( GetEmptyCells([' ','B','C',' ']) == [0,3] ) 
print( GetRandomElement([1,2,3,4,5]) )
print( MaxIndices([0,8,20,5]) == [2] )
print( MaxIndices([7,2,5,7,5]) == [0,3] )




# DISCUSSION:
# The code:
Run = False
if (Run):
    N = 5/0

# Python only checks code when it is executed. As 'Run' is set to false, then Python will
# never go inside the 'if' statement and so will not try the division by 0. Other languages
# check for these things when the code is compiled, hence you could not run this in Java
# or in C.
