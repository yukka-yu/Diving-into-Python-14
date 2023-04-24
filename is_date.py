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

def is_date(date):
    if not isinstance(date, str):
        raise TypeError('Please enter only strings')
    
    date_list = list(map(int, date.split(".")))

    if len(date_list) != 3:
        raise ValueError('Please enter date in format dd.mm.yyyy')
    
    if date_list[2] > 9999 or date_list[2] < 1 or date_list[1] > 12 or date_list[0] > 31:
        return False
    
    elif (date_list[1] in [4, 6, 9, 11]) and date_list[0] > 30:
        return False
    
    elif date_list[1] == 2 and is_leap(date_list[2]) and date_list[0] > 29:
        return False
    
    elif date_list[1] == 2 and not is_leap(date_list[2]) and date_list[0] > 28:
        return False
    
    else:
        return True


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False



if __name__ == "__main__":
    print(is_date("29.02.2004"))