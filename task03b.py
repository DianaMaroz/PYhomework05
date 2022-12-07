import function_candy as candy
import function_xo as xo
your_name = input("Привет! Как тебя зовут? ")
print("Сыграем в крестики- нолики!")
again = 'да'
while again == 'да':
    xo.game_xo(your_name)
    again = candy.is_yes_no(input('Напиши да, если хочешь сыграть еще:  '))
    if not again.lower() == 'да':
        print('Возвращайся, если захочешь повторить!')