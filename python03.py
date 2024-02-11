# 1
# name=input('enter first name : ')
# family=input('enter last name : ')
# age=int(input('enter age : '))

# print(name+" " + family+" " + str(age))
 

#2
# password='abc123'
# userPass=input('enter passsword : ')

# if password==userPass:
#     print('yes')
# else:
#     print('error')

#3
# a=int(input('enter number : '))

# # if a%2==0:
# #     print('even')
# # else:
# #     print('odd')

# if a>=0:
#     print('+')
# else:
#     print('-')

# 4
#color=input('enetr color : ').lower()

# print(color)
# print(color.lower())

# if color=='green':
#     print('Go->')
# elif color=='yellow':
#     print('SLOW!')
# elif color=='red':
#     print('STOP<>')
# else:
#     print('alarm')


# 5
# a=int(input('enter number'))

# if a<10 and a>-10:
#     print('1')
# elif a<100 and a>-100:
#     print('2')
# elif a<1000 and a>-1000:
#     print('3')
# else:
#     print('error')


#6
#a=int(input('enter number : '))

# if a>10 or a<-10:
#     print('OK')
# else:
#     print('error')

# if a<10 and a>-10:
#     print('error')
# else:
#     print('OK')

#7
# try:
#     n=int(input('enter number : '))
#     print(n*n)
# except Exception as e:
#     #print(e)
#     pass

#8
# names=['ali','saeed','sara','reza','narges']
# print(names)
# print(names[3])
# print(len(names))
# print(names[-1])
# print(names[-2])
# names[2]='amir'
# print(names)

#9
# names=['ali','saeed','sara','reza','narges','reza']
# # names.append('amir')
# # names.insert(3,'abbas')
# # names.insert(len(names),'arman')
# del names[1]
# names.remove('reza')

# #temp=names.pop()
# temp=names.pop(1)
# print(names)
# print(temp)

#10
# names=['ali','amir','arman']
# n=input('enter name : ')
# names.append(n)
# print(names)

#11
# try:
#     names=['ali','amir','arman']
#     n=input('enter name : ')
#     names.remove(n)
#     print(names)
# except Exception as e:
#     print(e)

#12
# names=['ali','sara','amir','narges','reza']
# print(names)
# # print(sorted(names))
# # print(sorted(names,reverse=True))
# # names.sort()
# # names.sort(reverse=True)
# names.reverse()
# print(names)

#12+1
# numbers=[7,3,-1,12,8,5]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

#14
# numbers=[7,3,-1,12,8,5]
# print(numbers[2:4])
# print(numbers[:3])
# print(numbers[2:])
# print(numbers[:])

#15
# names=['amir reza','artin','ariya','kosar','mahdi']
# n=input('enter name : ')
# # print(n in names)
# if n in names:
#     print('found')
# else:
#     print('not found')

#16
# n=range(5)
# n=range(3,10)
# n=range(10,100,2)
# n=range(50,10,-5)
# print(n)
# print(list(n))

#17
#1
# import random
# n=random.randrange(1,10)
#2
# from random import randrange
# n=randrange(1,5)
# print(n)

############## EXAM #################
#3
# try:
#     a=int(input('yek adad vared konid : '))
#     print(a*2)
# except Exception as error:
#     print(error)
#5
# print(list(range(10,100,2)))

############## EXAM #################

#18
# from random import randrange
# names=['amir reza','artin','taha','kosar','mahdi']
# i=randrange(len(names))
# #print(i)
# print(names[i])

#19
# names=['ali','amir','sara','maryam','amir']
# numbers=[2,6,9,-11,4,3,5]

# # f=filter(lambda n:n=='amir',names)
# # f=filter(lambda n:'r'in n,names)
# # f=filter(lambda n:'ar'in n,names)
# # f=filter(lambda n:n%2==0,numbers)
# f=filter(lambda n:n<0,numbers)

# print(list(f))

#20
#tuple
# user=('ali','ahmadi','0911')
# user=(input('enter name : '),
#       input('enter family : '),
#       input('enter phone : '))
# print(user)
# print(user[1])
#dictionary
# user={'name':'sara',
#       'family':'rezaei',
#       'phone':'0912'}
# print(user)
# print(user['family'])

# user['age']=int(input('enter age : '))
# print(user)

#21
# user1={'name':'ali','family':'asadi'}
# user2={'name':'sara','family':'ahmadi'}
# user3={'name':'reza','family':'sadeghi'}

# users=[user1,user2,user3]

# print(users)

#22
# for i in range(1,10):
# for i in range(1,10,2):
#     print(i,end='->')

#23
# names=['ali','sara','amir','narges','reza']
# # for i in range(len(names)):
# #     print(names[i])
# for n in names:
#     print(n)

#24
# numbers=[3,9,12,8,-3,6,11]
# for n in numbers:
#     if n%2==0:
#         print(n,end=' ')

#25
# n=100
# while n>0:
#     print(n,end=' ')
#     #n+=1
#     n=int(n/2)

#26
# names=[]
# while True:
#     n=input('enter name : ')
#     n=n.strip()
#     if len(n)>0:
#         names.append(n)
#     else:
#         break
#     print(names)

# print(names)
# print('end')


#27
# from random import randrange
# n=randrange(1,101)
# a=0
# while a!=n:
#     a=int(input('enter number 1 to 100'))
#     if a>n:
#         print('down')
#     elif a<n:
#         print('up')

# print('win')

#28
# numbers=list(range(1,101))
# for i in numbers:
#     #1
#     # if i==50:
#     #     break
#     #2
#     if i%5==0:
#         continue
#     print(i,end=' ')

#29
n='   Hello World, python   '
print(len(n))
print(len(n.strip()))
print(len(n.lstrip()))
print(len(n.rstrip()))
print(n.lower())
print(n.upper())
print(n.title())
print(n.replace('l','*'))
print(n.replace('Hello','Hi'))
print(n.index('o'))
print(n.index('or'))
print(n.find('l'))
print(n.find('z'))
print(n.isdigit())
print(n.isspace())
print(n.strip().capitalize())
print(n.count('l'))
print(n[6:10:1])

