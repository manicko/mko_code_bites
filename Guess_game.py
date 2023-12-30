import math
from random import *


def get_random():
    return randint(1, 100)


def guess_game():

    print('Давайте поиграем в угадайку? Я загадал число от 1 до 100. \n')

    agree = input('Попробуете его угадать? (да/нет) ')
    if agree == 'нет':
        print('жаль((')
    elif agree == 'да':
        n = get_random()
        while True:
            x = input('Какое число я загадал? (введите свой вариант): ')
            try:
                x = int(x)
                if x > n:
                    print('Слишком много, попробуйте еще раз \n')

                elif x < n:
                    print('Слишком мало, попробуйте еще раз \n')
                else:
                    print('Вы угадали, поздравляю! ')
                    print('        /\___/)')
                    print('　　　　   (　_　 _ )')
                    print('　　    ／ミ _ x _彡')
                    print('　 　  /　　　 　   \\')
                    print('　　  /　 　　ヽ    ﾉ')
                    print(' ／￣|　　  |　|　|')
                    print('| (￣ヽ＿＿\=)\=)')
                    print('＼二つ')

                    break
            except:
                print('Вы ввели что-то не то, давайте попробуем еще раз \n')


guess_game()
