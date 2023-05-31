import random


def password_generator(length, characters):
    """
    Генерирует случайный пароль заданной длины из заданных символов.

    Аргументы:
        length (int): Длина пароля.
        characters (str): Строка символов, из которых будет генерироваться пароль.

    Возвращает:
        str: Сгенерированный пароль.
    """
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
