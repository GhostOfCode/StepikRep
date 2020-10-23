class A:
    pass


class B(A):
    pass


class C:
    pass


class D(A):
    pass


class E(B, C, D):
    pass


# print(E.mro())
classes = dict()


def add_class(classes, class_name, parents):
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].extend(parents)
    for parent in parents:
        if parent not in classes:
            classes[parent] = []


def found_path(classes, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in classes:
        return None
    for node in classes[start]:
        if node not in path:
            newpath = found_path(classes, node, end, path)
            if newpath: return newpath
    return None


def answer(classes, parent, child):
    if not (parent or child) in classes or not found_path(classes, child, parent):
        return 'No'
    return 'Yes'


n = int(input())
for _ in range(n):
    class_description = input().split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    add_class(classes, class_name, class_parents)

q = int(input())
for _ in range(q):
    question = input().split()
    parent = question[0]
    child = question[1]
    print(answer(classes, parent, child))

"""
n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")

def test(parent, child):
    if parent == child or parent in base[child]:
        return 'Yes'
    for i in base[child]:
        if test(parent, i) == 'Yes':
            return 'Yes'
    return 'No'

Another one possible way:

base = {}
for com in [input().split(' ') for i in range(int(input()))]:
    base[com[0]] = com[2:len(com)]
for com in [input().split(' ') for i in range(int(input()))]:
    print (test(com[0], com[1]))


# put your python code here
def find_path(start, path):
    path.add(start)
    for node in graph[start]:
        if node not in path:
            find_path(node, path)

graph = {}
for i in range(int(input())):
    s = input().split()
    graph[s[0]] = s[2:] if len(s) > 1 else [s[0]]

for i in range(int(input())):
    s = input().split()
    path = set()
    find_path(s[1], path)
    print('Yes' if s[0] in path else 'No')

"""


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())

import time


class Loggable:

    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, arg):
        super(LoggableList, self).append(arg)
        self.log(arg)
