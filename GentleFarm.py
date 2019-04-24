class Animal:
    instances = {}

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animal.instances[self.name] = self.weight

    def feed(self):
        self.weight += 2
        Animal.instances[self.name] = self.weight
        print(f'{self.name} был откормлен(а) до {self.weight} кг')

    def distinguish_by_voices(self):
        print(f'"{self.voice}"')


class Sheep(Animal):
    voice = 'Беееее!'

    def shear(self):
        self.weight -= 2
        Animal.instances[self.name] = self.weight
        print(f'{self.name} подстрижен, теперь он весит {self.weight} кг')


class Bird(Animal):
    def feed(self):
        self.weight += 0.5
        Animal.instances[self.name] = self.weight
        print(f'{self.name} был откормлен(а) до {self.weight} кг')

    def collect_eggs(self):
        self.weight -= 0.5
        Animal.instances[self.name] = self.weight
        print(f'{self.name} теперь весит {self.weight} кг, яйца собраны')


class Goose(Bird):
    voice = 'Га-Га-Га!'


class Hen(Bird):
    voice = 'Ко-Ко-Ко!'


class Duck(Bird):
    voice = 'Кря-Кря-Кря!'


class Milking_Animal(Animal):
    def milk(self):
        self.weight -= 2
        Animal.instances[self.name] = self.weight
        print(f'{self.name} подоена и теперь весит {self.weight} кг')


class Cow(Milking_Animal):
    voice = 'Мууууу!'


class Goat(Milking_Animal):
    voice = 'Меееее!'


goose_1 = Goose('Гусь "Серый"', 3)
goose_2 = Goose('Гусь "Белый"', 4)
cow_1 = Cow('Корова "Манька"', 500)
sheep_1 = Sheep('Баран "Барашек"', 80)
sheep_2 = Sheep('Баран "Кудрявый"', 75)
hen_1 = Hen('Курица "Ко-Ко"', 2.5)
hen_2 = Hen('Курица "Кукареку"', 3)
goat_1 = Goat('Коза "Рога"', 82)
goat_2 = Goat('Коза "Копыта"', 84)
duck_1 = Duck('Утка "Кряква"', 2)


print('На ферме живут:')
for k in Animal.instances.keys():
    print(f'{k} весом {Animal.instances[k]} кг')
print('Общий вес всех животных на ферме: {} кг'.format(sum(Animal.instances.values())))
max_weight = max(Animal.instances.values())
for k in Animal.instances:
    if Animal.instances[k] == max_weight:
        big_animal = k
print(f'{big_animal} весит больше остальных: {max_weight} кг')


def main():
    while True:
        user_input_command = input(
            'Введите команду (покормить, собрать яйца, подстричь, подоить, послушать, закончить): ')
        if user_input_command == 'покормить':
            user_input_animal = input('Введите имя животного: ')
            if user_input_animal == 'Серый':
                goose_1.feed()
            elif user_input_animal == 'Белый':
                goose_2.feed()
            elif user_input_animal == 'Манька':
                cow_1.feed()
            elif user_input_animal == 'Барашек':
                sheep_1.feed()
            elif user_input_animal == 'Кудрявый':
                sheep_2.feed()
            elif user_input_animal == 'Ко-Ко':
                hen_1.feed()
            elif user_input_animal == 'Кукареку':
                hen_2.feed()
            elif user_input_animal == 'Рога':
                goat_1.feed()
            elif user_input_animal == 'Копыта':
                goat_2.feed()
            elif user_input_animal == 'Кряква':
                duck_1.feed()
            else:
                print('Животных с таким именем нет')
        elif user_input_command == 'послушать':
            user_input_animal = input('Введите имя животного: ')
            if user_input_animal == 'Серый' or 'Белый':
                goose_1.distinguish_by_voices()
            elif user_input_animal == 'Манька':
                cow_1.distinguish_by_voices()
            elif user_input_animal == 'Барашек' or user_input_animal == 'Кудрявый':
                sheep_1.distinguish_by_voices()
            elif user_input_animal == 'Ко-Ко' or user_input_animal == 'Кукареку':
                hen_1.distinguish_by_voices()
            elif user_input_animal == 'Рога' or user_input_animal == 'Копыта':
                goat_1.distinguish_by_voices()
            elif user_input_animal == 'Кряква':
                duck_1.distinguish_by_voices()
            else:
                print('Животных с таким именем нет')
        elif user_input_command == 'собрать яйца':
            user_input_animal = input('Введите имя животного: ')
            if user_input_animal == 'Серый':
                goose_1.collect_eggs()
            elif user_input_animal == 'Белый':
                goose_2.collect_eggs()
            elif user_input_animal == 'Ко-Ко':
                hen_1.collect_eggs()
            elif user_input_animal == 'Кукареку':
                hen_2.collect_eggs()
            elif user_input_animal == 'Кряква':
                duck_1.collect_eggs()
            elif user_input_animal == 'Манька' or 'Барашек' or 'Кудрявый' or 'Рога' or 'Копыта':
                print('Это животное не может нести яйца')
            else:
                print('Животных с таким именем нет')
        elif user_input_command == 'подстричь':
            user_input_animal = input('Введите имя животного: ')
            if user_input_animal == 'Барашек':
                sheep_1.shear()
            elif user_input_animal == 'Кудрявый':
                sheep_2.shear()
            elif user_input_animal == 'Серый' or 'Белый' or 'Манька' or 'Ко-Ко' or 'Кукареку' or 'Рога' or 'Копыта' or 'Кряква':
                print('Это животное не для стрижки')
            else:
                print('Животных с таким именем нет')
        elif user_input_command == 'подоить':
            user_input_animal = input('Введите имя животного: ')
            if user_input_animal == 'Манька':
                cow_1.milk()
            elif user_input_animal == 'Рога':
                goat_1.milk()
            elif user_input_animal == 'Копыта':
                goat_2.milk()
            elif user_input_animal == 'Серый' or 'Белый' or 'Барашек' or 'Кудрявый' or 'Ко-Ко' or 'Кукареку' or 'Кряква':
                print('Это животное нельзя подоить')
            else:
                print('Животных с таким именем нет')
        elif user_input_command == 'закончить':
            print('Общий вес всех животных на ферме к концу работы: {} кг'.format(sum(Animal.instances.values())))
            max_weight = max(Animal.instances.values())
            for k in Animal.instances:
                if Animal.instances[k] == max_weight:
                    big_animal = k
            print(f'{big_animal} весит больше остальных: {max_weight} кг')
            print('До свидания')
            break
        else:
            print('Неверная команда')


main()