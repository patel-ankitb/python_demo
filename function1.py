#4)----> Write a Python program to find the largest of three numbers.
#  Test Data : 12 25 52
#  Expected Execution:
#  1st Number = 12 
#  2nd Number = 25
#  3rd Number = 52

'''def larget( a,b,c):
    l1=list()
    l1.append(a)
    l1.append(b)
    l1.append(c)
    print("1st number  = ",max(l1))
    for x in l1:
        if min(l1)!= x and max(l1)!=x:
            print("2rd number = ",x)
    print("3rd number  = ",min(l1))
  
larget(int(input("ENTER THE NUMBER = ")),int(input()),int(input()))'''

'''a=int(input("enter the 1st number = "))
b=int(input("enter the 1st number = "))
c=int(input("enter the 1st number = "))
def find_largest_number (a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def find_mid_number (a, b, c):
    if a>b or a>c:
        return a
    elif b>a or b>c:
        return b
    else:
        return c
max=find_largest_number(a,b,c)
mid=find_mid_number(a,b,c)
def find_last_num(a,b,c,max,mid):
    return a+b+c-max-mid

last=find_last_num(a,b,c,max,mid)
print("first number = ",max)
print("second number = ",mid)
print("third number = ",last)'''


# Take values of length and breadth of a rectangle from user and check if it is square or not .

