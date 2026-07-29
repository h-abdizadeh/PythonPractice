#1
# print('hello python')
# print(4+5)
# print(7-9)
# print(3*2)
# print(8/3)

#2
# print(7/3)
# print(7//3)
# print(7%3)
# print(2**3)
# print(8%2)

#3
# print(7>5)
# print(7==5)
# print(4<=5)
# print(8!=3)
# print('a'=='A')
# print('reza'>'sara')

#4
# n=7
# print('n')
# print(n)
# print(n*2)

#5
# print(4+5)
# print('4+5')
# print('4'+'5')
## print('4'+5)
# print('4',5)
# print('4'+str(5))
# print(int('4')+5)

#6
# print(7/3)
# print(int(7/3))
# print(int(3/2))
# print(5)
# print(float(5))

#7
# print(bool(2))
# print(bool(0))
# print(bool(-1.5))
# print(bool('hello'))
# print(bool(''))
# print(bool(' '))

#8
# n=7
# m=2.5
# print(n+m)
# print('n'+'m')
# print(n<m)
# m=m/n
# print(int(m))

#9
#1
# n=int(input('enter number : '))
# print(2**n)
#2
# n=input('enter number : ')
# print(2**int(n))
# print('farda'*5)

# 10
# age=int(input('age : '))
# print('month:',age*12)
# print(age*365)
# print(age*365*24)

#11
# n=input('name : ')
# print('hello')
# print(n*10)

#12
# n=int(input('number : '))
# print(n*10)

#13
# just_minute=int(input('enter just a minute :'))
# hours=just_minute//60
# minute=just_minute%60
# print(hours,':',minute)

#14
# float_div=7/3
# int_div=7//3
# after_point=float_div-int_div
# print(after_point)

#15
# import math
# n=math.modf(7/3)
# print(n)

#16
# password='abc123'
# userpass=input('password : ')

# if password==userpass:
#     print('ok')
# else:
#     print('wrong')

#17
# n=float(input('number : '))
# if n>=12:
#     print('ok')
# else:
#     print(n+2)

#18
# from random import randint
# randomnum=randint(1,6)
# usernum=int(input('enter an integer: '))
# if randomnum==usernum:
#     print('ok')
# else:
#     print(randomnum)

#19
# n=int(input('number : '))
# if n>0:
#     print('+')
# elif n<0:
#     print('-')
# else:
#     print('zero')

#20
# import winsound
# color=input('color : ').lower()#.upper()
# if color == 'red':
#     print('stop')
# elif color == 'green':
#     print('go')
# elif color == 'yellow':
#     print('slow')
# else:
#     print('alarm')
#     winsound.Beep(3500,1000)

#21
# p=float(input('price: '))
# o=0
# if p>100000:
#     o=20
# elif p>50000:
#     o=15
# elif p>10000:
#     o=10
# print(p-(p*o)/100)

#21
# phone=input('phone number : ')
# if len(phone)is 11:#==
#     if phone.isdigit()==True:
#         if phone.startswith('09'):
#             print('valid phone')
#         else:
#             print('error 09')
#     else:
#         print('error digits')
# else:
#     print('error 11')

# # 22
# phone = input('phone : ')

# if len(phone)==11 and phone.isdigit() and phone.startswith('09'):
#     print('verify')
# else:
#     print('invalid')

#23
# n=float(input('number1 '))
# m=float(input('number2 '))
# if n>=12 or m>=12:
#     print('true')
# else :
#     print(m)

#24
# try:
#  n=int(input('n: '))
#  print(2**n)
# except:
#  print('error')

# 25
# numbers=[5,8,12,-3,11]
# names=['amirAli','yazdan','maryam','fatemeh','sorena','mahshid']
# #1
# # print(numbers)
# # print(*numbers)
# # print(names[2])
# # print(names[-3])
# #2
# # names[0]=names[-1]
# # print(names)
# #3
# # print(max(numbers))
# # print(min(numbers))
# # print(sum(numbers))
# # print(sum(numbers)/len(numbers))
# # names[0],names[5]=names[5],names[0]
# # print(names)
# temp=names[0]
# names[0]=names[5]
# names[5]=temp
# print(names)

#26
# names=['amirAli','yazdan','maryam','fatemeh','sorena','mahshid']
# #1
# # names.sort()
# # # names.sort(reverse=True)
# # print(names)
# #2
# # # print(sorted(names))
# # print(sorted(names,reverse=True))
# # print(names)
# #3
# # names.reverse()
# print(reversed(names))
# print(*reversed(names),sep=', ')
# print(names)

#27
# names=[]
# names.append('amir')
# names.append('sara')
# names.insert(0,'tanaz')
# names.insert(2,'maryam')
# print(names)

#28
# print('a' in 'ali')
# print('n' in 'ali')
# print('ali' in 'alireza')
# print('ali' in ['ali','reza'])
# print('sara' in ['ali','reza'])

#29 az ki
# from random import choice
# names=['amirAli','yazdan','maryam','fatemeh','sorena','mahshid']
# print(choice(names))

#30
# names=['amirAli','yazdan','maryam','fatemeh','sorena','mahshid']
# a=input('name :')
# if a not in names:
#     names.append(a)
# else:
#     # print('exists')
#     names.remove(a)

# print(names)

#31
# numbers=[12,8,21,-4,8,10]
# print(numbers)
# #
# # numbers.remove(8)#remove(value)
# # del numbers[3]#list[indice]
# # temp=numbers.pop()#last item
# # temp=numbers.pop(2)#indice
# temp=numbers.pop(-2)#indice
# print(temp)
# print(numbers)


#32
# names=['amirAli','yazdan','maryam','fatemeh','sorena','mahshid']
# result=filter(lambda n: len(n)>=6, names)
# print(result)
# print(list(result))

#33
# names=['amirAli','yazdan','maryam','fatemeh','sorena','mahshid']
# word=input('enter a word : ')
# result=list(filter(lambda i: word in i,names))

# if len(result)>0:
#     print(result)
# else:
#     print('not found')

#34 maryam ######################### map() ###### go to 50
# prices=[150,200,350,100,400,50,250]
# ts=int(input('please enter number:'))
# result=filter(lambda n: n<ts, prices)
# filtered_price=[price for price in prices]
#################################################

#36
# print(range(5))
# print(*range(5))
# print(*range(3,10))
# print(*range(3,10,2))
# print(*range(5,1))
# print(*range(5,1,-1))
# print(*range(5,1,-2))

# 37
# import random
# even_numbers=list(range(1000,10000,2))
# number=random.choice(even_numbers)
# print(number)

#38
# import random 
# names=['ali','sara','reza','maryam','zahra','sina']
# # winners=random.sample(names,6)
# winners=random.sample(names,len(names))
# print(winners)

#39
# import random
# # print(random.randrange(1000,10000,2))
# # print(random.choice(range(1,10)))
# # print(random.randint(10,20))#10 to 20
# # print(random.random())
# print(random.sample(range(1,10),9))
# print(random.choices(range(1,10),k=9))
# print(random.uniform(2.5,5.5))
# mylist=list(range(1,10))
# random.shuffle(mylist)
# print(mylist)

#40
# myTuple=('amir',21)
# print(myTuple)
# print(*myTuple)
# print(myTuple[0])
# print(type(myTuple))
# print(type(myTuple[1]))
## myTuple[1]=18

#41
# myDict={'name':'amir','age':21}
# print(myDict)
# print(*myDict)
# print(myDict['name'])
# print(myDict.values())
# print(myDict.keys())
# myDict['name']='sara'
# myDict['phone']='0911'
# print(myDict)

#42
# tupleList=[('ali',16),('reza',18),('sara',15)]
# dictList=[{'name':'ali','age':16},
#           {'name':'reza','age':18},
#           {'name':'sara','age':15}]
# print(tupleList[0][1])
# print(dictList[0]['name'])

#43
# names=['ali','amir','sara','ava']
# for n in names:
#     print(n,end='\t')

#44
# for i in range(1,101):
#     if i%2==0:
#         print(i,end='\t')

#45
# for n in 'hello world, python':
#     #1
#     # if n=='o':
#     #     print('*')
#     # else:
#     #     print(n)
#     #2
#     if n=='o':
#         n='*'
#     print(n,end='')
#     #3
#     # if 'o' in n:
#     #     n='*'
#     # print(n)

#46
# mystr='hello world, python'
# for n in range(0,len(mystr)):
#     if n%2:
#         print(mystr[n].upper(),end='')
#     else:
#         print(mystr[n].lower(),end='')

#47
# i=0
# for n in 'hello world, python':
#     if i%2==0:
#         print(n.lower(),end='')
#     else:
#         print(n.upper(),end='')
#     i+=1#i=i+1

#48
# row=int(input('row : '))
# column=int(input('column : '))

# for i in range(1,row+1):
#     for j in range(1,column+1):
#         print(i*j,end='\t')
#     print()

#49
# import random
# randnum=random.randint(1,100)
# guess=0
# while guess!=randnum:
#     guess=int(input('guess a number between 1 to 100: '))
#     if guess<randnum:
#         print('more!')
#     elif guess>randnum:
#         print('less!')
    
# print('excellent!')

#50
# prices=[150,200,350,100,400,50,250]
# ts=int(input('please enter number:'))
# filterPrice=filter(lambda n: n<ts, prices)
# result=[p*0.9 for p in filterPrice]
# print(result)

#51
# for i in range(1,10):
#     if i%3==0:
#         # break
#         # continue
#         pass
#     print(i)

# print('end')

#52
# import math
# print(math.pow(2,3))
# print(math.sqrt(64))
# print(math.e)
# print(math.pi)
# print(math.sin(90))
# print(math.cos(90))
# print(math.tan(90))
# print(math.log2(256))
# print(math.log10(10000))

#53
# import random
# randnum=random.randint(1,100)
# for i in range(1,6):
#     guess=int(input('guess a number: '))
#     if randnum==guess:
#         print('you won the game')
#         break
#     elif guess<randnum:
#         print('higher')
#     elif guess>randnum:
#         print('lower')
# else:
#     print('game over, the random number: ',randnum)

# # if guess!=randnum:
# #     print('game over, the random number: ',randnum)

#54
# setA={5,3,-2,11}
# setB={8,11,-3,5}
# print(setA)
# print(*setA)
# print(list(setA)[2])
# print(setA.intersection(setB))
# print(setA & setB)
# print(setA.union(setB))
# print(setA | setB)
# print(setA.difference(setB))
# print(setA - setB)
# print(setB.difference(setA))
# print(setB - setA)
# setA.add(-6)
# print(setA)
# setB.remove(-3)
# print(setB)

#55
# try:
#     n=int(input('number : '))
#     print(10/n)
# except Exception as error:
#     # print('error')
#     # print(error)
#     pass

#56
# mystr='     hello world, PYTHON     '
# print(mystr)
# print(len(mystr))
# print(mystr.strip())
# print(len(mystr.strip()))
# print(mystr.strip().upper())
# print(mystr.lower())
# print(mystr.title())
# print(mystr.swapcase())
# print(mystr.replace('o','*'))
# print(mystr.replace('hello','hi'))
# print(mystr.index('o'))
# # print(mystr.index('z'))
# print(mystr.find('o'))
# print(mystr.find('z'))
# print(mystr.count('l'))
# print(mystr.strip().split(' '))
# print(mystr.strip().split(','))

#57
# color=input('color : ')

# match(color):
#     case 'red':
#         print('stop')
#     case 'green':
#         print('go')
#     case 'yellow':
#         print('slow')
#     case _ :
#         print('alarm')
#         import winsound
#         winsound.Beep(700,500)

#58
# mylist=[4,7,-3,11,3,1]
# print(mylist[1:4])#1 to 3
# print(mylist[2:])#2 to end
# print(mylist[:3])#0 to 2
# print(mylist[:])#0 to end
# print(mylist[-5:-2])#-5(1) to -3(3)

#59
# listA=[1,3,5,7]
# listB=[2,4,5,9]
# copyA=listA[:]
# copyB=listB

# copyA.append(11)
# copyB.append(11)

# listA.remove(5)
# listB.remove(5)

# print(listA,copyA)
# print(listB,copyB)

#60
# mylist=[2,5,7,-1]
# temp=(5,11,9,8)
# mylist.extend(temp)
# print(mylist)

# #61
# user_sentence=input('enter a sentence')
# if ',' in user_sentence:
#     comma_sentence=user_sentence.split(',')[0]
#     print(comma_sentence)
# else:
#     print('YOUR SENTENCE DOESN\'T HAVE ANY COMMA !!!')    
#62
# user=input('enter a sentence: ')
# indice=user.find(',')
# if indice>=0:
#     print(user[:indice])
# else:
#     print('YOUR SENTENCE DOESN\'T HAVE ANY COMMA !!!')  

#63
# userstr=input('write something : ')
# for i in userstr:
#     if i==',':
#         break
#     print(i,end='')

#64
