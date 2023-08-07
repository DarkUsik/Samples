#Отрывок кода для разделения числа на цифры

'''number = input("Введите целое число: ")
digits = [int(digit) for digit in number]
i = len(digits) - 1

for digit in digits:
    print(digit, i * "_", end=" ")
    i = i - 1'''

# Отрывок кода для выделения чисел или букв из строк

'''mass=[]
sum=0
len=input("Введите кол-во элементов в массиве:\n")
for i in range(int(len)):
    mass.append(input())
print("В массиве хранятся следующие элементы:\n",mass)
for word in mass:
    for letter in word:
        try:

            int(letter)  #Проверка на цифру
            print(int(letter))
            sum+=1
        except:
            print(letter)  #Вывод буквы
            continue
print(sum)'''

# Программа для создания пустого двумерного массива
'''a=3
mass=[0]*a
for i in range(a):      
    mass[i]=[0]*a
print(mass)'''

# Отрывок для нахождения НОД
'''a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)'''

# Отрывок для нахождения НОК
'''a=int(input())
b=int(input())
m = a * b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(m // (a + b))'''


