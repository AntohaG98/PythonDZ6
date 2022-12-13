# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random


def print_value(num):
    print(f'Осталось {num} конфет')


def num_check(main_num, num_1, player):
    if 1 <= num_1 <= max_number:
        if main_num == num_1:
            print(f"{player} победил!")
            exit()
        elif main_num > num_1:
            print_value(main_num - num_1)
            return main_num - num_1
        else:
            print(f'Ошибка! Осталось {main_num} конфет')
            return -1
    else:
        print("Ошибка! Можно взять только от 1 до 28 конфет")
        return -1


def comp_player(some_candis, comp_color):
    print(comp_color.format(f"Компьютер берёт: {some_candis}"))


def comp_win():
    print("Компьютер победил!")
    exit()


def week_comp_player(main_num, move1):
    if 1 <= main_num <= max_number:
        comp_player(main_num, comp_color_1)
        comp_win()
    else:
        comp_n = random.randint(1, max_number)
        comp_player(comp_n, comp_color_1)
        print_value(main_num - comp_n)
        return not move1, main_num - comp_n


def strong_comp_player(main_num, move1):
    if 1 <= main_num <= max_number:
        comp_player(main_num, comp_color_2)
        comp_win()
    else:
        comp_n = main_num % (max_number + 1)
        if comp_n == 0:
            comp_n = random.randint(1, max_number)
        comp_player(comp_n, comp_color_2)
        print_value(main_num - comp_n)
        return not move1, main_num - comp_n


def moving(player, move1, balance_candies, player_color):
    some_cand = int(input(player_color.format(f"{player} берёт: ")))  # красим вывод
    temp = num_check(balance_candies, some_cand, player)
    if temp != -1:
        balance_candies = temp
        move1 = not move1
    return move1, balance_candies


def rand_move():
    if random.randint(11, 20) > 15:
        return True
    else:
        return False


# Начало программы
max_number = 28
balance_of_candies = 2021
player_name_1 = "Первый игрок"
player_name_2 = "Второй игрок"
player_name_3 = "Игрок"
player_color_1 = "\033[34m{}"  # синий цвет текста
player_color_2 = "\033[31m{}"  # красный цвет текста
comp_color_1 = "\033[35m{}"  # фиолетовый цвет текста
comp_color_2 = "\033[33m{}"  # желтый цвет текста
print("Выберете режим игры:\n1 - против другого игрока")
print("2 - против слабого компьютера\n3 - против сильного компьютера")
check_type_game = False
type_game = ""
while not check_type_game:
    type_game = input("Введите выбранный режим: ")
    if type_game == "1" or type_game == "2" or type_game == "3":
        check_type_game = True
    else:
        print("Ошибка!")

print_value(balance_of_candies)
move = True
if type_game == "1":
    while balance_of_candies >= 0:
        if move:
            move, balance_of_candies = moving(player_name_1, move, balance_of_candies, player_color_1)
        else:
            move, balance_of_candies = moving(player_name_2, move, balance_of_candies, player_color_2)
elif type_game == "2":
    move = rand_move()
    while balance_of_candies >= 0:
        if move:
            move, balance_of_candies = moving(player_name_3, move, balance_of_candies, player_color_1)
        else:
            move, balance_of_candies = week_comp_player(balance_of_candies, move)
elif type_game == "3":
    move = rand_move()
    while balance_of_candies >= 0:
        if move:
            move, balance_of_candies = moving(player_name_3, move, balance_of_candies, player_color_1)
        else:
            move, balance_of_candies = strong_comp_player(balance_of_candies, move)