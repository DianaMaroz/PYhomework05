# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
def is_integer(sm_input: str) -> int:
    while not sm_input.isdigit():
        sm_input = input('Давай на этот раз ты введешь целое число:  ')
    return int(sm_input)

def is_yes_no(sm_str:str) -> str:
    answer_list = ['да', 'нет' ]
    while sm_str.lower() not in answer_list:
        sm_str = input('Прости, я не понял, что ты имеешь в виду. Напиши да или нет:  ')
    return sm_str

def is_orel_reshka(sm_str: str) -> int:
    answer_list = ['орел', 'решка']
    while sm_str.lower() not in answer_list:
        sm_str = input('Прости, я не понял, что ты имеешь в виду. Напиши орел или решка:  ')
    return sm_str


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
        step = is_integer(input(f"Сколько конфет ты возьмешь? Помни, взять можно от 1 до {max_step}!   "))
    total_candy -= step
    return total_candy

def take_candy(total_candy: int, max_step: int, user: str, first: bool) -> str:
    print('Ты выбрал вариант попроще')
    flag_player = user
    while total_candy > 0:
        if not first:
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

def take_candy_clever_bot(total_candy: int, max_step: int, user:str, first: bool) -> str:
    print('Помни, против тебя играет очень умный бот')
    flag_player = 'bot'
    if not first:
        print(f'В игре {total_candy} конфет')
        print(f'Первый ходит бот')
        if total_candy % (max_step + 1) == 0:
            bot_step = random.randint(1, max_step)
        else:
            bot_step = total_candy % (max_step + 1)
        print(f'Бот взял {bot_step} конфет')
        total_candy -= bot_step
    while total_candy > 0:
        print(f'В игре {total_candy} конфет')
        if total_candy < max_step:
            max_step = total_candy
        user_step = 0
        while user_step < 1 or user_step > max_step:
            user_step = is_integer(input(f"Сколько конфет ты возьмешь? Помни, взять можно от 1 до {max_step}!   "))
        total_candy -= user_step
        if total_candy == 0:
            flag_player = user
            print(' Ура! Ты сделал этого умника! Все конфеты твои!')
        else:
            if total_candy < max_step:
                bot_step = total_candy
            else:
                bot_step = max_step + 1 - user_step
            print(f'Бот взял {bot_step} конфет')
            total_candy -= bot_step
            if total_candy == 0:
                print('Очень жаль, но ты проиграл: все конфеты достанутся боту. Он слишком умен! (((')
    return flag_player

def candy_game(user_name):
    first_player = True
    candy = is_integer(input('На какое количество конфет играем?  '))
    take_step = is_integer(input('А какое максимальное количество можно взять за ход? '))
    print('Давай проведем жеребьевку')
    user_choiсe = is_orel_reshka(input(f"{user_name}, выбери: орел или решка? "))
    coin_random = random.choice(['орел', 'решка'])
    print(f'Сейчас подброшу монетку! {coin_random.capitalize()}!')
    if user_choiсe == coin_random:
        print('Поздравляю, твой ход первый.')
    else:
        first_player = False
        print('В этот раз не повезло, первым ходит бот')
    level = is_yes_no(input('Хочешь сразиться с по настоящему умным противником? '))
    if level == 'нет':
        winner = take_candy(candy, take_step, user_name, first_player)
    else:
        winner = take_candy_clever_bot(candy, take_step, user_name, first_player)

    print(f'Победитель -  {winner.upper()}!')

your_name = input("Привет! Как тебя зовут? ")

print(f'{your_name},  давай я расскажу тебе правила игры.')
print('Условие задачи: На столе лежит определенное количество конфет. Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем N конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
again = 'да'
while again == 'да':
    candy_game(your_name)
    again = is_yes_no(input('Напиши да, если хочешь сыграть еще:  '))
    if not again.lower() == 'да':
        print('Возвращайся, если захочешь повторить!')







