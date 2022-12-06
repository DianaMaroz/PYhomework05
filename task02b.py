# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import function_candy as candy
your_name = input("Привет! Как тебя зовут? ")

print(f'{your_name},  давай я расскажу тебе правила игры.')
print('Условие задачи: На столе лежит определенное количество конфет. Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем N конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
again = 'да'
while again == 'да':
    candy.candy_game(your_name)
    again = candy.is_yes_no(input('Напиши да, если хочешь сыграть еще:  '))
    if not again.lower() == 'да':
        print('Возвращайся, если захочешь повторить!')