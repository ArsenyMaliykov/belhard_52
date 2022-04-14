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

numbers = '4 5 6 7 8 9 1 2'
numbers = numbers.split(' ')
for i,number in enumerate(numbers):
    numbers[i] = int(number)
print(numbers)
