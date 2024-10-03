'''
lenth 
type 
sling
max/mmin/sorted
'''

#s1=[1,2,3,4,5,6,7,8,9,0]
#print(s1[::2])
#print(s1[0]+s1[-1])

s1=int(input("enter the value = "))
s2=int(input("enter the value = "))
s3=int(input("enter the value = "))
s4=int(input("enter the value = "))
s5=int(input("enter the value = "))

s6=[s1,s2,s3,s4,s5]


print(s6)
print(max(s6))
print(min(s6))
print(sorted(s6))
print(sorted(s6,reverse=True))