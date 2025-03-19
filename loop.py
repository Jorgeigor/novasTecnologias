# for i in range(10):
#    print(i)

"""c = 0
while c < 10:
    print(c)
    c += 1"""
    
'''for i in range(10):
    if i == 5:
        continue
    print(i)'''

"""arr = [1,2,3,4,5,6,7,8,9,10]
arr_names = ["Joao", "ZÉ", "Marcos"]
for i in arr_names:
    print(i)"""

''' OPERADORES LÓGICOS'''

"""
x = 0 
y = 20
if x> 0 and y > 0:
    print("Ambos x e y são positivos")
if x > 0 or y > 0:
    print("Pelo menos x ou y é positivo")
if not x > 0:
    print("X não é maior que 0")"""

"""COLEÇÕES"""
"""
ny_text = [1,2,3,4,5,1]
print(ny_text[0:2])
print(ny_text[1:4])


ny_text.append(6)
print(ny_text)

ny_text.insert(0, 0)
print(ny_text)

ny_text.remove(1)
print(ny_text)


ny_text.clear()
print(ny_text)

ny_text.reverse()
print(ny_text)

ny_text.sort()
print(ny_text)

ny_text.extend([7,8,9])
print(ny_text)

print(ny_text.count(1))

print(ny_text.index(5))"
"""

"""TUPLAS"""

"""
ny_text = (1,2,3,4,5)
print(ny_text.index(1))
print(ny_text.count(1))
"""

"""Dicionary"""
"""
ny_dict = {"name": "John", "age": 30, "city": "New York"}
print(ny_dict["name"])
print(ny_dict.get("age"))
print(ny_dict.keys())
print(ny_dict.values())
print(ny_dict.items())
ny_dict["age"] = 31
ny_dict["country"] = "USA"
print(ny_dict)
ny_dict["city"]
print(ny_dict)
#ny_dict.clear()
#print(ny_dict)"
"""

"""FUNÇÃO"""

def ny_function():
    print("Hello from a function")
ny_function()

"""
def ny_function(param1, param2):
    return param1 + param2

texto = ny_function("Hello", "Word")
print(texto)"""