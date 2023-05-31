import hashlib


def hash_password(password):
    """
        Хэширование пароля с использованием алгоритма SHA256.

        Аргументы:
            password (str): Пароль для хэширования.

        Возвращает:
            str: Хэшированный пароль.
        """
    password = hashlib.sha256(password.encode()).hexdigest()
    return password
