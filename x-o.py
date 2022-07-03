# Крестики-нолики (итоговое задание)

str_0 = ['\ ', ' 1', '  2', '  3']
str_1 = [1, '  -', '  -','  -']
str_2 = [2, '  -', '  -','  -']
str_3 = [3, '  -', '  -','  -']
field = [str_0, str_1, str_2, str_3]
game = True
player = 'x'
new_game = ''

def game():
    global str_0
    global str_1
    global str_2
    global str_3
    global field
    global player
    global game
    global new_game
    count = 9

    while game:
# Вывод игрового поля
        print(f'{str_0[0]}{str_0[1]}{str_0[2]}{str_0[3]}')
        print(f'{str_1[0]}{str_1[1]}{str_1[2]}{str_1[3]}')
        print(f'{str_2[0]}{str_2[1]}{str_2[2]}{str_2[3]}')
        print(f'{str_3[0]}{str_3[1]}{str_3[2]}{str_3[3]}')
        print(f'* * * * * *')
        if count > 0:
            print(f'Игрок: {player}')
            coord = input('>> Ввод координат: ').split()
            print('\n')

# Проверка корректности ввода
        while 2 > len(coord) < 2 or not coord[0].isnumeric() or not coord[1].isnumeric()\
                or 1 > int(coord[0]) > 3 or 1 > int(coord[1]) > 3:
            coord = input(f'Введи 2 числа от 1 до 3 через пробел').split()

        x = int(coord[0])
        y = int(coord[1])

# Переход хода
        if ('-' in field[x][y]) and player == 'x':
            field[x][y] = '  x'
            count -= 1
            player = 'o'
        if ('-' in field[x][y]) and player == 'o':
            field[x][y] = '  o'
            count -= 1
            player = 'x'

# Выигрышные комбинации "X"
        if str_1 == [1, '  x', '  x', '  x'] or str_2 == [2, '  x', '  x', '  x'] or str_3 == [3, '  x', '  x', '  x']\
                or (field[1][1] == '  x' and field[2][1] == '  x' and field[3][1] == '  x')\
                or (field[1][2] == '  x' and field[2][2] == '  x' and field[3][2] == '  x')\
                or (field[1][3] == '  x' and field[2][3] == '  x' and field[3][3] == '  x')\
                or (field[1][1] == '  x' and field[2][2] == '  x' and field[3][3] == '  x')\
                or (field[1][3] == '  x' and field[2][2] == '  x' and field[3][1] == '  x'):
            print(f'*** Игрок "X" выиграл ***')
            game = False

# Выигрышные комбинации "O"
        if str_1 == [1, '  o', '  o', '  o'] or str_2 == [2, '  o', '  o', '  o'] or str_3 == [3, '  o', '  o', '  o']\
                or (field[1][1] == '  o' and field[2][1] == '  o' and field[3][1] == '  o')\
                or (field[1][2] == '  o' and field[2][2] == '  o' and field[3][2] == '  o')\
                or (field[1][3] == '  o' and field[2][3] == '  o' and field[3][3] == '  o')\
                or (field[1][1] == '  o' and field[2][2] == '  o' and field[3][3] == '  o')\
                or (field[1][3] == '  o' and field[2][2] == '  o' and field[3][1] == '  o'):
            print(f'*** Игрок "O" выиграл ***')
            game = False

# Ничья
        if count == 0:
            game = False
            print(f'*** Ничья!!! ***')

game()