# print('hello')
# print(4+5)
# print('4+5')
# print('4'+'5')
# print('ali'+'sara')
# print(8-2)
# print(3*4)
# print(10/5)
# print(7/3)
# print(10%5)
# print(7%3)
# print(18%4)
# print(5**3)

#2
# print(7/3)
# print(int(7/3))
# # print(5+'maharat')
# print(str(5)+'maharat')
# print(7)
# print(float(7))

#3
# print(5>2)
# print(8<3)
# print(5>=2)
# print(5>=5)
# print(8==5)
# print(8!=5)
# print('amir'>'sara')
# print('sara'>'sare')
# print('amir'=='amir')
# print('amir'=='Amir')
# print('a'>'A')

#4
# n=7
# print(n)
# n=2.5
# print(n*2)
# n='maharat'
# print(n)
# m=3
# print(str(m)+n)
# print(m*n)
# print(10*'hello')
# print('m')
# # print(number)#error

#5
# n=input('enter name : ')
# print(n)

#6
# password='abc123'
# userPass=input('enter password : ')
# print(password==userPass)

#7
# # n=input('enter number : ')#str input
# # n=int(input('enter number : '))
# n=float(input('enter number : '))
# print(2*n)#float output
# print(int(2*n))#int output

#8
# a=float(input('enter number 1 : '))
# b=float(input('enter number 2 : '))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)#divide on zero

# {}[]()<>

#9
# password='abc123'
# userPass=input('enter password : ')

# if password==userPass:
#     print('OK')
# else:
#     print('WRONG')

#10
# n=int(input('enter number : '))
# if n%2==0:
#     print('even')
# else:
#     print('odd')

#11
# n=int(input('enter number 1 : '))
# m=int(input('enter number 2 : '))
# if n>m:
#     # print('max is : '+str(n))
#     print(f'max is {n}')
# else:
#     print(f'max is {m}')

#12
# x=int(input('enter number 1 : '))
# y=int(input('enter number 2 : '))
# z=int(input('enter number 3 : '))

# if x>y:
#     if x>z:
#         print(x)
#     else:
#         print(z)
# else:
#     if y>z:
#         print(y)
#     else:
#         print(z)

#13
# color=input('enter light color : ')
# if color=='red':
#     print('STOP')
# elif color=='yellow':
#     print('SLOW')
# elif color=='green':
#     print('GO')
# else:
#     print('ALARM')
#     from winsound import Beep
#     Beep(450,2000)

#14
# x=int(input('enter number 1 : '))
# y=int(input('enter number 2 : '))
# z=int(input('enter number 3 : '))

# if x>y and x>z:
#     print(x)
# elif y>x and y>z:
#     print(y)
# else:
#     print(z)

#15
# x=float(input('enter number 1 : '))
# y=float(input('enter number 2 : '))

# if x>=16 or y>=16:
#     print('yes')
# else:
#     print('no')

#16
#A
# # n=int(input('enter number : '))
# n=float(input('enter number : '))
# print(n*n)

#B - try
# try:
#     # n=int(input('enter number : '))
#     n=float(input('enter number : '))
#     print(n*n)
# # except:
# except Exception as error:
#     # print('ERROR')
#     print(error)

#17
# # from math import math
# # print(pow(2,5))
# import math
# print(math.pow(2,5))
# print(math.sqrt(64))
# print(math.pi)
# print(math.e)
# print(math.log2(256))
# print(math.log10(10000))
# print(math.fabs(-5))
# print(round(2.42175,2))
# print(round(2.42575,2))
# print(math.ceil(2.42175))
# print(math.ceil(2.62575))

#18
# # numbers=[]#empty list
# numbers=[3,9,-1,4,11]
# print(numbers)
# print(*numbers)
# print(*numbers,sep='/')
# print(numbers[3])
# print(numbers[1])
# # print(numbers[5])#error
# print(numbers[-1]) 
# print(numbers[-2])
# # numbers[0]=12
# # numbers[0]=int(input('enter number : '))
# # print(numbers) 

# # numbers[0]=numbers[3]
# numbers[0],numbers[3]=numbers[3],numbers[0]
# print(numbers)

# #####
# a=5
# b=7
# # a,b=b,a
# c=b
# b=a
# a=c
# print(f'a={a} b={b}')

#19
# numbers=[16,18,8,14,20]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# # print(sum(numbers)/len(numbers))
# avg=sum(numbers)/len(s=numbers)
# print(avg)
# ##################
# print(sorted(numbers))
# print(sorted(numbers,reverse=True))
# #####
# print(5 in numbers)
# print(18 in numbers)

#20
# mylist=[8,5,-1,11,9,3]
# print(mylist[0:3])#0 -> 2
# print(mylist[:3])#0 -> 2
# print(mylist[3:6])#3 -> end
# print(mylist[3:])#3 -> end
# print(mylist[1:3])#1 -> 2
# print(mylist[:])#0 -> end

#21
# names=['ali','maryam','reza','narges']
# # print(sorted(names))
# # names.sort()
# # names.sort(reverse=True)
# names.reverse()
# print(names)

#22 add to list
# mylist=[]
# mylist.append('ali')
# mylist.append('sara')
# # mylist.append(input('enter name : '))
# mylist.insert(0,'reza')
# mylist.insert(2,'narges')
# mylist.insert(len(mylist),'amir')#append
# print(mylist)

#23 remove from list
# mylist=[6,3,-11,8,3,12]
# # del mylist[3]#index
# # mylist.remove(3)#value
# # # mylist.remove(15)#error
# # mylist.pop()
# # temp=mylist.pop()# save(return) delete value
# # print(temp)
# print(mylist.pop(2))
# print(mylist)

#24
# names=['ali','amir','sara','maryam']
# n=input('enter name : ')

# if n in names:
#     names.remove(n)
# else:
#     names.append(n)

# print(names)

#############
# n=5
# # n=7
# # n+=7#n=n+7
# n-=7#n=n+7
# print(n)

# a='ali'
# a+='reza'#a=a+'reza'
# print(a)

# c=3
# c*='maharat'
# print(c)

#25
# mylist=[2,5,8,-1,3]
# #1
# # temp=mylist
# #2
# # temp=mylist[:]
# #3
# temp=mylist.copy()#mylist[:]
# print(mylist)
# print(temp)
# temp[3]=20
# print(mylist)
# print(temp)

#26
# # mylist=[1,2,3,4,5,6,7,8,9,10]
# # print(range(5))
# # myRange=range(5)
# # myRange=range(2,5)
# # myRange=range(2,10,3)
# # myRange=range(2,10,-1)
# # myRange=range(10,1,-1)
# # myRange=range(-5,-1,1)
# # myRange=range(-5,-10,-1)
# # myRange=range(10,100,5)
# myRange=range(int(input('enter start : ')),
#               int(input('enter end : ')),
#               int(input('enter step : ')))
# print(*myRange)
# print(list(myRange))

#27
# from random import randrange
# print(randrange(5))
# print(randrange(1,5))
# print(randrange(2,15,3))
# print(randrange(-10,-1,1))

#28
from random import randrange
names=['amir','sara','reza','maryam']
n=randrange(len(names))
print(names[n])

###
# print(randrange(len(['amir','sara','reza','maryam'])))
