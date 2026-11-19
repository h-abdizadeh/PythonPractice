#1
# print('hello')
# # print(1000*'hello')
# print(7+5)
# print(7-5)
# print(7/5)
# print(7*5)

#2
# print(7>5)
# print(3==5)
# print('amir'>'parsa')
# print('a'=='A')

# 3
# a=5
# b=7
# print(a+b)
# print('a+b')
# a=b
# print(a+b)

#4
# nums=[12,8,18,15,20]
# print(nums)
# print(*nums)
# print(*nums,sep='hop')
# print(nums[3])
# print(nums[0])
# print(nums[-1])
# print(nums[-2])
# print(len(nums))

# 5
# nums=[10,18,-3,11,4,-1,15]
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# 6
# names=['parsa','saam','m javad','fatemeh']
# # print(sorted(names))
# names.sort()

# nums=[3,-1,11,-4,8]
# # print(sorted(nums))
# nums.sort()

# print(names)
# print(nums)

# 7
# mylist=['c','a','d','b']
# # print(sorted(mylist))
# # print(sorted(mylist,reverse=True))

# mylist.sort(reverse=True)
# print(mylist)

# 8
# names=[]
# print(names)
# names.append('fatemeh')
# names.append('saam')
# names.append('mohammad javad')
# names.insert(0,'hossein')
# names.insert(2,'parsa')
# names.insert(len(names),'reza')
# print(names)

# 9
# mylist=['reza','amir','sara','arad','ava','sara']
# print(mylist)
# # del mylist[1]
# # mylist.remove('sara')
# # mylist.pop()
# # mylist.pop(3)
# trash=mylist.pop(1)
# print(trash)
# print(mylist)

# 10
# print(7 in [1,3,9])
# print(3 in [1,3,9])
# print('arad' in ['saam','parsa','m.j'])
# print('parsa' in ['saam','parsa','m.j'])
# print('a' in 'saam')
# print('z' in 'm.j')


# 11
users=['parsa','m javad','saam']
n=input('name : ')

if n in users:
    users.remove(n)
else:
    users.append(n)

print(users)