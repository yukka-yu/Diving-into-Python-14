'''Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
Проверку года на високосность вынести в отдельную
защищённую функцию. '''


def is_date(date: str) -> bool:
    """
    Определяет, является ли введённая строка записью даты. Диапазон возможных значений года: 1-9999.

    >>> is_date("29.02.2004")
    True

    >>> is_date("32.05.2024")
    False

    >>> is_date(3.14)
    Traceback (most recent call last):
    ...
    TypeError: Please enter only strings

    >>> is_date("29.12")
    Traceback (most recent call last):
    ...
    ValueError: Please enter date in format dd.mm.yyyy
    """
    if not isinstance(date, str):
        raise TypeError('Please enter only strings')
    
    date_list = list(map(int, date.split(".")))

    if len(date_list) != 3:
        raise ValueError('Please enter date in format dd.mm.yyyy')

    if date_list[2] > 9999 or date_list[2] < 1 or date_list[1] > 12 or date_list[0] > 31:
        return False
    
    elif (date_list[1] in [4, 6, 9, 11]) and date_list[0] > 30:
        return False
    
    elif date_list[1] == 2 and _is_leap(date_list[2]) and date_list[0] > 29:
        return False
    
    elif date_list[1] == 2 and not _is_leap(date_list[2]) and date_list[0] > 28:
        return False
    
    else:
        return True


def _is_leap(year):
    """
    Определяет, является ли год високосным

    >>> _is_leap(1)
    False

    >>> _is_leap(4)
    True

    >>> _is_leap(100)
    False
    """

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    
    else:
        return False


if __name__ == "__main__":
    #print(is_date("29.02.2004"))
    import doctest
    doctest.testmod(verbose=True)