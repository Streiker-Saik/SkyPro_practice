from src.lesson_8_2 import (screening_by_list_value, sorting_the_list_of_collages, the_list_is_less_average,
                            unique_list_strings)
from src.lesson_9_1 import palindrome_numbers, repeating_numbers, unique_numbers
from src.lesson_9_2 import extract_names, main

print("Урок 8.2")
print("Задание_1")
numbers_list = [1, 2, 3, 4, 5]
print(the_list_is_less_average(numbers_list))

print("Задание_2")
strings_list = ["apple", "banana", "orange", "apple"]
print(unique_list_strings(strings_list))

print("Задание_3")
products_list = [("apple", 2.5), ("banana", 3.5), ("orange", 1.5)]
print(sorting_the_list_of_collages(products_list))

print("Задание_4")
movie_list_and_genre = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "director": "Frank Darabont"},
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
], "Drama"
print(screening_by_list_value((movie_list_and_genre)))

print("Урок 9.1")
print("Задание_1")
numbers_tuple_list = ([1, 2, 3, 4], [3, 4, 5, 6])
print(repeating_numbers(numbers_tuple_list))

print("Задание_2")
numbers_list = [121, 123, 131, 34543]
print(palindrome_numbers(numbers_list))

print("Задание_3")
numbers_tuple_list = ([1, 2, 3, 4], [3, 4, 5, 6])
print(unique_numbers((numbers_tuple_list)))

# filename = ("C:/Users/strei.TECHOTDEL/PycharmProjects/PythonProject/data/names.txt")
# directory = ("C:/Users/strei.TECHOTDEL/PycharmProjects/PythonProject/data")

print("Урок 9.2")
filename = "data/names.txt"
names = extract_names(filename)
print(names)
main(names)
