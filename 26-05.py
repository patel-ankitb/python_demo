# import requests

# response = requests.get('https://cdn.pixabay.com/photo/2024/05/15/12/31/lake-8763490_1280.jpg')
# print(response.text)
# with open('imag1.jpg','wb') as f:
#     f.write(response.content)

# ----------------------------------------------------->
# import json

# dic1  = '{"key1" : "keyvalue"}'
# print(type(dic1))
# a=json.loads(dic1)
# print(type(a))

# dic2 = {"key1" : "keyvalue"}
# print(type(dic2))
# a=json.dumps(dic2)
# print(type(a))


# -------------------------------------------------->

from datetime import datetime
print(datetime.now())
d=datetime.now()
print(d.hour)

abc = d.strftime('%m/%d/%y')
print(abc)
int_str = "25 september 2025"
a= datetime.strptime(int_str,"%d %B %Y")
print(a)