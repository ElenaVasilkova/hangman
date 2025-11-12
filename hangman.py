from random import choice


def get_word() -> str:
    """Получение случайного слова для игры"""
    # распаковка файла
    word_list = ["апельсин", "библиотека", "вертолёт", "галактика", "динозавр",
    "ежевика", "жаворонок", "зоопарк", "ископаемое", "календарь",
    "лаборатория", "магистраль", "небоскрёб", "олимпиада", "панорама",
    "репетитор", "самолёт", "телескоп", "университет", "фестиваль",
    "рак", "ночь", "луна"]
    return choice(word_list).upper()


def validate_letter(player_input: str, used_letters: list) -> bool:
    """Проверка введенного символа"""
    code: int = ord(player_input.upper())
    if player_input.isalpha() and (1040 <= code <= 1071 or code == 1025):
        if player_input not in used_letters:
            return True
        else:
            print('Эта буква уже была.')
            return False
    else:
        print('Введи букву русского алфавита.')
        return False


def validate_answer(valid_answer: str) -> bool:
    """Проверка валидности ответа (да/нет)"""
    if valid_answer.lower() == 'да' or valid_answer.lower() == 'нет':
        return True
    else:
        print('Ответь "да" или "нет".')
        return False


def validate_rus_word(word: str) -> bool:
    """Проверка, что введено русское слово"""
    for char in word:
        code: int = ord(char.upper())
        if 1040 <= code <= 1071 or code == 1025:
            continue
        else:
            print('Слово должно состоять из букв русского алфавита.')
            return False
    else:
        return True


def validate_word(player_input: str, used_words: list) -> bool:
    """Проверка, что слово состоит не вводилось ранее"""
    if validate_rus_word(player_input):
        if player_input.upper() in used_words:
            print('Это слово уже пробовали.\n')
            return False
        else:
            return True
    else:
        return False


def check_letter_in_word(secret_word: str, player_input: str) -> bool:
    """Проверка наличия буквы в слове"""
    if player_input in secret_word:
        print(f'Буква {player_input} есть в этом слове!')
        return True
    else:
        print('Такой буквы в этом слове нет!')
        return False


def check_whole_word(secret_word: str, player_input: str) -> bool:
    """Проверка - угадано ли слово"""
    if player_input.lower() == secret_word.lower():
        return True
    else:
        return False


def display_word_progress(secret_word: str, display_word: list, player_input: str) -> list:
    """Обработка отображения угадывания слова"""
    for i in range(len(secret_word)):
        if secret_word[i] == player_input:
            display_word[i] = player_input
    return display_word


def display_result(attempts: int, used_letters: list, used_words: list) -> None:
    """Вывод на дисплей текущего результата игры"""
    print(draw_gallows(attempts))
    print(f'Количество оставшихся попыток: {attempts}.\n')

    if len(used_letters) > 0:
        print(f'Названные буквы: {", ".join(used_letters)}.\n')

    if len(used_words) > 0:
        print(f'Названные слова: {", ".join(used_words)}.\n')


def draw_gallows(attempts: int) -> str:
    """Отрисовка виселицы"""
    hangman_stages: list = [
        """
           ------
           |    |
           |    0
           |   /|\\
           |    |
           |   / \\
           |
        --------
        """,
        """
            ------
            |    |
            |    O
            |   /|\\
            |    |
            |   /
            |
            |
        --------
        """,
        """
            ------
            |    |
            |    O
            |   /|\\
            |    |
            | 
            |
            |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    |
           | 
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    |
           |   
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
           |
           |
        --------
        """,
        """
            ------
            |    |
            |
            |
            |
            |
            |
            |
        --------
            """]
    return hangman_stages[attempts]


def process_letter_input():
    """Обработка ввода одной буквы"""
    pass


def initialize_round():
    """Инициализация переменных раунда"""
    pass


def game() -> None:
    """Основной игровой цикл"""
    while True:
        guessed: bool = False
        is_letter_valid: bool = True
        used_letters: list = []
        used_words: list = []
        attempts: int = 6
        player_input: str = ''
        secret_word: str = get_word()
        display_word: list = ['*'] * len(secret_word)

        print(draw_gallows(attempts))
        print(f'У тебя {attempts} попыток.\n')
        while not guessed and attempts > 0:
            if is_letter_valid:
                display_word = display_word_progress(
                    secret_word, display_word, player_input
                )
                print(f'{" ".join(display_word)}\n')
                print('Введи одну букву или слово целиком.\n')

            player_input = input().upper()
            if len(player_input) == 1:
                is_letter_valid = validate_letter(player_input, used_letters)
                if is_letter_valid:
                    used_letters.append(player_input)
                    letter_found: bool = check_letter_in_word(secret_word, player_input)
                    if letter_found:
                        display_word = display_word_progress(secret_word, display_word, player_input)
                        guessed = check_whole_word(secret_word, "".join(display_word))
                        display_result(attempts, used_letters, used_words)
                    else:
                        attempts -= 1
                        display_result(attempts, used_letters, used_words)
                        continue
                else:
                    continue

            elif len(player_input) > 1:
                is_word_valid: bool = validate_word(player_input, used_words)
                if is_word_valid:
                    guessed = check_whole_word(secret_word, player_input)
                    if not guessed:
                        attempts -= 1
                        used_words.append(player_input)
                        display_result(attempts, used_letters, used_words)
                else:
                    attempts -= 1

        draw_gallows(attempts)

        if guessed:
            print('Поздравляю! Ты угадал.\n')
            display_word = display_word_progress(secret_word, display_word, player_input)
            display_result(attempts, used_letters, used_words)
            print(f'{" ".join(display_word)}\n')
        else:
            print('Ты проиграл!\n')
            print(f'Загаданное слово: {secret_word.upper()}\n')

        print('Сыграем ещё раз? (да / нет)\n')
        player_answer: str = input()
        validate_answer(player_answer)

        if player_answer == 'да':
            continue
        elif player_answer:
            break
    print('\nСпасибо за игру!')


if __name__ == '__main__':
    print('''
        Давай поиграем в "Виселицу"? (да / нет)
        
        Правила: Нужно угадать загаданное слово, 
        называя буквы, до того как будет полностью 
        нарисована виселица человечком.
        ''')

    while True:
        answer: str = input().lower()
        if validate_answer(answer):
            if answer == 'да':
                game()
                break
            else:
                print('\nВозвращийся, как захочешь поиграть.')
                break
