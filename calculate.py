#from math import sqrt
#num1 = int(input("enter number 1: "))
#num2 = int(input('enter number 2: '))
#op = input('enter operation: ')
#if op == '+':
   # print(num1+num2)
#elif op == '-':
 #   print(num1-num2)
#elif op == '*':
  #  print(num1*num2)
#elif op == '/':
   # print(num1/num2)
#elif op == 'sq':
    #print(int(num1*num1))
    #print(int(num2*num2))
#elif op == 'sqr':
   # print(sqrt(num1))
   # print(sqrt(num2))
#else :
   # print('error')
from math import sqrt
def multiply(a,b):
    print(int(a)*int(b))
def divide(a,b):
    print(int(a)/int(b))
def add(a,b):
    print(int(a)+int(b))
def subtract(a,b):
    print(int(a)*int(b))
def sq(a):
    print(int(a)*int(a))
def sqr(a):
    print(sqrt(a))
#add(int(input('enter num1:')),int(input('enter num2: ')))
inp = input('operation : ')
num1 = int(input('number1'))
num2 = int(input('number2'))
if inp == 'multiply':
    print(num1*num2)
elif inp == 'add':
    print(num1+num2)
elif inp == 'subtract':
    print(num1-num2)
elif inp == 'divide':
    print(num1/num2)
elif inp == 'sq':
    print(num1*num1)
    print(num2*num2)
elif inp == 'sqr':
    print(sqrt(num1))
    print(sqrt(num2))
else:
    print('invalid')

