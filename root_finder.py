import numpy as np
import sys
sys.setrecursionlimit(10000)
"""
Very simple optimisation problem. 
Try to find a square root. 

"""

# Square root of X is Y 
def direction(Y,X):
    if Y > X/Y:
        return -1
    else:
        return 1

def step(Y,X,increment):
    d = direction(Y,X)
    Y = Y + d * increment
    return Y

def goal(X,Y,error,increment):
    try:
        if Y != X/Y:
            Yi = step(Y,X,increment)
            return goal(X,Yi,error,increment)
        elif Y==X/Y:
            print("Square root : ", Y)
            return Y
        
        else:
            return ("Something is wrong with the conditions.")

    except:
        print("Run time error occurred. The best approximation we have is:", Y)
        print("Square of the approximation: ", Y*Y)
        print("Delta : ", Y - X/Y)
        return Y

def test_case():
    increment = 1
    error = 0.001
    X = 1030608009090
    Y = np.random.randint(1,X)
    print("$Query : ", X)
    print("$Increment : ",increment)
    print("$Acceptable error :", error)
    print("$Random initialisation Y : ", Y)
    print(goal(X,Y,error,increment))

test_case()


"""
Notes & Observations 
* Hyperparameters exist. They influence the final outcome. 
* The recursion has limitations. It is set at 10k at the moment

>  incremental step 
> Tolerable error 
> Random initialisation 

influence the final answer. 
"""

