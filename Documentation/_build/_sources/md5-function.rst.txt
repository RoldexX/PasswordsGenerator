MD5 Function
============

Модуль "Функция MD5" в PasswordsGenerator позволяет вычислять хэш MD5 заданного пароля. MD5 - это широко используемая криптографическая хэш-функция, которая производит хэш-значение длиной 128 бит (16 байт). Однако MD5 считается менее безопасным по сравнению с более современными хэш-функциями.

Для вычисления хэша MD5 пароля можно использовать функцию `MD5()`. Вот пример:

.. code-block:: python

   from password_generator import MD5

   password = "mysecretpassword"
   hash_value = MD5(password)
   print(hash_value)

.. automodule:: MD5.md5

Это вычислит хэш MD5 для пароля "mysecretpassword" и выведет его значение.