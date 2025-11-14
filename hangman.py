from random import choice


def get_word() -> str:
    """Получение случайного слова для игры"""
    try:
        with open("words.txt", 'r', encoding='utf-8') as file:
            word_list = file.readlines()
        word = choice(word_list).rstrip().upper()
        return word
    except FileNotFoundError:
        word_list = ["АПЕЛЬСИН", "БИБЛИОТЕКА", "ВЕРТОЛЁТ", "ГАЛАКТИКА", "ДИНОЗАВР",
                     "ЕЖЕВИКА", "ЖАВОРОНОК", "ЗООПАРК", "ИСКОПАЕМОЕ", "КАЛЕНДАРЬ",
                     "ЛАБОРАТОРИЯ", "МАГИСТРАЛЬ", "НЕБОСКРЁБ", "ОЛИМПИАДА", "ПАНОРАМА",
                     "РЕПЕТИТОР", "САМОЛЁТ", "ТЕЛЕСКОП", "УНИВЕРСИТЕТ", "ФЕСТИВАЛЬ",
                     "РАК", "НОЧЬ", "ЛУНА"]
        word = choice(word_list).upper()
        return word


def validate_letter(player_input: str, used_letters: set) -> bool:
    """Проверка введенного символа"""
    if not player_input:
        return False

    player_input = player_input.upper()
    if (not player_input.isalpha() or player_input
            not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
        print('Введи букву русского алфавита.')
        return False

    if player_input in used_letters:
        print('Эта буква уже была.')
        return False

    return True


def validate_answer(valid_answer: str) -> bool:
    """Проверка валидности ответа (да/нет)"""
    if valid_answer.lower() in ['да', 'нет']:
        return True
    else:
        print('Ответь "да" или "нет".')
        return False


def validate_rus_word(word: str) -> bool:
    """Проверка, что введено русское слово"""
    for char in word:
        if char not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            print('Слово должно состоять из букв русского алфавита.')
            return False
    else:
        return True


def validate_word(player_input: str, used_words: set) -> bool:
    """Проверка, что слово не вводилось ранее"""
    player_input_upper = player_input.upper()
    if validate_rus_word(player_input_upper):
        if player_input_upper in used_words:
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
    return player_input.upper() == secret_word.upper()


def ask_play_again() -> bool:
    """Запрос на повторную игру"""
    while True:
        answer: str = input('Сыграем ещё раз? (да/нет): ').strip().lower()
        if validate_answer(answer):
            return answer == 'да'


def display_word_progress(secret_word: str, display_word: list, player_input: str) -> list:
    """Обработка отображения угадывания слова"""
    for i in range(len(secret_word)):
        if secret_word[i] == player_input:
            display_word[i] = player_input
    return display_word


def display_result(attempts: int, used_letters: set, used_words: set) -> None:
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


def process_letter_guess(secret_word: str, display_word: list, used_letters: set,
                         player_input: str) -> tuple[list, bool, bool]:
    """Обработка попытки угадать букву"""
    is_decrease_attempts: bool = False
    if not validate_letter(player_input, used_letters):
        is_guessed = False
        return display_word, is_guessed, is_decrease_attempts

    used_letters.add(player_input)
    letter_found = check_letter_in_word(secret_word, player_input)

    if letter_found:
        new_display_word = display_word_progress(secret_word, display_word, player_input)
        is_guessed = ("".join(new_display_word) == secret_word)
        return new_display_word, is_guessed, is_decrease_attempts
    else:
        is_guessed = False
        is_decrease_attempts = True
        return display_word, is_guessed, is_decrease_attempts


def process_word_guess(secret_word: str, used_words: set, player_input: str
                       ) -> tuple[bool, bool]:
    """Обработка попытки угадать слово"""
    is_decrease_attempts: bool = False
    if not validate_word(player_input, used_words):
        is_guessed = False
        is_decrease_attempts = True
        return is_guessed, is_decrease_attempts

    used_words.add(player_input.upper())
    is_guessed = check_whole_word(secret_word, player_input)
    is_decrease_attempts = not is_guessed
    return is_guessed, is_decrease_attempts


def game() -> None:
    """Основной игровой цикл"""
    while True:
        is_guessed: bool = False
        used_letters: set = set()
        used_words: set = set()
        attempts: int = 6
        player_input: str = ''
        secret_word: str = get_word()
        display_word: list = ['*'] * len(secret_word)

        print(draw_gallows(attempts))
        print(f'У тебя {attempts} попыток.\n')

        while not is_guessed and attempts > 0:
            display_word = display_word_progress(
                secret_word, display_word, player_input)
            print(f'{" ".join(display_word)}\n')
            print('Введи одну букву или слово целиком.\n')

            player_input = input().upper().strip()

            if not player_input:
                print('Введи букву или слово.\n')
                continue

            is_decrease_attempts: bool = False

            if len(player_input) == 1:
                display_word, is_guessed, is_decrease_attempts = process_letter_guess(
                    secret_word, display_word, used_letters, player_input
                )

            elif len(player_input) > 1:
                is_guessed, is_decrease_attempts = process_word_guess(
                    secret_word, used_words, player_input)

            if is_decrease_attempts:
                attempts -= 1

            display_result(attempts, used_letters, used_words)

        if is_guessed:
            print('Поздравляю! Ты угадал.\n')
            display_word = display_word_progress(secret_word, display_word, player_input)
            print(f'{" ".join(display_word)}\n')
        else:
            print('Ты проиграл!\n')
            print(f'Загаданное слово: {secret_word.upper()}\n')

        if not ask_play_again():
            break

    print('\nСпасибо за игру!')


if __name__ == '__main__':
    print('''
        Давай поиграем в "Виселицу"? (да / нет)
        
        Правила: Нужно угадать загаданное слово, 
        называя буквы, до того как будет полностью 
        нарисована виселица c человечком.
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
