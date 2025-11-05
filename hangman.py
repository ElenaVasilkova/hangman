from random import choice


def get_word() -> str:
    """Получения слова для игры"""
    # распаковка файла
    word_list = ["апельсин", "библиотека", "вертолёт", "галактика", "динозавр",
    "ежевика", "жаворонок", "зоопарк", "ископаемое", "календарь",
    "лаборатория", "магистраль", "небоскрёб", "олимпиада", "панорама",
    "репетитор", "самолёт", "телескоп", "университет", "фестиваль"]
    return choice(word_list).upper()


def validate_letter(valid_letter: str, used_letters: list) -> bool:
    """Проверка введеного символа"""
    if valid_letter.isalpha():
        if valid_letter not in used_letters:
            return True
        else:
            print('Эта буква уже была.')
            return False
    else:
        print('Введи букву русского алфавита.')
        return False


def validate_answer(valid_answer: str) -> bool:
    """Проверка валидности ответа (да /нет)"""
    if valid_answer.lower() == 'да' or valid_answer.lower() == 'нет':
        return True
    else:
        print('Ответь "да" или "нет".')
        return False


def validate_word(valid_word: str, played_word: list) -> bool:
    """Проверка, вводилось ли слово ранее"""
    if valid_word.isalpha():
        if valid_word.lower() not in played_word:
            return True
        else:
            print('Это слово уже пробовали.')
            return False
    else:
        print('Слово должно состоять из букв русского алфавита.')
        return False


def check_letter_in_word(letter: str, hidden_word: str) -> bool:
    """Проверка наличия буквы в слове"""
    if letter in hidden_word:
        print(f'Буква {letter} есть в этом слове!')
        return True
    else:
        print('Такой буквы в этом слове нет!')
        return False


def display_word_progress(secret_word: str, display_word: list, player_input: str) -> list:
    '''Обрабатывает прогресс угадывания слова'''

    for i in range(len(secret_word)):
        if secret_word[i] == player_input:
            display_word[i] = player_input

    return display_word


def draw_gallows(attempts: int, guessed_letters: list, guessed_words: list):
    """Отрисовка виселицы в зависимости от количества ошибок"""

    match attempts:
        case 0:
            print("""
           ------
           |    |
           |    0
           |   /|\\
           |    |
           |   / \\
           |
        --------
        """)
        case 1:
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
        case 2:
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
           |    |
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
           |
           |
           |
           |
           |
        --------
        """)
        case 6:
            print("""
            ------
            |    |
            |
            |
            |
            |
            |
            |
        --------
            """)

    print(f'''
        Количество ошибок: {attempts}.
        Названные буквы: {guessed_letters}.
        Названные слова: {guessed_words}.
        ''')


def game():
    '''Основной игровой цикл'''
    guessed: bool = False
    used_letters: list = []
    used_words: list = []
    attempts: int = 6
    player_input: str = ''
    secret_word: str = get_word()
    display_word: list = ['*'] * len(secret_word)
    display_word_progress(secret_word, display_word, player_input)

    while True:


        while attempts > 0 and not guessed:
            print(f'''
            У тебя {attempts} попыток.
            Введи одну букву или слово целиком.
                ''')

            player_input = input().upper()
            if len(player_input) == 1:
                is_letter_valid = validate_letter(player_input)
                used_letters.append(player_input)
                if is_letter_valid:
                    letter_found = check_letter_in_word(player_input, secret_word)
                    if letter_found:
                        guessed_word = player_input# проверить, открыты ли все буквы в слове
                        if guessed_word:
                            break
                            # Вы выиграли
                        else:
                            attempts -= 1
                    else:
                        used_letters.append(player_input)
                        attempts -= 1
                        display_word_progress(secret_word, player_input)
                else:
                    display_word_progress(secret_word, player_input)
                    # повторить ввод
            elif len(player_input) > 1:
                is_word_valid = validate_word(player_input, used_words)
                if is_word_valid:
                    if player_input == secret_word:
                        break
                        # Вы выиграли
                    else:
                        used_words.append(player_input)
                        attempts -= 1
                else:
                    break
                    # повторить ввод
                used_words.append(player_input)
                attempts -= 1
                # Повторить ввод

        draw_gallows(attempts, used_letters, used_words)

        print('Сыграем ещё раз? (да / нет)\n')
        player_answer: str = input()
        validate_answer(player_answer)

        if player_answer == 'да':
            attempts = 6
            continue
        elif player_answer:
            break
    print('\nСпасибо за игру!')


if __name__ == '__main__':
    print('''
        Давай поиграем в "Виселицу"? (да / нет)
        
        Нужно угадать загаданное слово, называя буквы, 
        до того как будет полностью нарисована виселица
        с человечком.
        ''')

    while True:
        answer: str = input().lower()
        if validate_answer(answer):
            if answer == 'да':
                game()
            else:
                print('\nВозвращийся, как захочешь поиграть.')
                break
        else:
            continue
