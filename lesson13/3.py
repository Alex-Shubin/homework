"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство cо значением урона от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.
                
                
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.

"""


"""
    Класс для создания героя

    Attributes:
    name : str - Имя героя
    health : int - Здоровье героя
    age : int - возраст героя

    Methods:
    print_info():
    Печатает в консоль информацию о герое

    kick():
    Производит один удар - высчитывает и уменьшает броню и здоровье
"""

import random
from abc import ABC, abstractmethod
class Hero(ABC):

    # свойства/атрибуты класса
    option1 = True
    point = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должгны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    
    
    def __init__(self, name, health, armor, strong) -> None:
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
    
    def _get_info(self):
        return (f"Имя {self.name}\n" \
                f"Здоровье {self.health}\n" \
                f"Защита {self.armor}\n" \
                f"Атака {self.strong}")
    
    def print_info(self, resource_name="Резурс", resource_value=0, sep="-"):
        info = f"{self._get_info()}\n{sep*20}\n{resource_name} - {resource_value}"
        print(info)

    @abstractmethod
    def get_special_attack_message(self, resource_name, resource_left):
        pass

    def basic_attack(self, other):
        damage_dealt = self.apply_damage(other, self.strong)
        print(f"{self.name} проводит обычную атаку и наносит {damage_dealt} урона!")
        print(f"У {other.name} осталось {other.armor} брони и {other.health} здоровья.")

    def special_attack(self, other, special_name, special_value):
            if special_value > 0:
                setattr(self, special_name, special_value - 1)
                print(self.get_special_attack_message(special_name, getattr(self, special_name)))
                damage_dealt = self.apply_damage(other, self.strong * 2)
                print(f"{self.name} наносит {damage_dealt} урона!")
                print(f"У {other.name} осталось {other.armor} брони и {other.health} здоровья.")
            else:
                print(f"недостаточно {special_name}! Обычная атака")
                self.basic_attack(other)


    def apply_damage(self, other, damage):
        initial_armor = other.armor
        initial_health = other.health
        other.armor -= damage
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
        damage_dealt = (initial_armor - other.armor) + max(0, initial_health - other.health)
        return damage_dealt

class Mag(Hero):
    def __init__(self, name, health, armor, strong, mana) -> None:
        super().__init__(name, health, armor, strong)
        self.mana = mana
        
    def attack(self, other):
        if random.randint(0, 3) == 0 and self.mana > 0:
            self.special_attack(other, 'mana', self.mana)
        else:
            self.basic_attack(other)

    def get_special_attack_message(self, resource_name, resource_left):
        return f"{self.name} использует магию! Осталось {resource_left} маны"

    def print_info(self):
        super().print_info("Мана", self.mana)

class Warrior(Hero):
    def __init__(self, name, health, armor, strong, fury):
        super().__init__(name, health, armor, strong)
        self.fury = fury
    
    def attack(self, other):
        if random.randint(0, 3) == 0 and self.fury > 0:
            self.special_attack(other, 'fury', self.fury)
        else:
            self.basic_attack(other)

    def get_special_attack_message(self, resource_name, resource_left):
        return f"{self.name} использует ярость! Осталось {resource_left} ярости"

    def print_info(self):
        super().print_info("Ярость", self.fury)

class Archer(Hero):
    def __init__(self, name, health, armor, strong, energy):
        super().__init__(name, health, armor, strong)
        self.energy = energy
    
    def attack(self, other):
        if random.randint(0, 3) == 0 and self.energy > 0:
            self.special_attack(other, 'energy', self.energy)
        else:
            self.basic_attack(other)

    def get_special_attack_message(self, resource_name, resource_left):
        return f"{self.name} использует энергию! Осталось {resource_left} энергии"
        
    def print_info(self):
        super().print_info("Энергия", self.energy)

class Arena():
    

    def __init__(self, warriors:list=None):
        if warriors is None:
            self.warriors = list()
        else:
            self.warriors = warriors

    def add_warrior (self, warrior):
        if not warrior in self.warriors:
            self.warriors.append(warrior)
            print(f"{warrior.name} участвует в битве")
        else:
            raise ValueError("Воин уже на арене")

    def choose_warrior(self):
        if self.warriors:
            return random.choice(self.warriors)
        else:
            return None
    
    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError('Количество воинов на арене должно быть больше 1')
        else:
            while len(self.warriors) != 1:
                in_battle = random.sample(self.warriors, 2)
                in_battle[0].attack(in_battle[1])
                if in_battle[1].health <= 0:
                    print(f'{in_battle[1].name} пал в битве')
                    self.warriors.remove(in_battle[1])
                else:
                    in_battle[1].attack(in_battle[0])
                    if in_battle[0].health <= 0:
                        print(f'{in_battle[0].name} пал в битве')
                        self.warriors.remove(in_battle[0])
            winner = self.warriors[0]
            print(f"Победил воин: {winner.name}")
            return winner
            


hero1 = Mag('Gendalf', 20, 20, 3, 30)
hero2 = Mag('Sauron', 20, 20, 3, 30)
hero3 = Warrior('Aragorn', 50, 30, 2, 30)
hero4 = Archer('Legolas', 40, 20, 2, 30)

arena = Arena()

arena.add_warrior(hero1)
arena.add_warrior(hero2)
arena.add_warrior(hero3)
arena.add_warrior(hero4)

winner = arena.battle()

if winner:
    print(f"Победитель битвы: {winner.name}")
else:
    print("Битва не состоялась")