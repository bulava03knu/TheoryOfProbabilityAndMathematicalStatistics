import math
import numpy
import matplotlib
a = []
print('Введіть назву файлу')
name = input()
file = open(name, mode="r")
i = int(0)
m = int(-1)
with open(name, "r") as file:
    for line in file.readlines():
        if (i > 0):
            a.append(int(line))
        else:
            m = int(line)
        i = i + 1
file.close()
output_name = 'output_'+str(m)+'.txt'

a.sort()

with open(output_name, "a") as f:
    q1 = (m+1)/4
    cq1 = math.floor(q1)
    dq1 = q1-cq1
    q1 = a[cq1-1]+dq1*(a[cq1]-a[cq1-1])
    f.write('Q1: ' + str(q1) + '\n')
    q3 = 0.75*(m+1)
    cq3 = math.floor(q3)
    dq3 = q3-cq3
    q3 = a[cq3-1]+dq3*(a[cq3]-a[cq3-1])
    f.write('Q3: ' + str(q3) + '\n')
    p90 = 0.9*(m+1)
    cp90 = math.floor(p90)
    dp90 = p90-cp90
    p90 = a[cp90-1]+dp90*(a[cp90]-a[cp90-1])
    f.write('P90: ' + str(p90) + '\n')

with open(output_name, "a") as f:
    f.write('\n\n')
    sum = int(0)
    for i in range(0, m):
        sum = sum + a[i]
    av = sum/m
    sum = int(0)
    for i in range(0, m):
        sum = sum + abs(a[i] - av)
    f.write('Середнє відхилення: ' + str(sum/m) + '\n')
    sum = int(0)
    for i in range(0, m):
        sum = sum + math.pow((a[i]-av), 2)
    f.write('Стандартне відхилення: ' + str(math.sqrt(sum/(m - 1))) + '\n')
    
with open(output_name, "a") as f:
    f.write('\n\n')
    sum = int(0)
    for i in range(0, m):
        sum = sum + a[i]
    av = sum/m
    l = numpy.array([[av,1],[100,1]])
    r = numpy.array([95,100])
    res = numpy.linalg.solve(l,r)
    f.write('Кориговані оцінки: ')
    sum = int(0)
    res1 = []
    for i in range(0, m-1):
        res1.append(res[0]*a[i]+res[1])
        f.write(str(res1[i]) + ', ')
        sum = sum + res1[i]
    res1.append(res[0]*a[m-1]+res[1])
    f.write(str(res1[m-1]) + '\n')
    sum = sum + res1[m-1]
    f.write('Перевірка: сережнє значення коригованих оцінок = ' + str(round(sum/m)) + '\n')
    
with open(output_name, "a") as f:
    f.write('\n\n')
    if (a[0] < 100):
        c = int(str(a[0])[0])
        f.write('\n' + str(c) + ' | ')
    else:
        c = 10
        f.write('\n' + '10 | ')
    for i in range(0, m):
        if (a[i] < 100):
            c1 = int(str(a[i])[0])
        else:
            c1 = 10
        if (c1 != c):
            f.write('\n' + str(c1) + ' | ')
            c = c1
        if (len(str(a[i])) == 2):
            f.write(str(a[i])[1] + ' ')
        else:
            f.write('0 ')
       
matplotlib.pyplot.boxplot(a)
matplotlib.pyplot.savefig('output_figure_'+str(m)+'.png')