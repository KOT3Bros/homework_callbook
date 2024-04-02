'''
Семинар 8. Работа с файлами
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''

from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'
new_file_name = 'new_phone.csv'


def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Некорректная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'имя': lst[0], 'фамилия': lst[1], 'телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def row_search(file_name):
    last_name = input('Введите фамилию: ')
    res = read_file(file_name)
    finded_rows = []
    for elem in res:
        if elem['фамилия'] == last_name:
            finded_rows.append(elem)
    if len(finded_rows) == 0:
        print('Введённая фамилия не найдена')
    else:
        print(*finded_rows, sep='\n')

def copy_row(file_name, new_file_name):
    copy_data_from = read_file(file_name)
    line_number = int(input('Введите номер строки, которую Вы хотите скопировать: '))
    obj = copy_data_from[line_number - 1]
    res = [obj['имя'], obj['фамилия'], obj['телефон']]
    write_file(new_file_name, res)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name), sep='\n')
        elif command == 'f':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            row_search(file_name)
        elif command == 'c':
            if not exists(new_file_name):
                create_file(new_file_name)
            copy_row(file_name, new_file_name)


main()
