"""
Основной игровой модуль
"""

import constants
from display import draw_gallows
from validators import validate_answer, validate_letter, validate_word
from words import get_word


def check_letter_in_word(secret_word: str, player_input: str) -> bool:
    """Проверка наличия буквы в слове"""
    if player_input in secret_word:
        print(constants.LETTER_FOUND.format(player_input))
        return True
    else:
        print(constants.LETTER_NOT_FOUND)
        return False


def check_whole_word(secret_word: str, player_input: str) -> bool:
    """Проверка - угадано ли слово"""
    return player_input.upper() == secret_word.upper()


def ask_play_again() -> bool:
    """Запрос на повторную игру"""
    while True:
        answer: str = input(constants.PLAY_AGAIN_PROMPT).strip().lower()
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
    print(constants.REMAINING_ATTEMPTS, attempts)

    if len(used_letters) > 0:
        print(constants.NAMED_LETTERS, ", ".join(used_letters))

    if len(used_words) > 0:
        print(constants.NAMED_WORDS, ", ".join(used_words))


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


def run_game() -> None:
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
        print(constants.INITIAL_ATTEMPTS.format(attempts))

        while not is_guessed and attempts > 0:
            display_word = display_word_progress(
                secret_word, display_word, player_input)
            print(" ".join(display_word))
            print(constants.INPUT_INVITATION)

            player_input = input().upper().strip()

            if not player_input:
                print(constants.EMPTY_INPUT_WARNING)
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

        # Завершение игры
        if is_guessed:
            print(constants.WIN)
            display_word = display_word_progress(secret_word, display_word, player_input)
            print(" ".join(display_word))
        else:
            print(constants.LOSE)
            print(constants.SECRET_WORD_REVEAL, secret_word.upper())

        if not ask_play_again():
            break

    print(constants.THANKS)
