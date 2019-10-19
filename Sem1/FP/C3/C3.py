# specifications
# tests
# exceptions
# undo ?
# modular programming (divide into UI and non UI)

# Q = n/d  n,m - integers, m not 0
# 2/3 -> (2,3)

import math

def print_menu():
    print ("Calculator menu:")
    print (" + for adding 2 rational numbers")
    print (" c to clear the calculator")
    print (" u to undo the last operation")
    print (" x to close the calculator")

def get_numerator(q):
    return q[0]
def get_denominator(q):
    return q[1]

'''
def createq(n = 0, m = 1):
    return (n,m)

print(createq(1,0)) !!!
'''

def createq(n = 0, d = 1):
    if d == 0:
        raise ValueError("invalid denuminator")
    g = math.gcd(n,d)
    return (n//g,d//g)

'''
def ui():
    try:
        print(createq(1,0))
    except ValueError:          #except Exception
        print("oopsie")

ui()
'''

def add(q1,q2):
    '''
    Return q1+q2
    params:
        q1,q2 - rational numbers
    output:
        q3, q1 + q2 = q3
    '''
    n = get_numerator(q1)*get_denominator(q2) + get_numerator(q2)*get_denominator(q1)
    d = get_denominator(q1)*get_denominator(q2)
    return createq(n,d)

def init_calc():
    return(createq(0),[])

def get_total(calc):
    return calc[0]

def tostr(q):
    return str(get_numerator(q)) + '/' + str(get_denominator(q))

def add_calc(calc):
    try:
        n = int(input("n= "))
        d = int(input("d= "))
        q = createq(n,d)
        total = add(get_total(calc),q)
        print(tostr(total))
        calc2 = [total,calc[1]+[q]]
    except ValueError:
        print("error")
    return calc2

def start():
    calc = init_calc()
    commands = {'+':add_calc}
    while True:
        print_menu()
        print("Total: " + tostr(get_total(calc)))
        cmd = input("command: ")
        if cmd in commands:
            calc = commands[cmd](calc)
        elif cmd == 'x':
            return
        else:
            print("bad user")

start()
# test-driven development
# 1. write functions specs
# 2. write some tests
# 3. run test - it must fail
# 4. write the function
# 5. run test - it must pass

# 1. start name with test + function that is tested
# 2. no params, no return!!
# 3. test passes -> be quiet
#    test fails -> make noise

def test_add():
    q1 = createq(0)
    q2 = createq(1)
    q3 = add(q1,q2)

    assert get_numerator(q3) == 1
    assert get_denominator(q3) == 1

    q1 = createq(1,2)
    q2 = createq(3,4)
    q3 = add(q1,q2)

    assert get_numerator(q3) == 5
    assert get_denominator(q3) == 4

test_add()
