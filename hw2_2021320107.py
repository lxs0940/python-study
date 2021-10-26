# DO NOT ADD ANY 'import' STATEMENT!!!
# Remove 'pass' statement
# And add your code at the location of 'IMPLEMENT HERE!' comment
# You can define your own function to use
# But you can't modify the name and arguments of the functions

# P01
def fibb(n):
    # IMPLEMENT HERE!
    if n == 1 or n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
  
# P02
import math

phi = (1 + math.sqrt(5)) / 2  # use this value as a true value of 'phi' to campare with estimated value

def fibb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

def estimatePhi(n):  # Do not use 'math' library functions in your own code!!!
    approx = fibb(2) / fibb(1)
    i = 2
    while abs(approx - phi) > 10**n:
        i += 1
        approx = fibb(i) / fibb(i - 1)        
    return approx

# P03
def sigma(a, b, f):
    if a > b:
        a, b = b, a
    if b == a:
        return f(b)
    else:
        return f(b) + sigma(a, b-1, f)
    # IMPLEMENT HERE!

# P04
def quadratic(a, b, c):
    # IMPLEMENT HERE!
    def f(x):
        return a*(x**2) + b*x + c
    return f
    
# P05
def composition(fs): 
    # IMPLEMENT HERE!
    num = len(fs)
    def calc(x):
        for i in range(num):
            x = fs[i](x)
        return x
    return calc 

# P06
def position(x0, y0, f):
    # IMPLEMENT HERE!
    y1 = f(x0)
    if y0 > y1:
        return -1
    elif y0 == y1:
        return 0
    else:
        return 1

# P07
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def goldBach(n):
    # IMPLEMENT HERE!
    count = 0
    for i in range(1, n):
        if isPrime(i) and isPrime(n-i):
            count += 1
    return count  

# P08
def iSP_recursive(n, k, p):          
    if n == k:
        return True
    if p == 0 and n != k:
        return False
    while p >= 1:
        if n%p != 0:
            p -= 1
        else:
            return iSP_recursive(n, k+p, p-1) or iSP_recursive(n, k, p-1)

def isSemiPerfect(n):
    if n == 1:
        return False
    p = n // 2 
    while n%p != 0:
        p -= 1
    return iSP_recursive(n, p, p-1) or iSP_recursive(n, 0, p-1)
# P09
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def comb(n, k):
    result = 1
    for i in range(1, k+1):
        result = (result * (n-i+1)) // i
    return result

def goodView(m, c):
    pass  # IMPLEMENT HERE!

# P10
def goodSide(n, a, b):
    pass  # IMPLEMENT HERE!

#########################################################################
# From this line, the code below is to test your answer functions
# So NEVER MODIFY IT
def testQuadratic(a, b, c, x):
    try:
        return quadratic(a, b, c)(x)
    except TypeError:
        return None

def testComposition(fs, x):
    try:
        return composition(fs)(x)
    except TypeError:
        return None

def nthPrime(n):
    if n == 1:
        return 2
    c = nthPrime(n-1) + 1
    while not isPrime(c):
        c += 1
    return c

def main():
    problems = ("fibb", "estimatePhi", "sigma", "quadratic", "composition", "position", "goldBach", "isSemiPerfect", "goodView", "goodSide")
    testcases = {
        "fibb": (
            fibb,
            [1, 2, 5, 6, 7],
            [1, 1, 5, 8, 13]
        ),
        "estimatePhi": (
            estimatePhi,
            [-4, -3, -1, -5, -10],
            [1.6179775280898876, 1.6176470588235294, 1.6666666666666667, 1.6180257510729614, 1.6180339886704431]
        ),
        "sigma": (
            sigma,
            [(1, 10, lambda x: x), (1, 10, lambda x: x**2), (5, 10, lambda x: 2*x), (1, 10, lambda x: 2**x), (1, 10, lambda _: 4)],
            [55, 385, 90, 2046, 40]
        ),
        "quadratic": (
            testQuadratic,
            [(1, 2, 3, 5), (1, 2, 3, 10), (-3, 1, 4, 6), (2, 5, 1, 9), (1, -4, 4, 2)],
            [38, 123, -98, 208, 0]
        ),
        "composition": (
            testComposition,
            [([lambda x: x**2, lambda x: 2*x, lambda x: x-10], 5),
             ([lambda x: x**2, lambda x: 2*x, lambda x: x-10], 7),
             ([nthPrime, lambda x: 5*x], 3),
             ([nthPrime, lambda x: x**2], 6),
             ([lambda x: x, lambda y: y], 10)],
            [40, 88, 25, 169, 10]
        ),
        "position": (
            position,
            [(1, 2, lambda x: x),
             (1, 3, lambda x: 2*x+4),
             (1, 6, lambda x: 2*x+4),
             (1, -9, lambda x: 2*x+4),
             (-1, -2, lambda x: 2*x)],
            [-1, 1, 0, 1, 0]
        ),
        "goldBach": (
            goldBach,
            [12, 24, 30, 32, 20],
            [2, 6, 6, 4, 4]
        ),
        "isSemiPerfect": (
            isSemiPerfect,
            [1, 10, 15, 30, 40],
            [False, False, False, True, True]
        ),
        "goodView": (
            goodView,
            [(3, 2), (5, 3), (7, 2), (9, 4), (10, 3)],
            [3, 35, 1764, 67284, 1172700]
        ),
        "goodSide": (
            goodSide,
            [(5, 2, 3), (10, 5, 5), (10, 7, 3), (4, 2, 2), (9, 3, 6)],
            [18, 2520, 1008, 6, 588]
        )
    }
    for fn in problems:
        correct = True
        testfunc, inputs, outputs = testcases[fn]
        for i in range(len(inputs)):
            result = testfunc(*(inputs[i])) if isinstance(inputs[i], tuple) else testfunc(inputs[i])
            if result != outputs[i]:
                print(fn + ": Incorrect output for " + str(i+1)+"-th input")
                correct = False
        if correct:
            print(fn + ": Correct for all inputs")

main()
