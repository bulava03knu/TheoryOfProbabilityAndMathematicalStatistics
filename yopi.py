import math
import matplotlib.pyplot as plt
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
i = 0
sukupna_chastota = int(0)
with open(output_name, "a") as f:
    f.write('Таблиця частот\n')
    f.write('Фільм         Частота         Сукупна частота\n')
    for i in range (1, m + 1):
        sukupna_chastota = sukupna_chastota + a[i-1]
        line = 'Фільм №'+str(i)+ '      '+str(a[i - 1])+ '              '+str(sukupna_chastota)+'\n'
        f.write(line)
max_value = []
maximum = max(a)
for i in range (1, m + 1):
    if (a[i - 1] == maximum):
        max_value.append(i)
if (len(max_value) == len(a)):
    with open(output_name, "a") as f:
        f.write('Усі фільми мають однакову кількість переглядів\n')
elif (len(max_value) == 1):
    with open(output_name, "a") as f:
        line = 'Найчастіше було переглянуто Фільм №'+str(max_value[0])+'\n'
        f.write(line)
else:
    with open(output_name, "a") as f:
        line = 'Найчастіше було переглянуто фільми №'.strip()
        f.write(line)
    for i in range (0, len(max_value)):
        if (i != len(max_value) - 1):
            with open(output_name, "a") as f:
                line = (str(max_value[i]) + ', ').strip()
                f.write(line)
        else:
            with open(output_name, "a") as f:
                f.write(max_value[i]+'\n')
exist_m = int(0)
for i in range (0, len(a)):
    for j in range (0, len(a)):
        if (a[i] == a[j] and i != j):
            exist_m = 1
if (exist_m == 0):
    with open(output_name, "a") as f:
        f.write('Моди цієї вибірки не існує\n')
else:
    moda_ch = max(a)
    moda = []
    for i in range (0, len(a)):
        if (a[i] == moda_ch):
            moda.append(i+1)
    with open(output_name, "a") as f:
        f.write('Мода вибірки: '.strip())
    for i in range (0, len(moda)):
        if (i != len(moda) - 1):
            with open(output_name, "a") as f:
                f.write(('Фільм №' + str(moda[i]) + ', ').strip())
        else:
            with open(output_name, "a") as f:
                f.write('Фільм №' + str(moda[i])+'\n')
if (sukupna_chastota % 2 == 0):
    d = sukupna_chastota/2
    i = 0
    c = int(0)
    while(c < d):
        c = c + a[i]
        i = i + 1
    i = i - 1
    with open(output_name, "a") as f:
        f.write('Медіана вибірки: Фільм №' + str(i+1)+'\n')
else:
    d1 = sukupna_chastota/2 - 0.5
    d2 = sukupna_chastota/2 + 0.5
    i1 = 0
    c1 = int(0)
    while(c1 < d1):
        c1 = c1 + a[i1]
        i1 = i1 + 1
    i1 = i1 - 1
    i2 = 0
    c2 = int(0)
    while(c2 < d2):
        c2 = c2 + a[i2]
        i2 = i2 + 1
    i2 = i2 - 1
    if (i1 == i2):
        with open(output_name, "a") as f:
            f.write('Медіана вибірки: Фільм №' + str(i1+1)+'\n')
    else:
        with open(output_name, "a") as f:
            f.write('Медіана вибірки: Фільм №' + str(i1+1), 'та Фільм №' + str(i2+1)+'\n')

sum = float(0)
sum1 = float(0)
for i in range (0, len(a)):
    sum = sum + (i+1)*(i+1)*a[i]
    sum1 = sum1 + (i+1)*a[i]
sum = sum/sukupna_chastota
sum1 = sum1/sukupna_chastota
sum1 = sum1*sum1
with open(output_name, "a") as f:
    f.write('Дисперсія: ' + str(round(sum - sum1, 3))+'\n')
    f.write('Середнє квадратичне відхилення: '+str(round(math.sqrt(sum - sum1), 3))+'\n')
x = []
for i in range (1, len(a) + 1):
    x.append(i)
fig, axes = plt.subplots(1, 1)
axes.bar(x, a)
#plt.show()
plt.savefig('output_figure_'+str(m)+'.png')