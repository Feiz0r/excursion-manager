from typing import Any


def add_group(
    groups: list[dict[str, Any]],
    excursion_id: int,
    name: str,
    capacity: int
) -> dict[str, Any]:
    """Добавить группу и вернуть её данные"""
    new_id = 1
    if groups:
        new_id = max(group["id"] for group in groups) + 1

    group = {
        "id": new_id,
        "excursion_id": excursion_id,
        "name": name,
        "capacity": capacity,
    }
    groups.append(group)
    return group


def find_group(
    groups: list[dict[str, Any]],
    query: str
) -> list[dict[str, Any]]:
    """Найти группы по подстроке в названии"""
    query_lower = query.lower()
    return [
        group for group in groups
        if query_lower in group["name"].lower()
    ]


def filter_groups_by_excursion(
    groups: list[dict[str, Any]],
    excursion_id: int
) -> list[dict[str, Any]]:
    """Вернуть группы указанной экскурсии"""
    return [
        group for group in groups
        if group["excursion_id"] == excursion_id
    ]


def check_group_capacity(
    groups: list[dict[str, Any]],
    group_id: int,
    min_capacity: int
) -> bool:
    """Проверить, вмещает ли группа не меньше min_capacity"""
    for group in groups:
        if group["id"] == group_id:
            return group["capacity"] >= min_capacity
    return False


def sort_groups(
    groups: list[dict[str, Any]],
    key: str
) -> list[dict[str, Any]]:
    """Вернуть группы, отсортированные по ключу"""
    allowed = ("id", "excursion_id", "name", "capacity")
    if key not in allowed:
        raise ValueError(f"Недопустимый ключ: {key}")
    return sorted(groups, key=lambda group: group[key])


def remove_group(
    groups: list[dict[str, Any]],
    group_id: int
) -> bool:
    """Удалить группу по id"""
    for index, group in enumerate(groups):
        if group["id"] == group_id:
            groups.pop(index)
            return True
    return False
