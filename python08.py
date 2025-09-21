# 1
# print('hello python')
# print(7+3)
# print(12-4)
# print(7/2)
# print(3*6)

# 2
# print(8%2)
# print(7%2)
# print(5**3)

# 3
# print(5>3)
# print(12==5)
# print('sara'<'amir')
# print('a'=='A')

# 4
# print('4+5')
# print('4'+'5')
# print(4+5)
# print(4*'5')
# print(6*'maharat')

# 5
# n=10
# m=7
# print('n'+'m')
# print(n+m)
# print('n'<'m')
# print(n<m)

#6
# n=input('enter name : ')
# print(n)

#7
# a=input('enter number 1 : ')
# b=input('enter number 2 : ')
# print(a+b)
# print(int(a)+int(b))
# print(int(a)*int(b))

#8
# a=float(input('enter number : '))
# b=float(input('enter number : '))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

#9
# age=int(input('enter age : '))
# print(age*365)
# print('days = '+str(age*365))
# print('days = ',age*365)
# print(f'days = {age*365}')

#10
# num=int(input('enter number : '))
# print(f'{num/60} hour : {num%60} minute')
# print(f'{int(num/60)} hour : {num%60} minute')
# print(f'{num//60} hour : {num%60} minute')

#11
# price=int(input('enter price : '))
# off=int(input('enter sellOff : '))

# n=off*price/100
# price(price-n)

#12
# password='abc123'
# userpass=input('enter password : ')

# if password==userpass:
#     print('ok')
# else:
#     print('wrong')

# 13
# number=float(input('enter number : '))
# if number>=10:
#     print('yes')
# else:
#     print('no')

#14
# from random import randint
# goal=randint(1,6)
# guess=int(input('enter guess [1 to 6] : '))

# if guess==goal:
#     print('win')
# else:
#     print('lose')
#     print(f'goal -> {goal}') 

#15
# number =int(input('enter number : '))
# if number%2==0:
#     print('even')
# else:
#     print('odd')

#16
# n=int(input('input number : '))
# if n>0:
#     print('+')
# elif n<0:
#     print('-')
# else:
#     print(0)

#17
# from winsound import Beep
# color=input('enter color : ').lower()
# print(color.upper())
# print(color.lower())
# if color=='red':
#     print('stop')
# elif color=='green':
#     print('go')
# elif color=='yellow':
#     print('slow')
# else:
#     print('alarm')
#     Beep(1000,2500)

#18
# color=input('enter color : ').lower()

# match color:
#     case 'red': 
#         print('stop')
#     case 'yellow': 
#         print('slow')
#     case 'green': 
#         print('go')
#     case _ : 
#         print('alarm')

#19
# n=input('enter 1 to 4 :')
# match n:
#     case '1': print('bahar')
#     case '2': print('tabestan')
#     case '3': print('paeiz')
#     case '4': print('zemestan')
#     case _: print('...')

#20
# n=float(input('input : '))
# #1
# # if n>=10:
# #     if n<=20:
# #         print('Yes')
# #2
# # if n>=10 and n<=20:
# #     print('Yes')
# #3
# if 10<=n<=20:
#     print('Yes')

#21
# n=int(input('enter number : '))
# # if n<=-10 or n>=10:
# if n<-9 or n>9:
#     print('valid')
# else:
#     print('invalid')

#22
# # n=int(input('enter age : '))
# # print(n*365)

# try:
#     #code
#     n=int(input('enter age : '))
#     print(n*365)
#     # print(100/n)
# except Exception as e:
#     #error
#     # print('error')
#     print(e)

#23
# names=['amir','sara','reza','ava','narges']
# # print(names)
# # print(*names)
# # print(*names,sep='-')
# # print(*names,sep='\n')#enter
# # print(*names,sep='\t')#tab
# # print(names[0])
# # print(names[2])
# # print(names[-1])
# # print(names[-2])
# names[2]='ali'
# print(names)
# print(len(names))

#24
# mylist=[12,8,-1,11,-7,15,5]
# print(min(mylist))
# print(max(mylist))
# print(sum(mylist))
# print(sum(mylist)/len(mylist))
# i=len(mylist)//2
# print(mylist[i])

#25
# names=['sara','amir','ava','reza','arman']
# #list[start:end]#end-1
# print(names[1:3])#3-1
# print(names[0:3])
# print(names[:3])
# print(names[2:])
# print(names[:])
# print(names[2:len(names)])

#26
# names=['sara','amir','ava','reza','arman']
# print(sorted(names))
# print(sorted(names,reverse=True))
# print(names)
# # names.sort()
# # names.sort(reverse=True)
# names.reverse()
# print(names)

#27
# mylist=[]
# mylist.append('amir')
# mylist.append('narges')
# mylist.append('ali')
# mylist.insert(0,'ava')
# mylist.insert(3,'arman')
# mylist.insert(len(mylist),'mani')
# print(mylist)

#28
# mylist=['amir','reza','sara','ava','mani','reza']
# print(mylist)
# del mylist[2]
# mylist.remove('reza')
# # mylist.remove('ali')#error
# mylist.pop()
# n=mylist.pop(0)
# print(mylist)
# print(n)

#29
# print(bool(0))
# print(bool(2))
# print(bool(-3.5))
# print(bool(''))
# print(bool('  '))
# print(bool('abc'))
# print(len(''))
# print(len('   '))
# print(bool([]))
# print(bool([2,3,-1]))
# print(bool(['sara']))

#30
# a=[]
# b=[1,2,3]

# if b:
#     a.append(b.pop())

# print(a)
# print(b)

#31
# print('a' in 'sara')
# print('m' in 'narges')
# print('python' in 'hellopython')
# # print(1 in 213)#error
# print('sara' in ['ava','narges','sara'])
# print('amir' in ['ali','reza','arad'])

#32
# names=['sara','amir','reza','ava','narges']
# n=input('name : ')
# if n in names:
#     names.remove(n)
# else:
#     names.append(n)

# print(names)

#33
# listA=[1,7,8,-3,9]
# listB=listA
# listC=listA[:]
# #1
# # listB.pop()
# # # listA.append(5)
# # print(listA)
# # print(listB)
# #2
# listC.pop()
# # listA.append(5)
# print(listA)
# print(listC)

#34
# print(range(5))
# print(*range(5))
# print(list(range(5)))
# print(*range(10,100))
# print(*range(10,100,2))
# print(*range(-10,-100,-2))
# print(*range(-98,-9,2))

#34
# import random
# print(random.randrange(100))
# print(random.randrange(1000,10000))
# print(random.randrange(1000,10000,2))
# print(random.randint(100,200))
# print(random.choice(range(100)))
# print(random.choice(['sara','amir','ava','reza']))
# print(random.sample(range(10),3))
# mylist=['sara','amir','reza','ava','narges']
# print(random.sample(mylist,2))
# print(random.choices(range(10),k=3))
# print(random.choices(mylist,k=3))
# print(random.sample(range(10),10))
# print(random.choices(range(10),k=11))

# 35
# # import random
# from random import randrange
# print(randrange(100))

#36 tuple
# book=('python','maharat',1500)
# print(book)
# print(*book)
# print(book[1])
# # book[0]='csharp'

#37
# student=(input('name : '),input('family : '))
# print(student)

#38 Dict
# person={'name':'ali', 'age':17}
# print(person)
# # print(*person)
# # print(person['age'])
# # print(person.values())
# # print(*person.values())
# # person['age']=23
# person['family']='ahmadi'
# person.pop('age')
# print(person)

# 39
# listA=[('amir',17),('sara',21)]
# listB=[{'name':'amir', 'age':17},{'name':'sara', 'age':21}]
# 1
# print(listA)
# print(*listA)
# print(listA[0])
# print(listA[1][1])
# 2
# print(listB[0]['age'])

#40 set
# setA={5,-3,11,9,3}
# setB={7,9,-8,1,-3}

# print(setA)
# print(*setA)
# print(setB)
# # print(setB[2])#error
# print(list(setB)[1])
# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setB.difference(setA))
# print(setA | setB)#union(or)
# print(setA & setB)#intersection(and)
# print(setA - setB)#diffrence
# print(setB - setA)
# setA.add(32)
# print(setA)
# setB.remove(-3)
# print(setB)
# print(min(setA))
# print(max(setA))
# print(sum(setA))

#41
# setA={5,-3,11,9,3}
# setB={7,9,-8,1,-3}
# print( (setA | setB) - ( (setA-setB) | (setB-setA) ) )

# 42
# numbers=[14,12,15,17,20,15,12,18,20]
# # result=filter(lambda n : n>14,numbers)
# # result=filter(lambda n : n>12 and n<18,numbers)
# result=filter(lambda n : 12<n<18,numbers)
# # result=filter(lambda n : n%2==0,numbers)
# print(*result)

# 43 for
# names=['sara','amir','ava','reza']
# for i in names:
#     print(i)

# 44
# for n in range(5):
#     import random
#     print(random.randint(1000,10000))

# 45
# for e in 'hello python':
#     if e=='o':
#         print('*',end='')
#     else:
#         print(e,end='')

#46
# import random
# while True:
#     print(random.randrange(100,1000),end='\t')

# 47
# import random
# rnd=0
# while rnd !=222:
#     # rnd=random.randrange(100,1000)
#     rnd=random.randrange(100,1000,2)
#     print(rnd,end='\t')

# 48
# for i in range(1,100):
#     if i%2==0:
#         # break
#         # continue
#         pass
    
#     print(i,end=' ')

#49
# mystr='hello python'
# key=True
# for i in mystr:
#     if key:
#         print(i.upper(),end='')
#         key=False
#     else:
#         print(i.lower(),end='')
#         key=True

# 50
# from random import randint
# goal=randint(1,100)
# guess=0
# while guess!=goal:
#     guess=int(input('enter guess [1 to 100]: '))
#     if guess>goal:
#         print('go down')
#     elif guess<goal:
#         print('go up')
#     else:
#         print('you win')

# 51
# mystr='     hello world, PYTHON     '
# print(mystr)
# print(len(mystr))
# print(mystr.strip())
# print(mystr.strip().upper())
# print(mystr.lower())
# print(mystr.title())
# print(mystr.swapcase())
# print(mystr.replace('world','WORLD'))
# print(mystr.replace(' ','*'))
# print(mystr.count('l'))
# print(mystr.count('hello'))
# print(mystr.find('hello'))
# print(mystr.index('o'))
# print(mystr.rindex('o'))
# print(mystr.capitalize())
# print(mystr.isalpha())
# print(mystr.isdigit())
# print('abc'.isalpha())
# print('123'.isdigit())
# print(mystr.isspace())
# print('   '.isspace())
# print(mystr[7:12])
# print(mystr[0:mystr.index(',')])

#52
# a=['hi',5,3+1]
# print(type(a[2:3]))

#53
# a=set([1,2,3])
# print(a.union([4,5]))
# print(a([4,5]))

