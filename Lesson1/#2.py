# Условие 2:
# На складе лежат разные фрукты в разном количестве. Нужно написать функцию, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе.

def fruit_basket(**kwargs):
    {print(f"Фрукт {name} в количестве {values} шт")
     for name, values in kwargs.items()}
    return print(f'Общее количество фрутов: {sum(kwargs.values())}')
fruit_basket(
    apple = 23,
    orange = 15,
    lemon = 5
)
# Фрукт apple в количестве 23 шт
# Фрукт orange в количестве 15 шт
# Фрукт lemon в количестве 5 шт
# Общее количество фрутов: 43