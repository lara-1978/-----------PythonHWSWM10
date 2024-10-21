    # Задание 1. Отцы, матери и дети.
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# ● имя,
# ● возраст,
# ● список детей.
# И он может:
# ● сообщить информацию о себе,
# ● успокоить ребёнка,
# ● покормить ребёнка.
# У ребёнка есть:
# ● имя,
# ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# ● состояние спокойствия,
# ● состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее

class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        print(f"My name is {self.name}, I'm {self.age} years old")

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f'Child {child.name} added to {self.name}.')
        else:
            print(f'Child {child.name} not added to {self.name}, since the age difference is too small.')

    def feed(self, child):
        if child in self.children:
            child.hungry = False
        else:
            print(f'Child {child.name} is not a child of {self.name}.')

    def calm(self, child):
        if child in self.children:
            child.calm = True
            print(f'Child {self.name} reassured {child.name}.')
        else:
            print(f'Child {child.name} is not a child of {self.name}.')

    def list_children(self):
        if self.children:
            print(f'{self.name} has the following children:')
            for child in self.children:
                print(f" - {child}")
        else:
            print(f"{self.name} doesn't have a child.")

class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hungry = False
        self.calm = True

    def get_status(self):
        calm_status = "calm" if self.calm else "not calm"
        hungry_status = "full" if not self.hungry else "hungry"
        print(f'Child {self.name} is {calm_status} and {hungry_status}.')

    def __str__(self):
        return f'Child {self.name}, {self.age} years old'

# Создаем родителей
parent = Parent('Jan', 45)
child1 = Child('Yumi', 13)
child2 = Child('Lila', 16)

for child in (child1, child2):
    parent.add_child(child)

parent.info()
parent.list_children()

for child in parent.children:
    parent.feed(child)
    parent.calm(child)
    child.get_status()


    
    
    







