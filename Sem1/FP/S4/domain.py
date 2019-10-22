'''
Here you code evrything about the domain(=problem domain)
domain = circles,Q,Z,exoenses,transactions,contest result
'''

#c[x,y,r]
#c=[0,0,1] unit circle, not valid in our program

def get_x(c):
    return c[0]
def get_y(c):
    return c[1]
def get_r(c):
    return c[2]

def create_circle(x,y,r):
    '''
    Create a circle centered in (x,y) with radius r
    params:
        x,y,r - integers, where x,y,r>0 and circle in (+,+)
    return the circle
    Raises ValueError if circle is invalid
    '''
    if r <= 0:
        raise ValueError("radius <= 0")
    if x < r or y < r:
        raise ValueError("Circle not in 1st quadrant")
    return[x,y,r]

# 1. write the function specification
# 2. write a test function 
# 3. run the test function - it must fail
# 4. write function code
# 5. run the test - it should pass(repeat)
# 6. Optimize

def test_init():
    circles = []
    circles.append(create_circle(1,1,1))
    circles.append(create_circle(5,3,2))
    circles.append(create_circle(4,1,1))
    return circles

def tostr(c):
    return "(" + str(get_x(c)) + ',' + str(get_y(c)) + "), r=" + str(get_r(c))


def test_create_circle():
    c = create_circle(1,1,1)
    assert get_x(c) == 1 and get_y(c) == 1 and get_r(c) == 1

    #radius is smaller than 0
    try:
        c = create_circle(1,1,-1)
        assert False
    except ValueError:
        assert True

    #not in (+,+)
    try:
        c = create_circle(1,1,2)
        assert False
    except ValueError:
        assert True

def test_tostr():
    c = create_circle(1,1,1)
    assert tostr(c) == '(1,1), r=1'
    c = create_circle(29,21,21)
    assert tostr(c) == '(29,21), r=21'

test_create_circle()
test_tostr()