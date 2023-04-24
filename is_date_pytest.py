import pytest
from is_date import *

def test_is_date():
    assert is_date("28.02.2024"), 'Функция не определяет правильную дату'
    assert is_date("29.02.2004"), 'Функция не определяет 29 февраля високосного года'
    assert not is_date("29.02.2003"), 'Функция определяет правильной дату 29 февраля невисокосного года'
    assert not is_date("26.13.2023"), "Функция не выдаёт ошибку на месяц больше 12"
    assert not is_date("26.05.20000"), 'Функция определяет дату с годом больше 9999 как верную'
    assert not is_date("32.05.14"), 'Функция определяет дату с числом больше 31 как верную'

def test_is_leap():
    assert is_leap(2004), 'Не определила високосный год'
    assert not is_leap(2003), 'Определила невисокосный год как високосный'
    assert not is_leap(2100), 'Определила невисокосный год как високосный'


def test_type():
    with pytest.raises(TypeError):
        is_date(3.14)

def test_value():
    with pytest.raises(ValueError):
        is_date('29.12')

if __name__ == '__main__':
    pytest.main(['-v', 'is_date_pytest.py'])