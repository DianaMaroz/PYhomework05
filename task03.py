#Создайте программу для игры в ""Крестики-нолики"".
import function_candy as candy
import random


def print_table(sm_list: list):
    print(f' {sm_list[0]} | {sm_list[1]} | {sm_list[2]}')
    print('___________')
    print(f' {sm_list[3]} | {sm_list[4]} | {sm_list[5]}')
    print('___________')
    print(f' {sm_list[6]} | {sm_list[7]} | {sm_list[8]}')

def is_from_one_to_nine(sm_input: str) -> int:
    while not sm_input.isdigit():
        sm_input = input('Давай на этот раз ты введешь целое число:  ')
    while int(sm_input) > 9 or int(sm_input) < 1:
        sm_input = input('Давай это будет число от 1 до 9:  ')
    return int(sm_input)

def check_win(sm_list: list, symb: str) -> bool:
    if sm_list[0] == sm_list[1] == sm_list[2] == symb:
        return True
    elif sm_list[3] == sm_list[4] == sm_list[5] == symb:
        return True
    elif sm_list[6] == sm_list[7] == sm_list[8] == symb:
        return True
    elif sm_list[0] == sm_list[3] == sm_list[6] == symb:
        return True
    elif sm_list[1] == sm_list[4] == sm_list[7] == symb:
        return True
    elif sm_list[2] == sm_list[5] == sm_list[8] == symb:
        return True
    elif sm_list[0] == sm_list[4] == sm_list[8] == symb:
        return True
    elif sm_list[2] == sm_list[4] == sm_list[6] == symb:
        return True
    else:
        return False


def game_xo_with_bot(user: str, first: str) -> str:
    table = [i for i in range(1, 10)]
    table_for_bot = [i for i in range(1, 10)]
    step_count = 0
    flag_player = 'nobody'
    while step_count < 9:
        print_table(table)
        if first == user:
            step = is_from_one_to_nine(input('Выбери номер ячейки, куда поставишь Х -    '))
            while table[step - 1] == 'X' or table[step - 1] == 'O':
                step = is_from_one_to_nine(input('Прости, но ячейка занята, выбери другую -   '))
            table_for_bot.remove(step)
            step_count += 1
            table[step - 1] = 'X'
            print_table(table)
            if check_win(table, 'X'):
                flag_player = user
                print(f'{user} поздравляю!')
                break
            else:
                if step_count == 9:
                    break
                else:
                    print('Теперь ходит бот')
                    bot_step = random.choice(table_for_bot)
                    table[bot_step - 1] = 'O'
                    step_count += 1
                    table_for_bot.remove(bot_step)
                    if check_win(table, 'O'):
                        flag_player = 'bot'
                        print(f'{user} может в следующий раз повезет')
                        break
        else:
            print('Теперь ходит бот')
            bot_step = random.choice(table_for_bot)
            table[bot_step - 1] = 'X'
            table_for_bot.remove(bot_step)
            step_count += 1
            print_table(table)
            if check_win(table, 'X'):
                flag_player = 'bot'
                print(f'{user} может в следующий раз повезет')
                break
            else:
                if step_count == 9:
                    break
                else:
                    step = is_from_one_to_nine(input('Выбери номер ячейки, куда поставишь O -    '))
                    while table[step - 1] == 'X' or table[step - 1] == 'O':
                        step = is_from_one_to_nine(input('Прости, но ячейка занята, выбери другую -   '))
                    table_for_bot.remove(step)
                    step_count += 1
                    table[step - 1] = 'O'
                    if check_win(table, 'O'):
                        flag_player = user
                        print(f'{user} поздравляю!')
                        break
    return flag_player


def game_xo_for_two(user: str, second_user: str, first: str) -> str:
    table = [i for i in range(1, 10)]
    step_count = 0
    flag_player = 'nobody'
    while step_count < 9:
        print_table(table)
        if first == user:
            print(f'Теперь ходит {user.capitalize()}')
            step = is_from_one_to_nine(input(f'{user.capitalize()}, выбери номер ячейки, куда поставишь Х -    '))
            while table[step - 1] == 'X' or table[step - 1] == 'O':
                step = is_from_one_to_nine(input('Прости, но ячейка занята, выбери другую -   '))
            step_count += 1
            table[step - 1] = 'X'
            print_table(table)
            if check_win(table, 'X'):
                flag_player = user
                print(f'{user} поздравляю!')
                break

            else:
                if step_count == 9:
                    break
                else:
                    print(f'Теперь ходит {second_user.capitalize()}')
                    step = is_from_one_to_nine(input(f'{second_user.capitalize()}, выбери номер ячейки, куда поставишь O -    '))
                    while table[step - 1] == 'X' or table[step - 1] == 'O':
                        step = is_from_one_to_nine(input('Прости, но ячейка занята, выбери другую -   '))
                    step_count += 1
                    table[step - 1] = 'O'
                    if check_win(table, 'O'):
                        print_table(table)
                        flag_player = second_user
                        print(f'{second_user.capitalize()} поздравляю!')
                        break
        else:
            step = is_from_one_to_nine(input(f'{second_user.capitalize()}, выбери номер ячейки, куда поставишь Х -    '))
            while table[step - 1] == 'X' or table[step - 1] == 'O':
                step = is_from_one_to_nine(input('Прости, но ячейка занята, выбери другую -   '))
            step_count += 1
            table[step - 1] = 'X'
            print_table(table)
            if check_win(table, 'X'):
                flag_player = second_user
                print(f'{second_user.capitalize()}, поздравляю!')
                break
            else:
                print(f'Теперь ходит {user.capitalize()}')
                step = is_from_one_to_nine(input(f'{user.capitalize()}, выбери номер ячейки, куда поставишь O -    '))
                while table[step - 1] == 'X' or table[step - 1] == 'O':
                    step = is_from_one_to_nine(input('Прости, но ячейка занята, выбери другую -   '))
                step_count += 1
                table[step - 1] = 'O'

                if check_win(table, 'O'):
                    print_table(table)
                    flag_player = user
                    print(f'{user} поздравляю!')
                    break
    return flag_player


def game_xo(user: str) -> str:
    mode = input("Если хочешь поиграть с ботом напиши 1, если с другом - 2:   ")
    while mode not in ['1', '2']:
        mode = input("Ой, что-то не то! Введи 1, если хочешь поиграть с ботом, и 2 - если с другом:   ")
    if mode == '1':
        print('Отлично, поиграем вместе')
    else:
        second_user = input('А как зовут твоего друга? ')
    user_choice = candy.is_orel_reshka(input('Теперь нам надо определить, кто ходит первый. Выбери - орел или решка:  '))
    coin_random = random.choice(['орел', 'решка'])
    print(f'Сейчас подброшу монетку! {coin_random.capitalize()}!')
    if user_choice == coin_random:
        first_player = user
        print(f'Поздравляю, {user.capitalize()}, твой ход первый')
    else:
        if mode == '1':
            first_player = 'bot'
        else:
            first_player = second_user
            print(f' {second_user.capitalize()} ходит первым')

    if mode == '1':
        winner = game_xo_with_bot(user, first_player)
        if winner == 'bot':
            print('Жаль, но победа досталась bot')
        elif winner == user:
            print(f'{user.upper()}, C ПОБЕДОЙ')
        else:
            print('Эта достойная игра закончилась ничьей')
    else:
        winner = game_xo_for_two(user, second_user, first_player)
        if winner == second_user:
            print(f'{second_user.upper()}, C ПОБЕДОЙ')
        elif winner == user:
            print(f'{user.upper()}, C ПОБЕДОЙ')
        else:
            print('Эта достойная игра закончилась ничьей')


your_name = input("Привет! Как тебя зовут? ")
print("Сыграем в крестики- нолики!")
again = 'да'
while again == 'да':
    game_xo(your_name)
    again = candy.is_yes_no(input('Напиши да, если хочешь сыграть еще:  '))
    if not again.lower() == 'да':
        print('Возвращайся, если захочешь повторить!')
