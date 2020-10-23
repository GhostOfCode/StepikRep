x = [1, 2, 3]

print(type(x[0]))
print(id(x))
print(id([1, 2, 3]))
print(id(x[0]))
print(id(x[1]))

y = x
print(x is y)
print(y is [1, 2, 3])

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)
print(s is t)

"""ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)"""
objects = [True, 5, 1, 257, 257, 3, 3, 3, 1, 2]

"""
# unique_objects = [obj if obj  for obj in objects]
unique_objects = []
for x in objects:
    if x not in unique_objects:
        unique_objects.append(x)

# for i in range(len(objects)):
#     for k in range(i+1, len(objects)):
#         if objects[i] is objects[k]:
#             unique_objects += 1

print(len(unique_objects))
Некорректно отрабатывает если в одном списке True и 1 (False - 0)
"""

# Верные во всех смыслах и вариантах решений - и с True и 1 в одном списке
s = set()
for obj in objects:
    s.add(id(obj))
print(len(s))

print(len({id(i) for i in objects}))
print(len(set(map(id, objects))))
