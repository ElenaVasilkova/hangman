from random import randint


def word() -> str:
    pass


def is_valid_letter(letter: str) -> bool:
    pass


def is_valid_answer(answer: str) -> bool:
    pass


def is_letter_in_word(letter: str) -> bool:
    pass


def drawing_of_gallows(number_of_errors: int) -> str:
    pass


def output_of_result(letter: str):
    number_of_errors: int = 0
    is_valid_letter(letter)     # валидация буквы
    is_letter_in_word(letter)  # проверка наличия буквы в слове
    print('Счетчик ошибок')
    print('Текущее состояние висилицы') # ASCII


print('Описание игры')

while True:
    print('Запрос ввода буквы')
    letter: str = input()
    output_of_result(letter)
    print('Сыграем ещё раз? (да / нет)')
    answer: str = input()
    is_valid_answer(answer)

    if answer == 'да':
        continue
    else:
        break

print('Спасибо за игру')
