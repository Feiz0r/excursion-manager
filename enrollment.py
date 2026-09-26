from typing import Any


def enroll_user(
    enrollments: list[dict[str, Any]],
    user_id: int,
    excursion_id: int,
    group_id: int
) -> dict[str, Any] | None:
    """Записать участника."""
    if is_user_enrolled(enrollments, user_id, excursion_id):
        return None

    new_id = 1
    if enrollments:
        new_id = max(
            enrollment["id"] for enrollment in enrollments
        ) + 1

    enrollment = {
        "id": new_id,
        "user_id": user_id,
        "excursion_id": excursion_id,
        "group_id": group_id,
    }
    enrollments.append(enrollment)
    return enrollment


def is_user_enrolled(
    enrollments: list[dict[str, Any]],
    user_id: int,
    excursion_id: int
) -> bool:
    """Проверить, записан ли участник на экскурсию"""
    for enrollment in enrollments:
        if (enrollment["user_id"] == user_id
                and enrollment["excursion_id"] == excursion_id):
            return True
    return False


def cancel_enrollment(
    enrollments: list[dict[str, Any]],
    enrollment_id: int
) -> bool:
    """Отменить запись по id"""
    for index, enrollment in enumerate(enrollments):
        if enrollment["id"] == enrollment_id:
            enrollments.pop(index)
            return True
    return False


def find_enrollments_by_user(
    enrollments: list[dict[str, Any]],
    user_id: int
) -> list[dict[str, Any]]:
    """Вернуть все записи участника"""
    return [
        enrollment for enrollment in enrollments
        if enrollment["user_id"] == user_id
    ]


def find_enrollments_by_group(
    enrollments: list[dict[str, Any]],
    group_id: int
) -> list[dict[str, Any]]:
    """Вернуть все записи группы"""
    return [
        enrollment for enrollment in enrollments
        if enrollment["group_id"] == group_id
    ]


def count_enrolled(
    enrollments: list[dict[str, Any]],
    group_id: int
) -> int:
    """Посчитать, сколько участников записано в группу"""
    return len(find_enrollments_by_group(enrollments, group_id))


def get_enrollment_status(is_enrolled: bool) -> str:
    """Вернуть текстовый статус записи"""
    if is_enrolled:
        return "Участник уже записан"
    return "Участник ещё не записан"
