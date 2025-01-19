def repeating_numbers(numbers_tuple_list: tuple[list[int], list[int]]) -> list[int]:
    """
    Функция получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые встречаются в обоих списках
    """
    numbers_list_one = set(numbers_tuple_list[0])
    numbers_list_two = set(numbers_tuple_list[1])
    return [numbers for numbers in numbers_list_one if numbers in numbers_list_two]

    # repeating_numbs_list = []
    # for numbers in numbers_list_one:
    #     if numbers in numbers_list_two:
    #         repeating_numbs_list.append(numbers)
    # return repeating_numbs_list


def palindrome_numbers(numbers_list: list[int]) -> list[int]:
    """
    Функция получает на вход список чисел и возвращает новый список, содержащий только числа,
    которые являются палиндромами
    """
    return [numbers for numbers in numbers_list if str(numbers) == str(numbers)[::-1]]

    # palindrome_list = []
    # for numbers in numbers_list:
    #     numbers_string = str(numbers)
    #     reversed_numbers_string = "".join(reversed(numbers_string))
    #     if numbers_string == reversed_numbers_string:
    #         palindrome_list.append(numbers)
    # return palindrome_list


def unique_numbers(numbers_tuple_list: tuple[list[int], list[int]]) -> list[int]:
    """
    Функция получает на вход два списка чисел и возвращает новый список, содержащий только те числа,
    которые есть только в одном из списков
    """
    set_one = set(numbers_tuple_list[0])
    set_two = set(numbers_tuple_list[1])
    # difference_set_one = set_one.difference(set_two)
    # difference_set_two = set_two.difference(set_one)
    difference_set = set_one.difference(set_two) | set_two.difference(set_one)

    return list(difference_set)

    # unique_number_list = []
    # for numbers in numbers_list_one:
    #     if numbers not in numbers_list_two:
    #         unique_number_list.append(numbers)
    # for numbers in numbers_list_two:
    #     if numbers not in numbers_list_one:
    #         unique_number_list.append(numbers)
    # return unique_number_list
