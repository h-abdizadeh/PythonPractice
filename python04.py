#1
# print('hello')
# print(7+5)
# print(8-3)
# print(6*2)
# print(14/4)
# print(5>3)
# print(8<2)
# print('ali'>'reza')
# print('amir'>'ali')

#2
# n=5
# m=7
# print(n)
# print('n')
# print(n+m)
# print('n+m')
# print('n'+'m')
# print("15"*3)

#3
# name=input('enter first name : ')
# family=input('enter last name : ')
# print(name+' '+family)

#4
# n=5
# m=7
# print(5+7)
# print('result = '+str(5+7))
# print(str(9)+str(3))
# print(str(n)+str(m))
# print(int(2.5)+int(3.75))
# print(14/8)
# print(int(14/8))
# print(13%5)
# print(12%6)
# print(int(2))
# print(float(2))

#5
# n=float(input('enter number : '))
# m=float(input('enter number : '))
# print(n+m)
# print(n-m)
# print(n*m)
# print(n/m)

#6
# if 5>2:
#     print('yes')
# else:
#     print('no')

#7
# password='abc123'
# userPass=input('enter password : ')

# if password==userPass:
#     print('OK')
# else:
#     print('WRONG')

#8
# n=int(input('enter number : '))

# if n%2==0:
#     print('even')
# else:
#     print('odd')

#9
# number=int(input('enter number : '))

# if number<10:
#     print('one digit')
# else:
#     print('invalid')

#10
# color=input('enter color : ')

# if color=='red':
#     print('STOP')
# elif color=='green':
#     print('GO')
# elif color=='yellow':
#     print('SLOW')
# else:
#     print('ALARM')
#     import winsound
#     winsound.Beep(700,5000)

#11
# n=float(input('enter score : '))
# p=input('enter project [yes/no] :')

# # if n>=17 and p=='yes':
# if n>15 or p=='yes':
#     print('accept')
# else:
#     print('failed')

#12
# names=['melina','sepanta','amirhossein']
# print(names)
# print(*names)
# print(*names,sep=',')
# print(names[1])

#13
# from random import randrange
# print(randrange(100))#0 -> 99
# print(randrange(10,100))#10 -> 99

#14
# from random import randrange
# names=['melina','sepanta','amirhossein']
# i=randrange(0,3)
# print(i)
# print(names[i])

#15
# names=['ali','sara','amir','reza','maryam']
# numbers=[12,-1,2,9,2,10]
# print(names[3])
# print(names[-1])
# print(len(names))
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(names))
# print(sorted(numbers))
# print(sorted(names,reverse=True))
# print(sorted(numbers,reverse=True))

#16
# names=['ali','sara','amir','reza','maryam']
# numbers=[12,-1,2,9,2,10]
# # names.sort()
# # print(names)
# # numbers.sort()
# # print(numbers)
# # names.sort(reverse=True)
# # print(names)
# names.reverse()
# print(names)

#17 slice
# names=['ali','sara','amir','reza','maryam']
# numbers=[12,-1,2,9,2,10]
# print(names[1:4])
# print(names[:4])
# print(names[2:])
# print(names[:])

#18
# names=[]
# print(type(names))
# print(names)

# names.append('narges')
# # names.append(input('enter name : '))
# names.append('amir')
# names.append('reza')
# names.insert(0,'ali')
# names.insert(2,'sara')
# names.insert(len(names),'maryam')
# print(names)

#19
# names=['ali','amir','sara','maryam','amir']
# print(names)

# # del names[3]
# # names.remove('ali')
# # names.remove('Ali'.lower())#.upper()
# # names.remove('amir')
# # print(names.pop())
# # n=names.pop()
# # print(names)
# # names.append(n)
# print(names.pop(2))
# print(names)

#20
# names=['ali','amir','sara','maryam','amir']
# print('ali' in names)
# print('narges' in names)

# if 'narges' in names:
#     names.remove('narges')

# print(names)

#21
# text='hello world, python'
# print('or' in text)
# print('remove' in text)

#22
# names=[12,15,9]#names[]
# if names:
#     print(len(names))

#23
# print(range(10))
# print(*range(10))
# print(*range(5,20))
# print(*range(10,50,5))
# print(*range(10,2,-1))
# print(*range(50,10,-5))
# print(*range(50,-50,-10))

####### review ######
#1
# # print('ali'*'reza')#error
# print(2*'ali')

#2
# name='amir'
# family='ahmadi'

# print('user name '+name+' '+family+'...')
# print(f'user name {name} {family}...')

#3
# print(-1*5)
# print(-1*-5)
# print(5>2)
# print(not 5>2)
# print(6>10)
# print(not 6>10)

#4
# n=[3,5,2,-2]
# print(max(n))
# print(max(range(10,100,2)))

# from random import randrange
# print(randrange(10,100,2))

#5
# print(range(5,50,2))
# print(list(range(5,56,2)))

####### review ######

#24 filter
# score=[14,12,18,17,16,5,12,18,20,18,1,7,14,18,16,19,11,15]
# #1
# # f=filter(lambda n:n>=18,score)
# # print(f)
# # result=list(f)
# # print(result)
# # print(len(result))
# # print(max(result))

# #2 practice #1
# print(score)
# # f=list(filter(lambda n: n>=10,score))
# # f=list(filter(lambda n: n<15,f))
# # print(f)

# #2
# f=filter(lambda n:n>=10 and n<15,score)
# print(list(f))

#25 tuple
# tuple1=('ali','amiri',35)
# print(tuple1)
# print(*tuple1)
# print(tuple1[1])

#26
# user=(input('enter name : '),
#       input('enter family'),
#       input('enter phone : '))

# print(user)

#27
# list1=[5,8,12]
# print(list1)
# print(tuple(list1))

#28
# user1=('reza','asadi')
# user2=('sara','sadeghi')
# listUser=[user1,user2]
# print(listUser)
# print(listUser[0])
# print(listUser[0][1])
# print(listUser[1][0])

#29 dictionary
# dict1={'name':'ali', 'family':'asadi'}
# print(dict1)
# print(*dict1)
# print(dict1['family'])
# print(dict1['family'])

# dict1['age']=35
# print(dict1)

#30
# dict1={'name': 'ali','age':37}
# dict2={'name': 'reza','age':32}

# myLsit=[dict1,dict2]
# print(myLsit)
# print(myLsit[0])
# print(myLsit[1]['age'])

#31 set
# setA={1,2,5,7}
# setB={3,5,9,7}
# # print(setA)
# # print(*setA)
# print(list(setA)[2])
# # print(setA.union(setB))
# # print(setA.intersection(setB))
# # print(setA.difference(setB))
# # print(setB.difference(setA))

# # #1
# # u=setA.union(setB)
# # print(u)
# # i=setA.intersection(setB)
# # # print(u-i)
# # print(u.difference(i))

# # #2
# # print(setA.union(setB).difference(setA.intersection(setB)))

#32
myStr='hello world, python'
for n in myStr:
    if n=='o':
        print(n.upper(),end='')
    else:
        print(n,end='')


