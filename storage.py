import json
from typing import Any


def load_data(filename: str) -> list[dict[str, Any]]:
    """Загрузить список словарей из JSON-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден — данные пусты.")
        return []
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён — данные пусты.")
        return []


def save_data(
    filename: str,
    data: list[dict[str, Any]]
) -> None:
    """Сохранить список словарей в JSON-файл"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Не удалось сохранить {filename}: {error}")


def load_users(filename: str) -> list[dict[str, Any]]:
    return load_data(filename)


def save_users(
    filename: str,
    users: list[dict[str, Any]]
) -> None:
    save_data(filename, users)


def load_excursions(filename: str) -> list[dict[str, Any]]:
    return load_data(filename)


def save_excursions(
    filename: str,
    excursions: list[dict[str, Any]]
) -> None:
    save_data(filename, excursions)


def load_groups(filename: str) -> list[dict[str, Any]]:
    return load_data(filename)


def save_groups(
    filename: str,
    groups: list[dict[str, Any]]
) -> None:
    save_data(filename, groups)


def load_enrollments(filename: str) -> list[dict[str, Any]]:
    return load_data(filename)


def save_enrollments(
    filename: str,
    enrollments: list[dict[str, Any]]
) -> None:
    save_data(filename, enrollments)
