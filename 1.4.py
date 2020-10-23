scopes = {'global': {'parent': None, 'variables': set()}}


def create(namespace, parent):
    scopes[namespace] = {'parent': parent, 'variables': set()}
    return


def add(namespace, var):
    scopes[namespace]['variables'].add(var)
    return


def get(namespace, var):
    if var in scopes[namespace]['variables']:
        return namespace
    elif scopes[namespace]['parent'] is not None:
        return get(scopes[namespace]['parent'], var)
    return None
# def get(namespace, var):
#     while not namespace is None and var not in namespaces[namespace]:
#         namespace = namespaces[namespace][0]
#     print(namespace)


n = int(input())
for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    elif cmd == 'add':
        add(namesp, arg)
    elif cmd == 'get':
        print(get(namesp, arg))
# commands = {'create': create, 'add': add, 'get': get}
# n = int(input())
# for _ in range(n):
#     enter = input().split()
#     commands[enter[0]](enter[1], enter[2])

'''
Example from Stepik

info = dict({'global':[None]})

def create(namespace, parent):
    info.update({namespace:[parent]})

def add(namespace, var):
    info[namespace].append(var)

def get(namespace, var):
    while namespace != None and var not in info[namespace][1:]:
        namespace = info[namespace][0]
    print(namespace)

operations = {'create': create, 'add': add, 'get': get}
for i in range(int(input())):
    inp = input().split()
    operations[inp[0]](inp[1], inp[2])

Another one

dct={'global':['None']}                                             # словарь списков(родитель,переменные)
for ops, nms, v in [input().split() for i in range(int(input()))]:  # цикл операций(копипаст у Vladmir Ryabov)
    if   ops=='create':dct[nms]=[v]                                 # создать пространство-новый список в словаре
    elif ops=='add'   :dct[nms].append(v)                           # новая переменная-добавить в список
    elif ops=='get':                                                # поиск переменной (циклом)
        while nms!='None' and v not in dct[nms]:                    # если нет в пространстве-меняем на родителя(пока не None)
            nms=dct[nms][0]                     
        print(nms)

The last one

namespace = {'global':{'parent':'None','childrens':[]}}

def create(a,b):
    namespace[b]['childrens'].append(a)
    namespace[a] = {'parent':b,'childrens':[]}  
    
def add(a,b):
    namespace[a]['childrens'].append(b)
    namespace[b] = {'parent':a}
    
def get(a,b):
    if b in namespace[a]['childrens']:
        print(a)
    else:
        if namespace[a]['parent'] != 'None': 
            get(namespace[a]['parent'],b)
        else:
            print('None')
            
for i in range(int(input())):
    f,a,b = input().split()
    globals()[f](a,b) 
'''