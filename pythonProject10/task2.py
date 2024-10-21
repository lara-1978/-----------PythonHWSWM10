# Задача 2. Совместное проживание
# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
# одиночестве, Артём решил провести необычное исследование. Для этого он
# реализовал модель человека и модель дома.
# Человек может (должны быть такие методы):
# ● есть (+ сытость, − еда);
# ● работать (− сытость, + деньги);
# ● играть (− сытость);
# ● ходить в магазин за едой (+ еда, − деньги);
# ● прожить один день (выбирает одно действие согласно описанному ниже
# приоритету и выполняет его).
# У человека есть (должны быть такие атрибуты):
# ● имя,
# ● степень сытости (изначально 50),
# ● дом.
# В доме есть:
# ● холодильник с едой (изначально 50 еды),
# ● тумбочка с деньгами (изначально 0 денег).
# Если сытость человека становится меньше нуля, человек умирает.
# Логика действий человека определяется следующим образом:
# 1. Генерируется число кубика от 1 до 6.
# 2. Если сытость < 20, то нужно поесть.
# 3. Иначе, если еды в доме < 10, то сходить в магазин.
# 4. Иначе, если денег в доме < 50, то работать.
# 5. Иначе, если кубик равен 1, то работать.
# 6. Иначе, если кубик равен 2, то поесть.
# 7. Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.
# Реализуйте такую программу и создайте двух людей, живущих в одном доме.
# Проверьте работу программы несколько раз

import random

class House:
    def __init__(self, food, money):
        self.food = food
        self.money = money

    def buy_food(self, quantity, price):
        if self.money >= price:
            self.food -= price
            self.food += quantity
            print(f'Купили {quantity} еды за {price} денег.')
        else:
            print(f' Недостаточно средств для покупки еды!')

    def earn_money(self, salary):
        self.money += salary
        print(f'Заработали {salary} денег.')

class Human:
    def __init__(self, name, house):

        self.name = name
        self.house = house
        self.hanger = 50

    def eat(self):
        if self.house.food >= 10:
            self.hanger -= 10
            self.house.food -= 10
            print(f'{self.name} поел. Сытость  увеличилась до {self.hanger},еда уменьшилась до {self.house.food}. ')
        else:
            print(f'{self.name} хотел поесть.Недостаточно еды!')

    def work(self):
        self.hanger -= 10
        self.house.earn_money(50)
        print(f'{self.name} поработал. Сытость  уменьшилась до {self.hanger}. ')

    def play(self):
        self.hanger -= 5
        print(f'{self.name} поиграл. Сытость уменьшилась до {self.hanger}. ')

    def shop_for_food(self):
        self.house.buy_food(15, 50)

    def live_one_day(self):
        cube = random.randint(1, 6)
        print(f"\nСегодняшний кубик: {cube}")
        if self.hanger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()
        if self.hanger <= 0:
            print(f"{self.name} умер от голода.")
            return False
        return True


# создаем объекты

house1 = House(10,50)
human1 = Human('Ivan', house1)
human2 = Human('Alex', house1)

house2 =House(25, 40)
human3 = Human('Phil', house2)

try:
    for day in range(1, 366):
        print(f'\nДень{day}')
        if not human1.live_one_day() or not human2.live_one_day() or not human3.live_one_day():
            print(f'Человек умер на{day} день.')
            break

finally:
    print("\nСостояние пары:")
    print(f"Еда в холодильнике - {house1.food}, Деньги -{house1.money}")
    print(f"Состояние {human1.name}: Сытость - {human1.hanger}")
    print(f"Состояние {human2.name}: Сытость - {human2.hanger}\n")
    print("Состояние одиночки:")
    print(f"Еда в холодильнике - {house2.food}, Деньги -{house2.money}")
    print(f"Состояние {human3.name}: Сытость - {human3.hanger}")















