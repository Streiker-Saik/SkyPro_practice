def the_list_is_less_average(numbers_list: list[int]) -> list[int]:
    """
    Функция получает на вход список чисел и возвращает новый список, содержащий только числа,
    которые меньше среднего значения списка.
    """
    average = sum(numbers_list) / len(numbers_list)
    return [number for number in numbers_list if number < average]

    # numbers_list_new = []
    # for number in numbers_list:
    #     if number < average:
    #         numbers_list_new.append(number)
    # return numbers_list_new


def unique_list_strings(strings_list: list[str]) -> list[str]:
    """Функция получает на вход список строк и возвращает новый список, содержащий только уникальные строки"""
    return list(set(strings_list))

    # unique_list = []
    # for string in strings_list:
    #     if string not in unique_list:
    #         unique_list.append(string)
    # return unique_list


def sorting_the_list_of_collages(products_list: list[tuple]) -> list[tuple]:
    """
    Функция получает на вход список кортежей, содержащих информацию о товарах (название, цена),
    и возвращает новый список, отсортированный по убыванию цены
    """
    return sorted(products_list, key=lambda product: product[-1], reverse=True)


def screening_by_list_value(movie_list_and_genre: tuple[list[dict], str]) -> list:
    """
    Функция получает на вход список словарей, содержащих информацию о фильмах (например, название, жанр, режиссер),
    и возвращает новый список, содержащий только те фильмы, которые относятся к заданному жанру
    """
    movie_list = movie_list_and_genre[0]
    genre = movie_list_and_genre[1]
    return [movie for movie in movie_list if movie.get("genre") == genre]

    # list_of_films_by_genre = []
    # for movie in movie_list:
    #     if movie.get("genre") == genre:
    #         list_of_films_by_genre.append(movie)
    # return list_of_films_by_genre
