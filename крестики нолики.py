# Игровое поле
field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_field(field):
    """Функция для отображения текущего состояния игрового поля."""
    for row in field:
        print(' '.join(row))  # Соединяем элементы строки пробелами и выводим

def check_input(input_elem):
    """Функция для проверки корректности ввода игрока (X или O)."""
    if input_elem not in ['X', 'O']:
        print('Ошибка: Неправильный ввод данных!')  # Сообщение об ошибке
        return None
    else:
        return input_elem  # Возвращаем корректный ввод

def add_to_field(field, row, col, player):
    """Функция для добавления хода игрока на игровое поле."""
    # Проверка корректности координат
    if row < 0 or row >= 3 or col < 0 or col >= 3:
        print('Ошибка: Неверно введены координаты!')  # Сообщение об ошибке
        return False
    # Проверка, занята ли ячейка
    if field[row][col] != '-':
        print('Ошибка: Данная ячейка уже занята!')  # Сообщение об ошибке
        return False
    # Добавление символа игрока в указанную ячейку
    field[row][col] = player
    return True  # Успешное добавление

def check_winner(field):
    """Функция для проверки наличия победителя на игровом поле."""
    # Проверка строк и столбцов на наличие победителя
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != '-':
            return field[i][0]  # Возвращает символ победителя
        if field[0][i] == field[1][i] == field[2][i] != '-':
            return field[0][i]  # Возвращает символ победителя
    # Проверка диагоналей на наличие победителя
    if field[0][0] == field[1][1] == field[2][2] != '-':
        return field[0][0]  # Возвращает символ победителя
    if field[0][2] == field[1][1] == field[2][0] != '-':
        return field[0][2]  # Возвращает символ победителя
    return None  # Нет победителя

def check_draw(field):
    """Функция для проверки на ничью."""
    # Проверка, заполнено ли поле
    for row in field:
        if '-' in row:
            return False  # Есть пустые ячейки, игра продолжается
    return True  # Поле заполнено, ничья

# Основной игровой цикл
current_player = 'X'  # Начинает игрок X
while True:
    print_field(field)  # Отображение текущего состояния поля

    # Запрос ввода координат от текущего игрока
    row = int(input(f'Игрок {current_player}, введите номер строки (0-2):'))
    col = int(input(f'Игрок {current_player}, введите номер столбца (0-2):'))

    # Попытка добавить ход игрока
    if add_to_field(field, row, col, current_player):
        winner = check_winner(field)  # Проверка на победителя
        if winner:
            print_field(field)  # Отображение финального состояния поля
            print(f'Игрок {winner} выиграл!')  # Объявление победителя
            break  # Завершение игры
        if check_draw(field):  # Проверка на ничью
            print_field(field)  # Отображение финального состояния поля
            print('Ничья!')  # Объявление ничьей
            break  # Завершение игры

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'
