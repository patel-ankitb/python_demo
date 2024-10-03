# thisdi={
#     "a" : 10,
#     "b" : 11,
#     "c" : 'ankit',
#     "d" : 'patel',
#     "e" : 12
#  }

# print(thisdi.get("a","no"))
# print(thisdi.get("ai","151"))
# print(thisdi.values())
# print(thisdi.keys())thi


# thisdi.update({"a" : 12345})
# print(thisdi)

# thisdi["b"]=None
# print(thisdi)

# my=[1,2,3,4,5]
# my1=[2,3,4,5,6]

# print(dict(zip(my,my1)))
# thisdi.update(dict(zip(my,my1)))
# print(thisdi)

# 1)------>Write a Python script to concatenate the following dictionaries to create a new one.
'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic5={}

for x in [dic1,dic2,dic3]:
    dic5.update(x)
print(dic5)'''

#2)---->Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.Sample Dictionary{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

'''dic1={}
for x in range(1,16):
    dic1.update({x:x*x*x*x})
print(dic1)
'''

#3)_----->  Write a Python program to create a dictionary from a string.Note: Track the count of the letters from the string.Sample string : 'w3resource'Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

'''string='w3resource'
dic1={}
for x in string:
    count=0
    for y in string:
        if(x==y):
            count+=1
    dic1.update({x:count})    
print(dic1)'''

#4)---->Write a Python program to drop empty items from a given dictionary.Original Dictionary:{'c1': 'Red', 'c2': 'Green', 'c3': None}New Dictionary after dropping empty items:{'c1': 'Red', 'c2': 'Green'}Write a Python program to drop empty items from a given dictionary.Original Dictionary:{'c1': 'Red', 'c2': 'Green', 'c3': None}New Dictionary after dropping empty items:{'c1': 'Red', 'c2': 'Green'}
    

'''
Dictionary={
    'c1': 'Red', 
    'c2': 'Green',
    'c3': None
    }
for key , value in  Dictionary.items() :
    if value is  None:
        Dictionary.pop(key)
print(Dictionary)'''

#5)---->Write a Python program to match key values in two dictionaries.

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for (key, value) in set(x.items()) & set(y.items()):
#     print('%s: %s is present ' % (key, value))


# counter = 0
# my_dict = {
#     'one': 100,
#     'two': 200,
#     'three': 300
# }


# for key,value in my_dict:
#     if key=='one':
#       counter += value*1
#     elif key == 'two':
#         counter += value*2
#     elif key == 'three':
#         counter += value*3
# print(counter)



# thisdict={
#     1:1,
#     2:2,
#     3:3,
#     4:4,
#     5:5
# }
# list1 = []
# for k,v in thisdict.items():
#     a = k*v
#     list1.append(a)

# print(list1)



original_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
threshold = 170
filtered_dict = {key: value for key, value in original_dict.items() if value > threshold}

print("Original Dictionary:", original_dict)
print(f"Marks greater than {threshold}:", filtered_dict)
