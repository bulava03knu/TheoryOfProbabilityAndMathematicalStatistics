import math

def ce(k, n):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def task1():
    with open("Lab4_Result.txt", "w") as f:
        f.write('Завдання 1\n')
        a = [40, 26, 22, 12]
        f.write('Імовірність: ')
        probability = (a[2]+a[3])/(a[0]+a[1]+a[2]+a[3])
        f.write(str(round(probability, 3)) + '\n\n')

def task2():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 2\n')
        f.write('Імовірність: ')
        f.write(str(round((ce(2,8)*ce(0,2)+ce(1,8)*ce(1,2))/ce(2,10), 3)) + '\n\n')
        
def task3():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 3\n')
        f.write('Імовірність: ')
        f.write(str(round(1 - (ce(3,8)/ce(3,10)), 3)) + '\n\n')

def task4():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 4\n')
        a = [0.15, 0.25, 0.2, 0.1]
        f.write('p5 = ')
        f.write(str(round(1 - a[0] - a[1] - a[2] - a[3], 3)) + '\n\n')

def task5():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 5\n')
        f.write('Імовірність: ')
        f.write(str(round(ce(2,80)/ce(2,120), 3)) + '\n\n')
        
def task6():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 6\n')
        p1 = float(0.9)
        p2 = float(0.8)
        f.write('Імовірність: ')
        f.write(str(round(p1 * p2, 3)) + '\n\n')
        
def task7():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 7\n')
        num_of_stud = float(10.0)
        num_of_quest = float(20.0)
        students = [3, 4, 2, 1]
        marks = [20, 16, 10, 5]
        temp = []
        p = float(0)
        for i in range(0, 4):
            add = students[i] / num_of_stud
            for j in range(0, 3):
                add = add * (marks[i] - j) / (num_of_quest - j)
            p = p + add
            temp.append(add)
        p1 = temp[0]/p
        p2 = temp[3]/p
        f.write('а) ' + str(round(p1, 6)) + '\n')
        f.write('б) ' + str(round(p2, 6)) + '\n\n')
        
def task8():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 8\n')
        f.write('Імовірність: ')
        proc1 = [0.4, 0.3, 0.3]
        proc2 = [0.9, 0.95, 0.95]
        p = float(0.0)
        for i in range(0, 3):
            p = p + proc1[i]*proc2[i]
        f.write(str(round(p, 3)) + '\n\n')
        
def task9():
   with open("Lab4_Result.txt", "a") as f:
       f.write('Завдання 9\n')
       f.write('Імовірність: ')
       proc1 = [0.4, 0.3, 0.3]
       proc2 = [0.8, 0.7, 0.85]
       p = float(0.0)
       for i in range(0, 3):
           p = p + proc1[i]*proc2[i]
       p0 = proc1[1]*proc2[1]/p
       f.write(str(round(p0, 3)) + '\n\n')

def task10():
    with open("Lab4_Result.txt", "a") as f:
        f.write('Завдання 10\n')
        f.write('Імовірність: ')
        proc1 = [0.3, 0.7]
        proc2 = [0.9, 0.8]
        p = float(0.0)
        for i in range(0, 2):
            p = p + proc1[i]*proc2[i]
        p0 = proc1[0] * proc2[0] / p
        f.write(str(round(p0, 3)))
        
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