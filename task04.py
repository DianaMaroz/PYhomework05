# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def get_list_symb(sm_str: str) -> list:
    list_for_symb = [sm_str[0]]
    for i in range(1, len(sm_str)):
        if sm_str[i] != sm_str[i - 1]:
            list_for_symb.append(sm_str[i])
    return list_for_symb


def get_list_count(sm_str: str) -> list:
    list_for_count = []
    symb = sm_str[0]
    count_symb = 0
    for i in range(len(sm_str)):
        if sm_str[i] == symb:
            count_symb += 1
        else:
            list_for_count.append(count_symb)
            symb = sm_str[i]
            count_symb = 1
    count_last_symb = len(sm_str) - sum(list_for_count)
    list_for_count.append(count_last_symb)
    return list_for_count


def code_rle(list_count: list, list_symb: list) -> str:
    string_rle = ''
    list_count_str = list(map(str, list_count))
    for i in range(len(list_count_str)):
        string_rle += list_count_str[i] + list_symb[i]
    return string_rle


def decode_rle(sm_str: str):
    list_num = []
    list_symb = []
    start_ind = 0
    for i in range(len(sm_str)):
        if sm_str[i].isalpha():
            list_symb.append(sm_str[i])
            list_num.append(sm_str[start_ind:i])
            start_ind = i + 1
    list_number = list(map(int, list_num))

    decode_str = ''
    for i in range(len(list_symb)):
        for _ in range(list_number[i]):
            decode_str += list_symb[i]
    return decode_str


data = open('uncodefile04.txt', 'r')
my_str = str(data.readline())
data.close()
print(my_str)

list2 = get_list_symb(my_str)
print(list2)
list1 = get_list_count(my_str)
print(list1)
str_rle = code_rle(list1, list2)
print(str_rle)

data_rle = open('codefile04.txt', 'w')
data_rle.write(str_rle)
data_rle.close()

dec_rle = decode_rle(str_rle)
print(dec_rle)
data_decode = open('decodefile04.txt', 'w')
data_decode.write(str_rle)
data_decode.close()
