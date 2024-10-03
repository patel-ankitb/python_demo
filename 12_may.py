# x= lambda n : [ print(n*n-1)  for x in range(1,n) if x>=1]
# x(5)

# x = lambda n : 1 if n==0 and n%2==0 else 0
# print(x(10)) 

# -------------------------------------------------

# l=[]
# for i in [1,2,3,4,5]:
#     l.append(i*i)

# print(dict(map(lambda n: [n,n*n],[1,2,3,4,5])))

# X = list(filter(lambda even : even%2==0,range(1,101)))
# print(X)

# ----------------------------------------------------

# from functools import reduce
# num =int(input("enter number --- > "))
# def custom_sum(first,num):
#     return first*num
# result = reduce(custom_sum ,range(1,num+1))
# print(result)

# ----------------------------------------4
# word=["wertyu","sdfghjudsgh","werr"]
# x = list(filter(lambda n : len(n)>=5, word ))
# print(x)
# ---------------------------------------------------

students = [
    {"name": "Denis Helio", "age": 17, "grade": 97},
    {"name": "Hania Mehtap", "age": 16, "grade": 92},
    {"name": "Kelan Stasys", "age": 17, "grade": 90},
    {"name": "Velvet Mirko", "age": 16, "grade": 94},
    {"name": "Delores Aeneas", "age": 17, "grade": 100},
]
x = list(filter(lambda grade : grade ,len("grade")>=95 ,students))
print(x)