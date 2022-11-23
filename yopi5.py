import math
from sympy import *

def ce(k, n):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def gauss(x):
    return math.exp(-math.pow(x, 2)/2)/math.sqrt(2*math.pi)

def integral(t1, t2):
    x = Symbol('x')
    expr = exp(-x**2 / 2)
    return integrate(expr, (x, t1, t2))

def integfunc(t1, t2):
    return integral(t1, t2)/math.sqrt(2*math.pi)

def integlaplas(n, m1, m2, p):
    q = 1 - p
    x1 = (m1 - n * p) / math.sqrt(n * p * q)
    x2 = (m2 - n * p) / math.sqrt(n * p * q)
    return round(integfunc(x1, x2), 4)

def bernulli(n, m, p):
    return round(ce(m, n) * math.pow(p, m) * math.pow(1 - p, n - m), 3)

def laplas(n, m, p):
    q = 1 - p
    x = (m - n*p)/math.sqrt(n*p*q)
    return round(1/math.sqrt(n*p*q)*gauss(x), 5)

def puasson(n, m, p):
    return round(math.pow(n*p, m) * math.exp(-n*p) / math.factorial(m), 4)

def searchc(n, p):
    if (n * p - int(n * p) == 0):
        c = n * p
    else:
        c = int(n * p + p)
    return c

def task1():
    with open("Lab5_Result.txt", "w") as f:
        f.write('Завдання 1\n')
        f.write('Імовірність: ')
        n = 5
        m = 3
        p = 0.2
        f.write(str(bernulli(n, m, p)) + '\n\n')

def task2():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 2\n')
        f.write('а) ')
        m = 4
        n = 5
        p = 0.8
        f.write(str(bernulli(n, m, p)) + '\n')
        f.write('б) ')
        sum = 0.0
        for i in range(4, n + 1):
            sum = sum + bernulli(n, i, p)
        f.write(str(round(sum, 5)) + '\n\n')
        
def task3():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 3\n')
        f.write('Імовірність: ')
        n = 400
        m = 80
        p = 0.2
        f.write(str(laplas(n, m, p)) + '\n\n')
        
def task4():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 4\n')
        f.write('Імовірність: ')
        n = 100000
        m = 5
        p = 0.0001
        f.write(str(puasson(n, m, p)) + '\n\n')
    
def task5():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 5\n')
        f.write('Імовірність: ')
        n = 600
        m1 = 228
        m2 = 252
        p = 0.4
        f.write(str(integlaplas(n, m1, m2, p)) + '\n\n')
    
def task6():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 6\n')
        f.write('Число вимог: ')
        n = 100.0
        p = 0.4
        c = searchc(n, p)
        f.write(str(c) + '\n')
        f.write('Імовірність: ')
        f.write(str(laplas(n, c, p)) + '\n\n')
    
def task7():    
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 7\n')
        f.write('Імовірність: ')
        n = 4000
        p = 0.04
        m1 = 0
        m2 = 170
        f.write(str(integlaplas(n, m1, m2, p)) + '\n\n')
    
def task8():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 8\n')
        f.write('Імовірність: ')
        n = 10000
        m = 5000
        p = 0.5
        f.write(str(laplas(n, m, p)) + '\n\n')
def task9():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 9\n')
        f.write('Імовірність: ')
        n = 1000
        m = 5
        p = 0.002
        f.write(str(puasson(n, m, p)) + '\n\n')
def task10():
    with open("Lab5_Result.txt", "a") as f:
        f.write('Завдання 10\n')
        f.write('Імовірність: ')
        n = 150.0
        p = 0.03
        c = searchc(n, p)
        f.write(str(c) + '\n')

task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()