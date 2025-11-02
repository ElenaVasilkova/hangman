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
    # проверить, что введеный символ - буква
    # проверить, вводилась ли буква ранее


def is_valid_answer(answer: str) -> bool:
    """Проверка валидности ответа (да /нет)"""
    pass


def is_valid_word(letter: str) -> bool:
    """Проверка введеного символа"""
    # проверить, вводилось ли слово ранее


def is_letter_in_word(letter: str, word: str) -> bool:
    """Проверка наличия буквы в слове"""
    if is_valid_letter(letter):
        # проверяем наличие буквы в слове
        pass
    else:
        # просим повторно ввести букву
        pass


def draw_gallows(errors_count: int, guessed_letters: list, guessed_words: list) -> str:
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

    print(f'''
        Количество ошибок: {errors_count}.
        Названные буквы: {guessed_letters}.
        Названные слова: {guessed_words}.
        ''')



def processing_guess(letter: str, word: str, guessed_letters: list, guessed_words: list):
    """Обработка угадывания слова"""
    errors_count: int = 0

    if len(letter) == 1:
        if not is_letter_in_word(letter, word):
            errors_count += 1
            guessed_letters.append(letter)
        else:
            pass
            # открываем буквы
    elif letter == word:
        return True
    elif len(letter) > 1 and letter != word:
        errors_count += 1
        guessed_words.append(letter)

    draw_gallows(errors_count, guessed_letters, guessed_words)
    return False


def game():
    guessed: bool = False
    guessed_letters: list = []
    guessed_words: list = []
    tries = 6

    while tries > 0 and not guessed:
        word: str = get_word()
        letters_count: int = len(word)
        hidden_word = '*' * letters_count
        print(f'''
            {hidden_word}
        ''')

        print(f'''
        У тебя {tries} попыток.
        Введи одну букву или слово целиком.
            ''')
        tries -= 1
        letter: str = input().upper()
        guessed = processing_guess(letter, word, guessed_letters, guessed_words)

        if guessed is True:
            # Выводим результат
            break

        print('Сыграем ещё раз? (да / нет)\n')
        answer_game: str = input()
        is_valid_answer(answer_game)

        if answer_game == 'да':
            tries = 6
            continue
        elif answer_game:
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

    print('\nСпасибо за игру!')
