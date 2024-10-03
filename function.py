
# lamba
# *args
# **arg
# sort(revered ,true ) dec.
#sort aec.


# def function():
#     a=int(input("enter the number a ="))
#     b=int(input("enter the number b ="))
#     if a>b:
#         print(a)
#     else:
#         print(b)
#     print("sum = " ,a+b)
# function()


# ======================================================================================================


'''def function(**kid):

    print(kid["first"] + kid["midd"]  + kid["last"])

function(first=input("enter the first-name  =  "),midd=input("enter the midd-name  =  "),last=input("enter the last-name  =  "))
'''
# ---------------------------------------------------------------------------------------------------------------------------------//-

'''def evenfun(even):
    for x in even:
        if x%2==0:
            print(x)
number = [1,2,3,4,5,6,7,8,9]
evenfun(number)'''



'''# x=int(input("enter the number = "))

# l=lambda x : print(x,"is leap year") if x%4==0  else print(x,"not leap year")
# print(l(x))'''

# program is sum of a natural number ---->
'''def function():
    sum=0
    a=int(input("enter the number  = "))
    for x in range(1,a+1):
        sum=sum+x
    print(sum)
function()'''


#4)----> Write a Python program to find the largest of three numbers.
# # # Test Data : 12 25 52
#  # Expected Execution:# 1st Number = 12 # 2nd Number = 25
#  # 3rd Number = 52

# def larget(*no):
#     if no[0]>no[1]:
#         if no[0]>no[2]:
#             print(" 1st Number = ",no[0])
#         else:
#             print("3rd number  = ",no[2])
#     elif no[1]>no[2]:
#         print("2rd number = ",no[1])
#     else:
#         print("3rd number = ",no[2])   
# larget(int(input("ENTER THE NUMBER = ")),int(input()),int(input()))

# Take values of length and bre 1st Number = ",adth of a rectangle from user and check if it is square or not.



# count=0
# l1=[1,2,3,4,5,6,7,8,9,10]
# a = tuple(filter(lambda x : x % 2 == 0 ,l1))

# c=len(a)
# print(c)


# l2 = ["mam","aba","xyz","1221"]
# a= list(filter(lambda x :x==x[::-1] ,l2))
# print(a)




# s1 ="my name is ankit"
# print(s1[::-1])