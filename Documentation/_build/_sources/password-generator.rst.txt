Password Generator
==================
Модуль "Генератор паролей" в PasswordsGenerator позволяет генерировать случайные пароли с различными опциями. Вы можете указать длину пароля и символы, которые будут включены в него. Сгенерированные пароли предназначены быть надежными и безопасными.

Для генерации пароля с использованием модуля "Генератор паролей" просто вызовите функцию `generate_password()` и укажите необходимые опции в качестве аргументов. Вот пример:

.. code-block:: python

   from PasswordGenerateFunc import password_generator

   password = generate_password(length=12, symbols="qwertyuiop[]asdfghjkl;'\zxcvbnm,./1234567890!@#$%^&*()")
   print(password)

.. automodule:: PasswordGenerateFunc.password_generator
   :members:

Это сгенерирует случайный пароль длиной 12 символов и с необходимыми символами.