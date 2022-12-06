# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def bot_step(total_candy: int, max_step:int) -> int:
    if total_candy < max_step:
        max_step = total_candy
    step = random.randint(1, max_step)
    print(f"Бот взял {step} конфет. Осталось {total_candy - step}")
    total_candy -= step
    return total_candy

def user_step(total_candy: int, max_step:int)-> int:
    if total_candy < max_step:
        max_step = total_candy
    step = 0
    while step < 1 or step > max_step:
        step = int(input(f"Сколько конфет ты возьмешь? Помни, взять можно от 1 до {max_step}!   "))
    total_candy -= step
    return total_candy

def take_candy(total_candy: int, max_step: int, user: str) -> str:
    flag_player = user
    while total_candy > 0:
        if first_player == 'bot':
            print(f'В игре {total_candy} конфет')
            total_candy = bot_step(total_candy, max_step)
            if total_candy == 0:
                flag_player = 'bot'
                print('Очень жаль, но ты проиграл, все конфеты достанутся боту (((')
            else:
                total_candy = user_step(total_candy, max_step)
                if total_candy == 0:
                    print(' Ура! Все конфеты твои!')
        else:
            print(f'В игре {total_candy} конфет')
            total_candy = user_step(total_candy, max_step)
            if total_candy == 0:
                print(' Ура! Все конфеты твои!')
            else:
                total_candy = bot_step(total_candy, max_step)
                if total_candy == 0:
                    flag_player = 'bot'
                    print('Очень жаль, но ты проиграл, все конфеты достанутся боту (((')
    return flag_player

def candy_game(user_name):
    first_player = user_name
    candy = input('На какое количество конфет играем? ')
    while not candy.isdigit():
        candy = input('Ой, кажется это не число... Попробуй еще раз:  ')
    candy = int(candy)
    take_step = input('А какое максимальное количество можно взять за ход? ')
    while not take_step.isdigit():
        take_step = input('Давай на этот раз ты введешь целое число:  ')
    take_step = int(take_step)
    user_choiсe = input(f"{user_name}, выбери: орел или решка? ").lower()
    coin_random = random.choice(['орел', 'решка'])
    print(f'Сейчас подброшу монетку! {coin_random.capitalize()}!')
    if user_choiсe == coin_random:
        print('Поздравляю, твой ход первый.')
    else:
        first_player = 'bot'
        print('В этот раз не повезло, первым ходит бот')
    winner = take_candy(candy, take_step, user_name)
    print(f'Победитель -  {winner.upper()}!')

your_name = input("Привет! Как тебя зовут? ")
first_player = your_name
print(f'{your_name},  давай я расскажу тебе правила игры.')
print('Условие задачи: На столе лежит определенное количество конфет. Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем N конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
again = 'да'
while again == 'да':
    candy_game(your_name)
    again = input('Напиши да, если хочешь сыграть еще:  ')
    if not again.lower() == 'да':
        print('Возвращайся, если захочешь сыграть еще!')







