SHA256 Function
===============
Модуль "Функция SHA256" в PasswordsGenerator позволяет вычислять хэш SHA256 заданного пароля. SHA256 - это широко используемая криптографическая хэш-функция, которая производит хэш-значение длиной 256 бит (32 байта). Она часто используется для хэширования паролей и проверки целостности данных.

Для вычисления хэша SHA256 пароля можно использовать функцию `SHA256()`. Вот пример:

.. code-block:: python

   from SHA256 import hash_password

   password = "mysecretpassword"
   hash_value = SHA256(password)
   print(hash_value)

.. automodule:: SHA256.hash_password
   :members:

Это вычислит хэш SHA256 для пароля "mysecretpassword" и выведет его значение.