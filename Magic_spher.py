from random import choice


def draw_stars(n):
    for i in range(n):
        print(' '*(n-i-1), '*'*(i), '*'*(i + 1), sep="")


def draw_stars_inv(n):
    for i in range(n-1, -1, -1):
        print(' '*(n-i-1), '*'*(i), '*'*(i + 1), sep="")


def ask_oracul():
    draw_stars(30)

    print('\n\nРаз ты пришел ко мне, значит так пожелала вселенная...')
    print('Задай свой вопрос и не проси больше, чем получишь в ответ...\n')
    reply = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
             'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
             'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
             'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
             'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

    questions = []
    to_remove = '0123456789,.?! ;'
    while True:
        again = input('У тебя есть вопрос? (да/нет) ')

        if not again == 'да':
            draw_stars(10)
            print('\nЧто ж прекрасно!',
                  'Твои вопросы лишь пыль на границе вселенной...',
                  'Многомерность миров вот где кроется истинный смысл!',
                  sep='\n')
            break
        q_dirty = input('\nЧто ты хочешь спросить у вселенной? \n')
        q = ''.join([c.lower() for c in q_dirty if c not in to_remove])
        if not q.isalpha:
            print('\nТвой вопрос непонятен.\n',
                  'Сначала собери свои мысли, потом приходи с вопросом.\n')
            continue
        if q in questions:
            print('\nТы уже получил свой ответ',
                  'Не раздражай вселенную своим невежеством.',
                  sep='\n')
            continue
        else:
            draw_stars(10)
            questions.append(q)
            x = choice(reply)

            step = max(0, (19-len(x))//2)

            print('\n\n\n', ' '*step + x, '\n\n\n', sep="")
            draw_stars_inv(10)
            print()
            print()


ask_oracul()
