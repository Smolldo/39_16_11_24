board = [[' ' for _ in range(3) ] for _ in range(3)]

for row in board:
    print(row)


current_player = 'X'
game_over = False
turn = 0

while not game_over and turn < 9:
    move = input(f'Turn {current_player}. enter num (1-9): ')
    
    if int(move) < 1 or int(move) > 9:
        print('Out of range enter num (1-9):')
        continue

    move = int(move) - 1

    if board[move] != ' ':
        print('Зайнято. спробуйте іншу клітинку')
        continue


    board[move] = current_player



# # Ініціалізація порожнього поля
# board = [' ' for _ in range(9)]

# # Відображення початкового поля
# for row in range(3):
#     print(f"| {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} |")
#     if row < 2:
#         print("-------------")

# current_player = 'X'
# game_over = False
# turns = 0

# # Гра
# while not game_over and turns < 9:
#     move = input(f"Хід {current_player}. Введіть номер клітинки (1-9): ")
    
#     # Перевірка коректності вводу
#     if not move.isdigit() or int(move) < 1 or int(move) > 9:
#         print("Введіть число від 1 до 9.")
#         continue
    
#     move = int(move) - 1
    
#     # Перевірка, чи клітинка вільна
#     if board[move] != ' ':
#         print("Клітинка вже зайнята. Спробуйте ще раз.")
#         continue

#     # Оновлення поля
#     board[move] = current_player

#     # Відображення поля
#     for row in range(3):
#         print(f"| {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} |")
#         if row < 2:
#             print("-------------")

#     # Перевірка перемоги
#     win_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонталі
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикалі
#         [0, 4, 8], [2, 4, 6]              # Діагоналі
#     ]
#     for combo in win_combinations:
#         if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player:
#             print(f"Гравець {current_player} переміг!")
#             game_over = True
#             break

#     if not game_over:
#         current_player = 'O' if current_player == 'X' else 'X'
#         turns += 1

# if not game_over:
#     print("Нічия!")


