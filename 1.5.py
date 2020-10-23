class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, value):
        if (self.capacity - value) < 0:
            return False
        return True

    def add(self, value):
        if self.can_add(value):
            self.capacity -= value


"""
Similar, but differ a little bit

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        
    def can_add(self, v):
        return self.capacity >= v
        
    def add(self, v):
        self.capacity -= v
"""


class BufferNotWork:
    def __init__(self):
        self.buffer_list = []

    def add(self, *a):
        if len(self.buffer_list) >= 5:  # Вот здесь косяк - как я думаю - ибо при 4 уже в буфере + 3 из ввода = 7, а так
            print(sum(self.buffer_list[:5]))  # нельяз так - вот как
            del self.buffer_list[0:5]
        else:
            self.buffer_list += a

    def get_current_part(self):
        return self.buffer_list


class Buffer:
    def __init__(self):
        self.buffer_list = []

    def add(self, *a):
        self.buffer_list.extend(a)
        while len(self.buffer_list) >= 5:
            print(sum(self.buffer_list[:5]))
            del self.buffer_list[0:5]

    def get_current_part(self):
        return self.buffer_list


"""
class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.value = []
        
    def add(self, *a):
        # добавить следующую часть последовательности.
        # просто увеличим наш список 'value'
        # на величину кортежа 'a', Python просто чудо!
        self.value += a
        while len(self.value) >= 5:
            # суммируем первые 5 элементов, это
            # так просто! красота!
            print(sum(self.value[0:5]))
            # переприсваиваем в атрибут списка 'value'
            # все его же элементы после 5-го!
            self.value = self.value[5:]
            # интересно, что сделает интерпретатор
            # со старым значением в памяти после
            # переприсваивания?

    def get_current_part(self):
        # вернуть сохраненные в текущий момент
        # элементы последовательности в порядке,
        # в котором они были добавлены
        return self.value
"""

class Song:
    tags = []

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song

    def add_tags(self, *args        ):
        self.tags.extend(args)


song1 = Song('one', 'one-one')
song1.add_tags('one and one', '1-1')

song2 = Song('two', 'two-two')
song2.add_tags('two and two', '2-2')


class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)
