
#############################
# TASK 1
#############################
def Swap(List,i,j):
    return


#############################
# TASK 2
#############################
def FindPairSum(List, X):
    return
        

#############################
# TASK 3
#############################
def Fibonacci(n):
    return

def FibonacciDP(n):
    return


#############################
# TASK 4
#############################
def SubText(s1,s2):
    return


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


#TimeFunction('Fibonacci(40)')
#TimeFunction('FibonacciDP(40)')