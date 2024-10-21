#     Задача 4. Создание класса-фабрики для животных
# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и
# добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который
# возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
# Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
# В противном случае, рыба относится к категории "Средневодная рыба".
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию
# млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса.
# Если вес объекта меньше 1, то он относится к категории "Малявка".
# Если вес объекта больше 200, то он относится к категории "Гигант".
# В противном случае, объект относится к категории "Обычный".
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных
# разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь
# метод create_animal, который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для конкретного
# типа животного. Количество и типы аргументов могут различаться в зависимости от типа животного.
# Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.
# Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с
# сообщением 'Недопустимый тип животного'.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}"

class Bird(Animal):
    def __init__(self, name: str, wingspan: float):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, name: str, max_depth: int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Shallow"
        elif 10 <= self.max_depth < 100:
            return "Moderate"
        else:
            return "Deep"

class Mammal(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

# создания объектов
bird = Bird("Sparrow", 20.0)
fish = Fish("Nemo", 30)
mammal = Mammal("Elephant", 6000)

# Вывод инфы
print(bird)
print(f"Wing length: {bird.wing_length()}")
print(fish)
print(f"Depth category: {fish.depth()}")
print(mammal)

