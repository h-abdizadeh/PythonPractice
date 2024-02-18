# 1
# print('mohandesi farda')
# print(5+12)
# print(5-11)
# print(3*4)
# print(12/7)

# print(2**4)

# print(7>2)
# print(6<3)

# print(5+7)
# print('5+7')
# print('5'+'7')

#2
# name='ali'
# family='ahmadi'
# age=23

# print(name)
# print('name')
# print(name+' '+family)
# print(name+' '+family+' '+str(age))

#3
# print(str(3)+str(5))
# print(int('3')+int('5'))
# # print(int('ali'))#error
# print(7/5)
# print(int(7/5))
# print(7%5)
# print(8%2)
# print(2)
# print(float(2))
# print(int(2.5))

#4
# name=input('enter fisrt name : ')
# family=input('enter last name : ')

# print('name is : '+name+' '+family)
# print(f'name is : {name} {family}')

#5
# n=float(input('enter number : '))
# m=float(input('enter number : '))

# print(n+m)
# print(n-m)
# print(n*m)
# print(n/m)

#6
# import winsound 
# password='abc123'
# userPass=input('enter password : ')

# if password==userPass:
#     print('YES')
# else:
#     print('NO')
#     winsound.Beep(780,2000)

#7
# n=int(input('enter number : '))

# if n<10:
#     print(n+10)
# else:
#     print(n-10)

#8
# number=int(input('enter number : '))

# if number%2==0:
#     print('even')
# else:
#     print('odd')

#9
# color=input('enter color : ').lower()
# # print(color.lower())
# # print(color.upper())
# # color=color.lower()

# if color=='red':
#     print('STOP')
# elif color=='green':
#     print('GO')
# elif color=='yellow':
#     print('SLOW')
# else:
#     import winsound
#     winsound.Beep(2500,1000)

#10
# n=float(input('enter score : '))

# if n>=18:
#     print('A')
# elif n>=15:
#     print('B')
# elif n>=12:
#     print('C')
# else:
#     print('D')

#11
# password='abc123'
# code=1234

# #A
# # userPass=input('enter password : ')
# # if password==userPass:
# #     userCode=int(input('enter code : '))
# #     if code==userCode:
# #         print('Ok')

# #B
# userPass=input('enter Password : ')
# userCode=int(input('enter code : '))

# # if password==userPass and code==userCode:
# #     print('Ok')
# if password==userPass or code==userCode:
#     print('Ok')


#12
# mylist=['ali','sara','amir','maryam','parsa']
# print(mylist)
# print(*mylist)
# print(*mylist,sep='-')
# print(mylist[2])
# # print(mylist[5])#error
# print(mylist[-1])
# print(len(mylist))

#13
# numbers=[3,7,-1,3,11]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print((numbers))
# print(sum(numbers)/len(numbers))
# print(numbers.count(3))
# print(numbers.count(9))
# print(numbers.index(7))
# print(numbers.index(3))
# numbers.sort(reverse=True)
# print(numbers)

#14
# numbers=[3,7,-1,3,11]
# print(sorted(numbers,reverse=True))
# print(numbers)

# numbers.reverse()
# print(numbers)

#15
# names=[]
# print(names)

# names.append('ali')
# names.append('sara')
# names.append('amir')
# # names.append(input('enter name : '))
# names.insert(1,'amir')
# names.insert(0,'maryam')
# names.insert(len(names),'mehdi')
# # print(names)
# del names[3]
# names.remove('amir')
# temp=names.pop()
# print(temp)
# temp=names.pop(1)
# print(temp)
# print(names)

#16
# numbers=[3,9,-1,3,8]
# #in
# print(9 in numbers)
# print(11 in numbers)
# if -1 in numbers:
#     numbers.remove(-1)

# print(numbers)

#17
# list1=[]
# list2=[2,5,9]

# if list1:
#     print(list1)
# else:
#     print('empty')

# if list2:
#     print(list2)
# else:
#     print('empty')

#18
# print(list(range(10)))
# print(list(range(1,10)))
# print(list(range(1,10,2)))
# print(list(range(10,0,-1)))
# print(list(range(10,0,-2)))

#19
# from random import randrange
# print(randrange(1,10))
# print(randrange(1000,10000))

#20
# from random import randrange
# names=['tina','ali','amir reza','iliya',
#        'mohammad amin','amir reza','parsa']
# #1
# index=randrange(0,len(names))
# print(index)
# print(names[index])
# # #2
# # index=randrange(0,len(names))
# # print(index)
# # print(names[index])
# # #3
# # index=randrange(0,len(names))
# # print(index)
# # print(names[index])

#21
# from random import randrange
# names=['tina','ali','amir reza','iliya',
#        'mohammad amin','amir reza','parsa']

# for n in range(0,7):
#     i=randrange(len(names))
#     print(f"index {i} ==> {names[i]}")
#     # print("index "+i+" ==> "+names[i])
#     del names[i]

#22 tuple
# user=('ali','ahmadi',26)
# print(user)
# print(*user)
# print(user[0])
# # user.append('09112223344')#error
# # user[3]='09112223344'#error
# # user[1]='asadi'#error
# print(*user)
# print(type(user))
# user2=('sara','amiri',24)
# mylist=[user,user2]
# print(*mylist,sep='\n')

# inputTuple=(input('enter name : '), 
#             input('enter family : '))
# print(inputTuple)

#23
# user={'name':'ali',
#       'family':'amiri',
#       'age':32}

# print(user)
# print(*user)
# print(user['family'])

# user['phone']='0911'
# print(user)

# user['family']='sadeghi'
# print(user)

#24
# setA={5,8,3,12}
# setB={10,8,4,9}
# print(setA)
# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setB.difference(setA))
# setA.remove(5)
# setA.add(11)
# print(setA)
# print(max(setA))

# review #
#1
# name='ali'
# print(name*3)
# print(3*name)
# print('name is : {name}')
# print(f'name is : {name}')

#2
# n=0
# print(n>0)
# print(n>=0)
# print(not n==0)

#3
# mylist=['ali','sara','amir','maryam','parsa']
# print(mylist)
# temp=mylist.pop()
 
# print(temp)
# print(mylist) 

#4
# dict={'name':'ali','family':'amiri'}
# print(dict['family'])
# #print(dict[0])#error

#5
# A={'ali','amir'}
# B={'ali','sara'}
# print(A.union(B))

#25 filter lambda
# score=[12.5,15,14.25,8,17.5,18,15,19,6.75,20]
# f=filter(lambda n: n<10, score)
# lst=list(f)
# print(f)
# print(lst)
# print(len(lst))

# result=list(filter(lambda n: n>=15,score))
# print(result)
# print(*result, sep=' - ')
# print(len(result))

#26
# score=[12.5,15,14.25,8,17.5,18,15,19,6.75,20]
# #1
# # lst1=list(filter(lambda n: n>10, score))
# # lst2=list(filter(lambda n: n<15, lst1))
# # print(lst2)

# #2
# # result=list(filter(lambda n: n>10 and n<15, score))
# # print(result)

# #3
# result=list(filter(lambda s: s>15 or s<10, score))
# print(result)

#27 for
# myStr='hello world, python'
# for n in myStr:
#     # print(n.upper(),end='')
#     if n=='o':
#         print(n.upper(),end='')
#     else:
#         print(n,end='')


#28   
# myStr='hello world, python'
# #HeLlO wOrLd, PyThOn
# i=0
# for n in myStr:
#     if i%2==0:
#         print(n.upper(),end='')
#     else:
#         print(n.lower(),end='')
#     i+=1

#29
# names=['ali','amir','sadegh','mehdi','reza']
# # for
# for n in names:
#     if 'r' in n:
#         print(n)
# # lambda
# result=filter(lambda n: 'r' in n,names)
# print(list(result))

#30
# price=[15000,37500,5000,23000,20000]
# # 1
# # i=0
# # for n in price:
# #     if n<=15000:
# #         finalprice=n-(n*10/100)
# #         price[i]=finalprice
# #     i+=1

# #2
# for i in range(0,len(price)):
#     if price[i]<=15000:
#         p=price[i]
#         p=p-(p*10/100)
#         price[i]=p

# print(price)

#31
# myStr="Hello World, Python"
# for n in myStr:
#     if n=='o':
#         # break
#         # continue (just in loop)
#         pass
#     print(n,end='')
        
#32
# n=374
# while n>0:
#     print(n%10)
#     n=int(n/10)

#33
from random import randrange
while True:
    print(randrange(1000,10000),end='\t')
