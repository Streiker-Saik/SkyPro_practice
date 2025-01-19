import re
from typing import Any


def extract_names(filename: Any) -> list[str]:
    """Функция получает на входе txt файл, выводит список слов, кроме цифр/знаков препинания"""
    with open(filename, "r", encoding="utf-8") as text:
        content = text.read()
        # Удаляем знаки препинания и цифры, а также разбиваем строки по пробелам
        pattern = r"[^\w\s]|[\d]+"  # Знаки препинания и цифры
        cleaned_content = re.sub(pattern, "", content)
        # Разбиваем текст на строки и удаляем пустые строки
        # names = []
        # for name in cleaned_content.splitlines():
        #     if name.strip():
        #         names.append(name.strip())
        names = [name.strip() for name in cleaned_content.splitlines() if name.strip()]
        return names


def is_russian(name: str) -> bool:
    """Функция определяет наличие русских букв"""
    return bool(re.search(r"[а-яА-Я]", name))


def is_english(name: str) -> bool:
    """Функция определяет наличие английских букв"""
    return bool(re.search(r"[a-zA-Z]", name))


def main(names: list[str]) -> Any:
    """Функция создает файл в директории "data" файлы: русские имена и английские имена с сортировкой"""
    # names = extract_names(filename)
    names_rus = sorted([name for name in names if is_russian(name)])
    names_eng = sorted([name for name in names if is_english(name)])
    with open("data/names_rus.txt", "w", encoding="utf-8") as text:
        text.write("\n".join(names_rus))
    with open("data/names_eng.txt", "w", encoding="utf-8") as text:
        text.write("\n".join(names_eng))
    return names_rus, names_eng
