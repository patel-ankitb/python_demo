# 1)---> print  the first 10 natural number using for loop
'''
''for a in range(1,11):
    print(a)''
'''
# 2)---> python program to print all the even  number within the given rangr

'''a=int(input("enter the number a  = "))
b=int(input("enter the number  b = "))

for x in range(a,b,2):
    print(x)'''

# 3)----> sum of the number 1 staring 

'''sum=0
a=int(input("enter the number a  = "))
for x in range(1,a):
    sum=sum+x
print(sum)'''


# 4)----> Python program to calculate the sum of all the odd numbers within the given range.

'''sum=0
a=int(input("enter the numbr a= "))
b=int(input("enter the number b = "))
for x in range(a,b):
    if x%2!=0:
        print(x)
        sum=sum+x
print(sum)

'''

# 5)--->Python program to print a multiplication table of a given number 
'''

a=int(input("enter the number a = "))
for x in range(1,11):
    print(a,'x' , x,'=' ,a*x)
'''

# 6)---> Python program to count the total number of digits in a number.
'''
count=0
s=int(input("enter the number s  = "))
for x in range(1,s):
    if i.isdigit():
      count+=1
print(count)'''

# 7)---->Python program to find the factorial of a given number.
'''
fac=1
a=int(input("enter the number "))
for x in range(1,a+1):
    fac=fac*x
print(fac)'''

# 8)---->Python program to count the number of even and odd numbers from a series of numbers. 

# s=int(input("enter the number = "))
# e=int(input("enter the number = "))



# for x in range(s,e):
#     if '3' not in str(x) and '6' not in str(x):
#         print(x)
#     else :
#         continue
# print(x)

# 9)---->Python program that accepts a word from the user and reverses it.

'''str = input('Enter word : ')
rev=0
print('reversed word : ',str[::-1])

for x in str:
    rev = x + rev
print(rev)
 '''
 

#  Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# number = [1,2,3,4,5,6,7,8,9]
# for x in range(number):
#     if(x%2==0 and x%)



# Write a Python program to sum two integers. 
# However, if the sum is between 15 and 20 it will return 20.

# a=input("enter the number = ")
# for i in range(a):
#     if i.integers(a):
#          print("int")
#     else:
#         print("not")


# i=1
# sum=0
# while(i<=5):
#     a=int(input("enter the number ="))
#     i+=1
#     sum=sum+a
# print(sum)




# tuple1 = ('abc','royal','pvt','ltd','Mango')
# find min and max of this tupleremove all the elements from 'pvt'add ['apple','banana'] to tuple1

t1 = ('abc','royal','pvt','ltd','Mango')
x=list(t1)
del x[2:5]
x.extend(['apple','banna'])
print(x)