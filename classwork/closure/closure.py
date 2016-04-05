def makeAdder(n):
    def inner(x):
        return x + n
    return inner

add3 = makeAdder(3)
add5 = makeAdder(5)

print add3(10)
print add5(10)

def make_counter():
    # private "instance" data
    # has to be a list due to weird python scoping rules
    count[0]

    # public methods
    def inc():
        count[0] = count[0] + 1
    def dec():
        count[0] = count[0] - 1
    def reset():
        count[0] = 0
    def get():
        return count[0]

    # return a dictionary so we have access to all the methods
    return {'inc': inc, 'dec': dec, 'reset': reset, 'get': get}

#c1 = make_counter()
#c2 = make_counter()

#c1['inc']()
#c1['inc']()
#c1['inc']()
#print c1['get']()

import random
def get_name():
    names = ['bob','tom','sue']
    return random.choice(names)

def dble(f):
    name = f()
    return name + name

print dble(get_name)

def doubler(f):
    def inner():
        name = f()
        return name + name
    return inner

