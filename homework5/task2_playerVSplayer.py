from random import *
import os


rules = ('Сегодня поиграем с конфетками :)\n'
        'Правила:\n'
        'Есть 150 конфет, вы берете их по очереди,\n'
        'за один раз можно взять не больше 28 конфет.\n'
        'Выигрывает тот, кто последним ходом заберет все конфеты.\n')
print(rules)

message = ['Твоя очередь,', 'Бери еще,', 'Можешь взять еще,','Бери быстрее,', 'Да, еще бери']


def player_vs_player():
    candies_total = 150
    max_take = 28
    count = 0
    player_1 = input('\nКак тебя зовут? ')
    player_2 = input('\nА тебя? ')

    print('\nДля начала опеределим, кто начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось еще: {candies_total} конфет')
            count = 1
        else:
            print('Всё, конфет больше нет')

        if count == 1:
            step = int(input(f'\n{choice(message)} {loser} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОСталось еще {candies_total}, конфет')
            count = 0

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


# def player_vs_bot():
#     candies_total = 150
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()