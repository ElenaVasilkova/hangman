from random import choice


def get_word() -> str:
    """Получения слова для игры"""
    # распаковка файла
    word_list = ["апельсин", "библиотека", "вертолёт", "галактика", "динозавр",
    "ежевика", "жаворонок", "зоопарк", "ископаемое", "календарь",
    "лаборатория", "магистраль", "небоскрёб", "олимпиада", "панорама",
    "репетитор", "самолёт", "телескоп", "университет", "фестиваль"]
    return choice(word_list).upper()


def is_valid_letter(letter: str) -> bool:
    """Проверка введеного символа"""
    if letter


def is_valid_answer(answer: str) -> bool:
    """Проверка валидности ответа (да /нет)"""
    pass


def is_letter_in_word(letter: str, word: str) -> bool:
    """Проверка наличия буквы в слове"""
    pass


def draw_gallows(errors_count: int) -> str:
    """Отрисовка виселицы в зависимости от количества ошибок"""
    match errors_count:
        case 0:
            print("""
           ------
           |    |
           |
           |
           |
           |
           |
        --------
        """)
        case 1:
            print("""
            ------
            |    |
            |    O
            | 
            | 
            | 
            |
            |
        --------
        """)
        case 2:
            print("""
            ------
            |    |
            |    O
            |    |
            |    |
            | 
            |
            |
        --------
        """)
        case 3:
            print("""
           ------
           |    |
           |    O
           |   /|
           |    |
           | 
           |
           |
        --------
        """)
        case 4:
            print("""
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |   
           |
           |
        --------
        """)
        case 5:
            print("""
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |   / 
           |
           |
        --------
        """)
        case 6:
            print(""""
            ------
            |    |
            |    O
            |   /|\\
            |    |
            |   / \\
            |
            |
        --------
            """)

    print(f'Количество ошибок: {errors_count}')


def processing_guess(letter: str, word: str):
    """Обработка угадывания слова"""
    errors_count: int = 0
    is_valid_letter(letter)     # валидация буквы

    if is_letter_in_word(letter, word):
        errors_count += 1

    draw_gallows(errors_count)


def game():

    while True:
        word: str = get_word()
        letters_count: int = len(word)
        hidden_word = '*' * letters_count
        print(f'''
            {hidden_word}
        ''')

        print(f'''
        У тебя 6 попыток.
        Введи одну букву или слово целиком.
            ''')  # Добавить подсчет количества оставшихся попыток
        letter: str = input().upper()
        processing_guess(letter, word)

        print('Сыграем ещё раз? (да / нет)')
        answer_game: str = input()
        is_valid_answer(answer_game)

        if answer == 'да':
            continue
        else:
            break


if __name__ == '__main__':
    print('''
        Давай поиграем в "Виселицу"? (да / нет)
        
        Нужно угадать загаданное слово, называя буквы, 
        до того как будет полностью нарисована виселица
        с человечком.
        ''')
    answer: str = input()
    is_valid_answer(answer)

    game() if answer == 'да' else print()

    print('Спасибо за игру!')
