from random import randint

from decouple import config


def load_settings():
    min_num = config('MIN_NUM', cast=int)
    max_num = config('MAX_NUM', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    initial_capital = config('INITIAL_CAPITAL', cast=int)
    return min_num, max_num, attempts, initial_capital


if __name__ == "__main__":
    print(load_settings())


def play_game():
    min_num, max_num, attempts, initial_capital = load_settings()
    secret_num = randint(min_num, max_num)
    print(f'Добро пожаловать в игру "Угадай число"!!! Диапазон чисел: от {min_num} до {max_num}')
    print(f'У вас есть: {attempts} количество попыток. И началный капитал : {initial_capital}')
    while attempts > 0 or initial_capital > 0:
        try:
            bet = int(input(f'Сделайте ставку (Доступно:{initial_capital}): '))
            if bet > initial_capital or bet <= 0:
                print('Неверное ставка. Попробуйте снова!')
                continue
            guess = int(input(f'Угадайте число (попыток осталось {attempts}): '))
            if guess == secret_num:
                initial_capital += bet * 2
                print(f"Поздравляем! Вы угадали число "
                      f"{secret_num}. Ваш баланс: {initial_capital}.")
            else:
                initial_capital -= bet
                attempts -= 1
                if attempts > 0:
                    print(f"Неправильно! Баланс: {initial_capital}."
                          f" Осталось попыток: {attempts}.")
                else:
                    print(f"Вы проиграли! Число было: {secret_num}."
                          f" Баланс: {initial_capital}.")
        except ValueError:
            print("Пожалуйста, введите числовое значение.")


if __name__ == "__main__":
    print(play_game())
