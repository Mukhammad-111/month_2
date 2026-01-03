class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'CPU: {self.cpu}, MEMORY: {self.memory}'

    def __lt__(self, other):
        return self.__memory < other

    def __gt__(self, other):
        return self.__memory > other

    def __eq__(self, other):
        return self.__memory == other

    def __ne__(self, other):
        return self.__memory != other

    def __le__(self, other):
        return self.__memory <= other

    def __ge__(self, other):
        return self.__memory >= other


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = list(sim_cards_list)

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number in self.__sim_cards_list:
            if sim_card_number == 1:
                print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}-Mega')
            elif sim_card_number == 2:
                print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}-Beeline')
        else:
            raise TypeError(f'Извините такое симкарту нету {sim_card_number}')

    def __str__(self):
        return f'SIM_CARDS_LIST: {self.sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Успешно проложен маршрут от вашего местоположение до локацию: {location}')
    
    def __str__(self):
        return f'CPU: {self.cpu}, MEMORY: {self.memory}, SIM_CARDS_LIST: {self.sim_cards_list}'


computer = Computer(16, 512)
phone = Phone([1, 2])
smartphone_1 = SmartPhone(4, 64, [1, 2])
smartphone_2 = SmartPhone(8, 128, [1, 2])

accessories = [computer, phone, smartphone_1, smartphone_2]

for accessory in accessories:
    print(accessory)

print(computer.make_computations())
phone.call(2, +996222938968)
smartphone_1.call(1, 550525131)
smartphone_2.use_gps('Ala-Archa')
print(smartphone_2 < smartphone_1)
print(smartphone_2 > smartphone_1)
print(smartphone_2 == smartphone_1)
print(smartphone_2 != smartphone_1)
print(smartphone_2 <= smartphone_1)
print(smartphone_2 >= smartphone_1)