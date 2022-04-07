print('Hello World')
print(123) 
print('WhoCame?')
print('Привет! Я Арсений')
print('и что?')
text = 'Helloy Helloy Helloy'
text =text . replace('y',' ')
print(text)

first_name = "Whocame--Mountaindew--Smokazacho"
words = first_name.split('--')
print(words)
new_text = '\n'.join(words)
print(new_text)
print(first_name.istitle())
a=15
b=15
c=(a+b)
print(c)
from time import sleep
from os import system
text='МаКс лОх'
for i in range(2):
    print(text)
    text = text.swapcase()
    sleep(0.5)
what=input("Что делаем?(+,-,*,):")
a=float(input("Введи первое число: "))
b=float(input("Введи второе число: "))
if what=="+":
    c= a+b
    print("Результат: "+str(c))
elif what=="-":
    c= a-b
    print("Результат: "+str(c))
elif what=="*":
    c=a*b
    print("Результат: "+str(c))