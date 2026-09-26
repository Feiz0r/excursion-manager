from typing import Any


def add_excursion(
    excursions: list[dict[str, Any]],
    title: str,
    date: str,
    place: str,
    capacity: int
) -> dict[str, Any]:
    """Добавить экскурсию и вернуть её данные"""
    new_id = 1
    if excursions:
        new_id = max(excursion["id"] for excursion in excursions) + 1

    excursion = {
        "id": new_id,
        "title": title,
        "date": date,
        "place": place,
        "capacity": capacity,
    }
    excursions.append(excursion)
    return excursion


def find_excursion(
    excursions: list[dict[str, Any]],
    query: str
) -> list[dict[str, Any]]:
    """Найти экскурсии по подстроке в названии"""
    query_lower = query.lower()
    return [
        excursion for excursion in excursions
        if query_lower in excursion["title"].lower()
    ]


def check_excursion_capacity(
    excursions: list[dict[str, Any]],
    excursion_id: int,
    min_capacity: int
) -> bool:
    """Проверить, вмещает ли экскурсия не меньше min_capacity"""
    for excursion in excursions:
        if excursion["id"] == excursion_id:
            return excursion["capacity"] >= min_capacity
    return False


def sort_excursions(
    excursions: list[dict[str, Any]],
    key: str
) -> list[dict[str, Any]]:
    """Вернуть экскурсии, отсортированные по ключу"""
    allowed = ("id", "title", "date", "place", "capacity")
    if key not in allowed:
        raise ValueError(f"Недопустимый ключ: {key}")
    return sorted(excursions, key=lambda excursion: excursion[key])


def remove_excursion(
    excursions: list[dict[str, Any]],
    excursion_id: int
) -> bool:
    """Удалить экскурсию по id"""
    for index, excursion in enumerate(excursions):
        if excursion["id"] == excursion_id:
            excursions.pop(index)
            return True
    return False
