import constants


def validate_letter(player_input: str, used_letters: set) -> bool:
    """Проверка введенного символа"""
    if not player_input:
        return False

    player_input = player_input.upper()
    if (not player_input.isalpha() or player_input
            not in constants.RUSSIAN_ALPHABET):
        print(constants.INVALID_LETTER)
        return False

    if player_input in used_letters:
        print(constants.LETTER_ALREADY_USED)
        return False

    return True


def validate_answer(valid_answer: str) -> bool:
    """Проверка валидности ответа (да/нет)"""
    if valid_answer.lower() in ['да', 'нет']:
        return True
    else:
        print(constants.INVALID_ANSWER)
        return False


def validate_rus_word(word: str) -> bool:
    """Проверка, что введено русское слово"""
    for char in word:
        if char not in constants.RUSSIAN_ALPHABET:
            print(constants.INVALID_RUSSIAN_WORD)
            return False
    else:
        return True


def validate_word(player_input: str, used_words: set) -> bool:
    """Проверка, что слово не вводилось ранее"""
    player_input_upper = player_input.upper()
    if validate_rus_word(player_input_upper):
        if player_input_upper in used_words:
            print(constants.WORD_ALREADY_USED)
            return False
        else:
            return True
    else:
        return False
