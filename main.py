"""
Главный модуль приложения Виселица
"""
from constants import COME_BACK_MESSAGE, WELCOME_TEXT

from game import run_game
from validators import validate_answer


def main():
    print(WELCOME_TEXT)

    while True:
        answer: str = input().lower()
        if validate_answer(answer):
            if answer == 'да':
                run_game()
                break
            else:
                print(COME_BACK_MESSAGE)
                break


if __name__ == '__main__':
    main()
