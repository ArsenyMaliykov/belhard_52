#a=float(input("Введите первое число:"))
#what=input("Что хотите сделать?(+,-,*,/,**):")
##b=float(input("Введите второе число:"))
#if what=="+":
    #c= a+b
    #print("Ответ: "+str(c))
#elif what=="-":
    #c= a-b
    #print("Ответ: "+str(c))
#elif what=="*":
    #c= a*b
    #print("Ответ: "+str(c))
#elif what=="/":
    #с= а/b
    #print("Ответ: "+str(c))
#elif what=="**":
    #c= a**b
    #print("Ответ: "+str(c)
#data = {
    #1: 'a',
    #2: 'b',
    #3: 'c',
#}
#for key in data:
       #print(key)


#number = input('Введи число: ')
#while not number.isdigit():
    #print('Are you stupid man?')
    #number = input('Try again stupid: ')
#while number.isdigit():
#number = int(number)

#numbers = '4 5 6 7 8 9 1 2'
#numbers = numbers.split(' ')
#for i,number in enumerate(numbers):
    #numbers[i] = int(number)
#print(numbers)

#N = int(input('Количество: '))
#M = int(input('Кратные: '))
#K = int(input('Нижний предел: '))
##for i in range(K, N*M+K+1):
    #if not i % M:
        #print(i)

#вводится текст,подсичтать количество гласный и согласный в самом тексте
#def foo(a,b,  *args, **kwargs):
    #print(a)
   #print(b)
    #print(args)
    #print(kwargs)
#foo(1,2,3,4,5,6,7)

#lst = [1,2,3,4,5,5,7,8]
#for i in range(len(lst)+1):
    #if lst[i] > lst[i+1]:
        #print(i+1)
        #break
    #else:
        #print(True)

import itertools


# 0 2 4 6 8
#for i in itertools.count(0,2):
    #if i >= 10:
       #break
    #print(i)

from random import randint

#пузырьковый метод(много циклов)
numbers = [randint(1,123)for _ in range(10)]
for _ in range(len(numbers)):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)