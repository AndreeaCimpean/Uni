from domain import *

'''
place functions which solve problem requierments functions
'''

def add_circle(circles,history,x,y,r):
    c = create_circle(x,y,r)
    history.append(circles.copy())
    circles.append(c)


'''
Ways to undo:
    1. keep list of operations and their parameters and reverse them
    (efficent but complicated way)

    2. keep the history of program data in a list
'''
def undo(circles, history):
    # update circles with the last elem in the history
    if len(history) == 0:
        raise ValueError("No more undos.")
    circles.clear()
    circles.extend(history.pop())