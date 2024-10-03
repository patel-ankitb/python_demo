# set:--------
#  set {}        
# taple ()
# list[]

"""
Ordered     Mutable     list        []
Ordered     Immutable   tuple       ()
Unordered   Mutable     set         {}
Unordered   Immutable   frozenset"""

# method:====
# 1) --> add 2)----> update 3)-->remove 4)-->discard (no error)5)--. clear 5)--> union   6)--> intersection 7)--> symmtric 
# function--->  min ---> max--->sum--->

# empty

# --->  A set is a colletion whichb is unoredered anchangeble , and unindexed
#---->  set items are unchangble but you can remove items and add new items .

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(y)



# s1 = {11,2,3,(4,4),"ab",123}
# print(s1)
# print(type(s1))
# s1 = {15, 7, -17, 15, 0.78, 6, 15, 18, 15.47, 15, 98.2, 0, 15}
# empty_set = {1}
# empty_set = set("1")
# print(len(empty_set))
# print(type(empty_set))

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update({"mylist"})
# print(thisset)


# thisset = {"apple", "cherry"}
# # thisset=set(thisset)
# thisset.remove("apple")
# print(thisset)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)


#-----> 1) remove repeating items from list [None,1,None,1]===[None,1]

'''s1=[None,1,None , 1,None]
new=[]
s1=(s1)
s1=list(set(s1))
print(s1)

for i in s1:
    if i not in new:
        new.append(i)
print(new)
'''


#----> 2) remove ony None values or empty values from list--None, ""[None,1,None,1,""]==[1,1]

'''s1=[None ,1,None,1,""]
new=[]
for x in s1:
    # print(x)
    if x != None and x != "":
        new.append(x)

print(new)

s2=set(s1)
print(s2)'''

#----> 3) find factorial of the elements in the list
'''s1=[1,5,3,6,7]
fact = 1
for x in s1:
    fact*=x
print(fact)'''

#----> 4 ) check whether elements in the list are pallindrome or not ["mam","ram","121","33"]

'''l1 = ["mam","ram","121","33"]
print(l1)
for x in l1:
    if x == x[::-1]:
        print(x,' is pallindrome\n')'''
    

#---> 5) add multiple items to tuple

'''t1=(1,2,3,4,5,6)
s1=[5,6,7,8,9,1]

t1=list(t1)
print(t1)
t2=t1.extend(s1)
print(t2)'''