"""
Модуль для работы со словарем
"""

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
