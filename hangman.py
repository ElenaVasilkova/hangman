from random import choice


def get_word() -> str:
    """Получения слова для игры"""
    # распаковка файла
    word_list = ["апельсин", "библиотека", "вертолёт", "галактика", "динозавр",
    "ежевика", "жаворонок", "зоопарк", "ископаемое", "календарь",
    "лаборатория", "магистраль", "небоскрёб", "олимпиада", "панорама",
    "репетитор", "самолёт", "телескоп", "университет", "фестиваль"]
    return choice(word_list)


def is_valid_letter(letter: str) -> bool:
    """Проверка введеного символа"""
    pass


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


print('Описание игры')

while True:
    word: str = get_word()
    letters_count: int = len(word)
    hidden_word = '*' * letters_count
    print(hidden_word)
    print('Запрос ввода буквы')
    letter: str = input()
    processing_guess(letter, word)
    print('Сыграем ещё раз? (да / нет)')
    answer: str = input()
    is_valid_answer(answer)

    if answer == 'да':
        continue
    else:
        break

print('Спасибо за игру')
