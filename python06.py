# 1
# print('hello world, python')
# print(5+4)
# print('5+4')
# print('5'+'4')
# print('nazanin'+'zazhra')
# # print(8-3)
# print(3*4)
# print(8/2)
# print(7/3)
# print(8%2)
# #print(7%3)
# print(17%3)
# print(2**3)

# 2
# print(7/3)
# print(int(7/3))
# # print(54+'farda')
# print(str(54)+'farda')
# print(7)
# print(float(7))

#3
# print(5>2)
# print(8>10)
# print('sogand'>'tania')
# print(5<5)
# print(5<=5)
# print(5>=5)
# print('sara'=='sara')
# print('sara'=='Sara')
# print('a'>'A')
# print(5!=3)
# print(5!=5)

#4
# n=7
# print(n)
# n='farda'
# print(n)
# n=7/3
# print(n)
# n=8>2
# print(n)

#5
# n=7
# m=3
# print(n+m)
# print('n+m')
# print('n'+'m')
# name='sara'
# # print(n+name)
# print(str(n)+name)
# print(m*name)
# print(10*'farda')

#6
# n=input('enter name : ')
# print(n)
# print(3*n)

#7
# n=input('enter name : ')
# m=input('enter family : ')
# print(n+m)
# print(n+' '+m) 

#8
# n=int(input('enter number : ')) 
# print(n*n)

#9
# n=int(input('enter number 1 : '))
# m=int(input('enter number 2 : '))
# print(n+m)
# print(n-m)
# print(n*m)
# print(n/m)

#10
# n=int(input('enter number : '))
# if n>10:
#     print(n-10)
# else:
#     print(n+10)

#11
# n=int(input('enter number : '))
# # print(n%2==0)
# if n%2==0:
#     print('even')
# else:
#     print('odd')

#12
# password='abc123'
# userPass=input('enter password : ')

# if userPass==password:
#     print('OK')
# else:
#     print('ERROR')

#13
# n=int(input('enter number : '))

# if n>0:
#     print('positive')
# elif n<0:
#     print('negative')
# else:
#     print('zero')

#14
# number=int(input('enter number : '))

# if number<10:
#     print('1 digit')
# elif number<100:
#     print('2 digit')
# elif number<1000:
#     print('3 digit')
# else:
#     print('more digit')    

#15
# num=input('enter number : ')
# # print(len(num))
# l=str(len(num))
# print(l+' character')
# print(f'{l} character')
# print(num.isdigit())

#16
# color=input('enter light color : ')
# #red  green yellow
# #STOP GO    SLOW
# if color=='red':
#     print('STOP')
# elif color=='green':
#     print('GO')
# elif color=='yellow':
#     print('SLOW')
# else:
#     print('ALARM')
#     import winsound
#     winsound.Beep(1500,5000) 

#17
# a=int(input('enter number : '))
# b=int(input('enter number : '))
# c=int(input('enter number : '))

# if a>b:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b>c:
#         print(b)
#     else:
#         print(c)

#18
# a=int(input('enter number : '))
# b=int(input('enter number : '))
# c=int(input('enter number : '))

# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

#19
# name='sareh'
# age=14
# print(name+str(age))
# print('first name is : '+name+' age : '+str(age))
# print(f'first name is : {name} age : {age}')

#20
# # name='sareh'
# names=['melika','fatemeh','sara','sareh','parnian','sogand','tania','ava']
# print(names)
# print(*names)
# print(*names,sep=' / ')

#21
# numbers=[12,8,13,9,-5,6,10]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(len(numbers))
# average=sum(numbers)/len(numbers)
# print(average)

#22
# numbers=[12,8,13,9,-5,6,10]
# print(numbers)
# print(numbers[3])
# print(numbers[5])
# # print(numbers[7])#error
# print(numbers[len(numbers)-1])
# print(numbers[-1])
# print(numbers[-2])

#23
# numbers=[12,8,13,9,-5,6,10]
# names=['melika','fatemeh','sara','sareh','parnian','sogand','tania','ava']
# print(8 in numbers)
# print(3 in numbers)
# print('sara' in names)
# print('maryam' in names)
# print('m' in 'fatemeh')
# print('n' in 'melika')
# # print(3 in 1583)#error
# # print(9 in str(1583))#error

##### empty list index 0
# mylist=[]
# print(len(mylist))
# mylist[0]=input('enter name : ')
# print(mylist)

#24 - try
# #1
# # a=int(input('enter number : '))
# a=float(input('enter number : '))
# print(2*a)

#2
# try:
#     # a=int(input('enter number : '))
#     a=float(input('enter number : '))
#     print(2*a)
# # except:
# except Exception as error:
#     # pass
#     # print('ERROR')
#     print(error)

#25
# import math
# print(math.pow(2,5))
# print(math.sqrt(64))
# print(math.pi)
# print(math.e)
# print(math.fabs(-8))
# print(math.fabs(8))
# print(math.ceil(2.64564656465465))
# print(math.ceil(2.14564656465465))
# print(math.sin(90))
# print(math.cos(90))
# print(math.tan(90))
# print(round(2.348546,2))#>=5 --> +1
# print(round(2.342546,2))#<5  --> +0
# print(round(2.345546,2))

#26
# import math
# r=float(input('enter radius : '))
# s=(math.pow(r,2)*math.pi)
# print(f'space = {s}')

# p=(2*r*math.pi)
# print(f'perimeter = {p}')

#27 - list
# numbers=[5,8,-1,3,-9]
# print(numbers[2])
# print(numbers[-1])
# print(numbers)
# print(*numbers)
# print(*numbers,sep=',')
# numbers[1]=12
# print(*numbers)

#28
# numbers=[5,8,-1,3,-9]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(sorted(numbers,reverse=True))

#29
# numbers=[5,8,-1,3,-9]
# print(numbers[0:3])#0 to 2
# print(numbers[:3])#0 to 2
# print(numbers[2:4])#2 to 3
# print(numbers[3:5])#3 to 4
# print(numbers[3:])#3 to 4
# print(numbers[:])#?

#30
# names=['melika','sara','fatemeh','sareh','parnian','tania']
# # print(sorted(names))
# # names.sort()
# # names.sort(reverse=True)
# names.reverse()
# print(names)

#31
# mylist=[]
# mylist.append('ava')
# mylist.append('sogand')
# mylist.insert(0,'sara')
# mylist.insert(2,'sare')
# mylist.insert(len(mylist),'fatemeh')
# mylist.insert(len(mylist),'tania')
# print(mylist)

#32
# mylist=['melika','sara','fatemeh','sareh','sara']
# # del mylist[2]#index
# # mylist.remove('sara')#value
# # # mylist.remove('ava')#error
# # mylist.pop()
# # mylist.pop(0)
# # print(mylist.pop())
# n=mylist.pop()
# print(n)
# print(mylist)

#46
# mylist=[6,5,-3,12,-8,5,33,2,-1]
# print(mylist.count(5))
# print(mylist.count(12))
# print(mylist.count(1))
# mystr='mohandesi farda'
# print(mystr.count('a'))
# print(mystr.count('farda'))

#47 filter, lambda
# mylist=[6,5,-3,12,-8,5,33,2,-1]
# result=filter(lambda n: n<0, mylist)
# print(result)
# print(*result)

# result=filter(lambda n: n%2, mylist)
# print(*result)

#############
# print(bool(5))
# print(bool(-3))
# print(bool(0))
# print(bool('farda'))
# print(bool(''))
# print(bool(5.25))
# print(bool(0.0))
# print(bool([3,8,12]))
# print(bool([]))
# print(bool(5%2))
# print(bool(8%2))

#48
# mylist=[6,5,-3,12,-8,5,33,2,-1,120,11]
# result=filter(lambda n: n>=10 and n<=99, mylist)

#49
# mylist=['amir','sara','ava','narges','reza']
# search=input('enter input : ')
# result=filter(lambda n:search in n , mylist)
# print(*result)

#50
# for i in range(1,100):
#     if i%2==0:
#         print(i,end=' ')
#     else:
#         print('hop',end=' ')


#51
# from random import sample
# names=['melika','fatemeh','sara','sareh','parnian','sogand','tania','ava']
# result=sample(names,len(names))
# print(*result,sep='\n')

#52
# mylist=[1,5,-3,4,12,5,-5,8,32]
# # # print(mylist.count(5))
# # # print(mylist.count(-3))
# # result=list(filter(lambda n: n<0, mylist))
# # print(result)
# # print(*result)
# # print(len(result))
# result=filter(lambda n: n>0 and n%2!=0, mylist)
# print(*result)

#53
# mylist=[1,5,-3,4,12,5,-6,8,32]
# #1
# # for n in mylist:
# #     if n%2==0:
# #         print(n,end=' ')
# #         # break

# #2
# for i in range(len(mylist)-1,-1,-1):
#     # print(i)
#     if mylist[i]%2==0:
#         print(mylist[i],end=' ')
#         break

#54
# from random import randrange
# score=1000
# goal=randrange(1,501)

# while True:
#     guess=int(input(f'enter guess 1 -> 500 [score :{score}]: '))
#     if guess>goal:
#         print('go down')
#         score-=50
#     elif guess<goal:
#         print('go up')
#         score-=50
#     elif guess==goal:#else
#         print('you win')
#         break
    
#     if score<=0:
#         print(f'you lose [goal : {goal}]')
#         break

#55
# from random import randrange
# goal=randrange(1,501)

# for i in range(5):
#     guess=int(input('enter guess 1 -> 500: '))
#     if guess>goal:
#         print('go down')
#     elif guess<goal:
#         print('go up')
#     elif guess==goal:#else
#         print('you win')
#         break

# print(f'goal : {goal}')

#56
# myStr='     Hello World, Python     '
# print(myStr)
# print(len(myStr))
# print(myStr.strip())#lstrip, rstrip
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.replace('o','*'))
# print(myStr.replace('Hello','Hi'))
# print(myStr.count('l'))
# print(myStr.index('o'))
# print(myStr.index('World'))
# result=myStr.strip().split(' ')
# print(result)

###################
#1
# from random import randrange
# i=0
# while i<5:
#     rnd=randrange(1000,10000)
#     if rnd%2==0:
#         print(rnd)
#         i+=1

#2
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end='\t')
#     print()

#3
numbers=[12.5,14,11.75,15,17.75,10.25]
result=filter(lambda n: n>=10 and n<12, numbers)
print(*result)



