 #  1---take input as your name ,check whether your name entered is correct or not

'''a=input("ENTER THE NAME = ")
print(a)
if a=='ankit':
    print(a)
else:
    print('incorrect name')'''


# 2)---->find max number from two number


'''a=int(input("enter the number = "))
b=int(input("enter the number = "))
if a>b:
    print(a)
else:
    print(b)
'''

# 3)-----> find maxnimum number between three element

'''a=int(input("enter the number a = "))
b=int(input("enter the number b = "))
c=int(input("enter the number c = "))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif(b>c):
    print(b)
else:
    print(c)

'''


# 



# Write a Python program to calculate a dog's age in dog years.# Note: For the first two years, a dog year# is equal to 10.5 human years. After that, each dog year equals 4 human years.

'''dog = int(input("enter the age = "))
if dog<0:
    print("age is possitive number")
elif dog<=2:
    year = dog * 10.5
else:
    year = (dog*10.5)+4-10.5

print("this is dog year --> ",year)'''

#  Write a Python program to check whether an alphabet is a vowel or consonant.

'''vowel = ['a','e','i','o','u']

a=input("enter the char = ")

if a in vowel:
    print("vowel --->")
else:
    print("consonant ---> ")'''


# List of months: January, February, March, April, May, June, July, August, September, October, November, December   

month =('January', 'February',' March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

a=input("enter the month = ")
if month=='February':
    print(" no.of day 28/29")
elif month in ('January',' March','May','July','August','October','December'):
    print("no.of day 31")
elif month in ('April','June','September','November'):
    print(" no .of day 30")
else:
    print("no")
