# 1
# print('hello')
# print(5+7)
# print(7/5)
# print('hello,'+'hi')
# print('5+9')
# print('5'+'9')

#2
# number=5
# print(number)
# #print('number')
# # number='reza'
# # print(number)
# print(number*number)
# number=number*number
# print(number)

#3
# name=input('enter first name : ')
# family=input('enter last name : ')
# print(name+" "+family)

#4
# n=float(input('enter number : '))
# m=float(input('enter number : '))
# #print(n+m)
# print('result = '+str(n+m))

#5
# import winsound
# password='abc123'
# userPass=input('enter password : ')

# if password==userPass:
#     print('YES')
# else:
#     print('NO')
#     winsound.Beep(2000, 5000)

#6
# n=int(input('enter number : '))
# # m=int(n/2)

# # if m*2==n:
# if n%2==0:
#     print('even')
# else:
#     print('odd')

#7
# n=int(input('enter number : '))
# if n>0:
#     print('+')
# else:
#     print('-')

#8
# n=int(input('enter number : '))
# if n<10:
#     print(1)
# elif n<100:
#     print(2)
# elif n<1000:
#     print(3)
# else:
#     print('invalid')

#9
# import winsound
# color=input('enter color : ').lower()

# # print(color)
# # print(color.lower())
# # print(color.upper())

# if color=='red':
#     print('STOP')
# elif color=='green':
#     print('GO')
# elif color=='yellow':
#     print('SLOW')
# else:
#     winsound.Beep(800,1000)

#10
# n=int(input('enter number : '))
# if n<10 and n>-10:
#     print(1)
# elif n<100 and n>-100:
#     print(2)
# elif n<1000 and n>-1000:
#     print(3)
# else:
#     print('invalid')

#11
# n=int(input('enter number : '))
# if n<0 or n>10:
#     print('yes')
# else:
#     print('invalid')

#12
# n=float(input())
# m=float(input())
# op=input()

# if op=='+':
#     print(n+m)

#13
# try:
#     n=int(input('entrer number : '))
#     print(n*n)
#     #print(10/n)
# except Exception as error:
#     #print('error')
#     print(error)
#     #pass

#14
# names=['ali','sara','reza','amir','narges']
# print(names)
# print(names[3])
# #print(names[5])
# print(names[-1])
# print(names[-2])
# print(len(names))
#print(len(input('enter text : ')))
# names[2]='maryam'
# names[3]=names[0]
# print(names)

#15
# names=['ali','sara','reza','amir','narges']
# # names.append('saeid')
# # names.append(input('enter name : '))
# #names.insert(2,'sahar')
# names.insert(len(names),'sahar')
# print(names)

#16
# names=['ali','sara','reza','amir','narges']
# index=int(input('enter index : '))

# if index>=0 and index<len(names):
#     print(names[index])
# else:
#     print('invalid index')

#17
# names=['ali','sara','reza','amir','narges']
# i=int(input('enter index : '))
# j=int(input('enter index : '))

# #1
# # temp=names[i]
# # names[i]=names[j]
# # names[j]=temp

# #2
# names[i],names[j]=names[j],names[i]

# print(names)

#18
# names=['ali','sara','reza','amir','narges','amir']
# #del names[2]
# #names.remove('amir')
# # n=names.pop()
# n=names.pop(2)
# print(names)
# print(n)

#19
# names=['ali','sara','reza','amir','narges']
# print(names)
# # print(sorted(names,reverse=True))
# # names.sort(reverse=True)
# names.reverse()
# print(names)

#20
# numbers=[3,1,9,4,5]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(sum(numbers)/len(numbers))

#21
# numbers=[3,1,9,4,5]
# print(numbers[2:4])
# print(numbers[:3])#[0:3]
# print(numbers[1:])
# print(numbers[0:len(numbers)])
# print(numbers[:])

#22
# names=['ali','sara','reza','amir','narges']
# n=input('enter name : ').lower()
# #print(n in names)
# #if n in names[0]:
# if n in names:
#     print('found')
# else:
#     print('not found')

#23
# names1=[]
# names2=['ali','sara','reza','amir','narges']
# n=input('enter name : ')

# if n in names2:
#     names2.remove(n)
#     names1.append(n)

# print(names1)
# print(names2)   

#24
# r=range(10)
# r=range(5,50)
# r=range(1,100,2)
# r=range(100,1,-1)
# print(r)
# print(list(r))
# print(list(range(1,100,10)))

#25
# import random
# n=random.randrange(10)
# n=random.randrange(1,10)
# n=random.randrange(1,10,2)
# from random import randrange
# n=randrange(100)
# print(n)

#26
from random import randrange
names=['sepehr',
       'sepanta',
       'elaheh',
       'elnaz',
       'fatemeh',
       'maryam',
       'mahdieh']
n=randrange(len(names))
print(names[n])

#27
# names=['ali','sara','reza','amir','narges','reza']
# numbers=[3,6,7,11,8,9,2]
# #1
# # f=filter(lambda n:n=='reza',names)
# # print(f)
# # print(list(f))

# #2
# # f=filter(lambda i:i%2!=0,numbers)
# # print(list(f))

# #3
# letter=input('enter letter : ')
# f=filter(lambda n:letter in n,names)
# print(list(f))

#28
#tuple
# user=('ali','asadi','0911')
# user=(input('enter name : '),
#       input('enter family : '),
#       input('enter phone : '))
# print(user)
# print(user[1])
#dictionary
# user={'name':'ali',
#       'family':'asadi',
#       'phone':'0911'}

# print(user)
# print(user['family'])
# user['age']=int(input('enter age : '))
# print(user)

#29
# names=['sepehr',
#        'sepanta',
#        'elaheh',
#        'elnaz',
#        'fatemeh',
#        'maryam',
#        'mahdieh']
#1
# for n in names:
#     print(n,end=' ')#\n, \t

#2
# for i in range(len(names)):
#     print(names[i])      

#30
# from random import randrange
# n=int(input('enter number : '))
# for i in range(n):
#     print(randrange(7))

#31
# from random import randrange
# names=['ali','sara','reza','amir','narges']
# n=int(input('enter number : '))

# for i in range(n):
#     r=randrange(len(names))
#     print(names[r])
#     del names[r]

#32
# n=1
# m=1
# i=1
# while n<16:
#     #1
#     # if n%5==0:
#     #     print(n)
#     # else:
#     #     print(n,end='\t')
#     #2
#     print(n,end='\t')
#     if m==i:
#         print()
#         m+=1
#         i=0
#     i+=1

#     n+=1