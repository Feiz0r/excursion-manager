from typing import Any


def add_user(
    users: list[dict[str, Any]],
    name: str,
    age: int,
    contact: str
) -> dict[str, Any]:
    """Добавить участника в список и вернуть его данные"""
    new_id = 1
    if users:
        new_id = max(user["id"] for user in users) + 1

    user = {
        "id": new_id,
        "name": name,
        "age": age,
        "contact": contact,
    }
    users.append(user)
    return user


def get_user_by_id(
    users: list[dict[str, Any]],
    user_id: int
) -> dict[str, Any] | None:
    """Вернуть участника по id"""
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def find_user(
    users: list[dict[str, Any]],
    query: str
) -> list[dict[str, Any]]:
    """Найти участников по подстроке в имени"""
    query_lower = query.lower()
    return [
        user for user in users
        if query_lower in user["name"].lower()
    ]


def sort_users(
    users: list[dict[str, Any]],
    key: str
) -> list[dict[str, Any]]:
    """Вернуть участников, отсортированных по ключу"""
    allowed = ("id", "name", "age", "contact")
    if key not in allowed:
        raise ValueError(f"Недопустимый ключ: {key}")
    return sorted(users, key=lambda user: user[key])


def remove_user(
    users: list[dict[str, Any]],
    user_id: int
) -> bool:
    """Удалить участника по id"""
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return True
    return False
