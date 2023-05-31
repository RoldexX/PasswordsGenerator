import hashlib

def md5(password):
    """
    Хэширование пароля с использованием MD5.

    Аргументы:
        password (str): Пароль для хэширования.

    Возвращает:
        str: Хэшированный пароль.
    """
    hash_password = hashlib.md5(password.encode()).hexdigest()
    return hash_password
