from typing import Any

import enrollment
import excursion
import group
import storage
import user
import utils


def show_users(users: list[dict[str, Any]]) -> None:
    """Вывести список участников"""
    for user_data in users:
        print(f"{user_data['id']}. {user_data['name']}, "
              f"{user_data['age']} лет, {user_data['contact']}")


def show_excursions(excursions: list[dict[str, Any]]) -> None:
    """Вывести список экскурсий"""
    for excursion_data in excursions:
        print(f"{excursion_data['id']}. {excursion_data['title']}, "
              f"{excursion_data['date']}, {excursion_data['place']}, "
              f"до {excursion_data['capacity']} чел.")


def show_groups(groups: list[dict[str, Any]]) -> None:
    """Вывести список групп"""
    for group_data in groups:
        print(f"{group_data['id']}. {group_data['name']} "
              f"(экскурсия {group_data['excursion_id']}), "
              f"до {group_data['capacity']} чел.")


def show_enrollments(enrollments: list[dict[str, Any]]) -> None:
    """Вывести список записей."""
    for enrollment_data in enrollments:
        print(f"{enrollment_data['id']}. "
              f"участник {enrollment_data['user_id']} -> "
              f"экскурсия {enrollment_data['excursion_id']}, "
              f"группа {enrollment_data['group_id']}")


def menu_user(users: list[dict[str, Any]]) -> None:
    """Меню работы с участниками"""
    while True:
        print(
            "Меню пользователей\n"
            "   1. Добавить пользователя\n"
            "   2. Найти пользователя\n"
            "   3. Отсортировать пользователей\n"
            "   4. Вывести пользователей\n"
            "   5. Удалить пользователя\n"
            "   0. Выход"
        )
        mode = utils.input_int("Действие: ")
        match mode:
            case 1:
                name = utils.input_str("Имя: ")
                age = utils.input_int("Возраст: ")
                contact = utils.input_str("Контакт: ")
                user.add_user(users, name, age, contact)
            case 2:
                query = utils.input_str("Поиск по: ")
                show_users(user.find_user(users, query))
            case 3:
                key = utils.input_str("Ключ сортировки: ")
                try:
                    show_users(user.sort_users(users, key))
                except ValueError as error:
                    print(error)
            case 4:
                show_users(users)
            case 5:
                user_id = utils.input_int("ID участника: ")
                user.remove_user(users, user_id)
            case 0:
                return
            case _:
                print("Ошибка! Неверное число.")


def menu_excursion(excursions: list[dict[str, Any]]) -> None:
    """Меню работы с экскурсиями"""
    while True:
        print(
            "Меню экскурсий\n"
            "   1. Добавить экскурсию\n"
            "   2. Найти экскурсию\n"
            "   3. Проверить вместимость\n"
            "   4. Отсортировать экскурсии\n"
            "   5. Вывести экскурсии\n"
            "   6. Удалить экскурсию\n"
            "   0. Выход"
        )
        mode = utils.input_int("Действие: ")
        match mode:
            case 1:
                title = utils.input_str("Название: ")
                date = utils.input_str("Дата: ")
                place = utils.input_str("Место: ")
                capacity = utils.input_int("Вместимость: ")
                excursion.add_excursion(
                    excursions, title, date, place, capacity
                )
            case 2:
                query = utils.input_str("Поиск по названию: ")
                show_excursions(
                    excursion.find_excursion(excursions, query)
                )
            case 3:
                excursion_id = utils.input_int("ID экскурсии: ")
                min_capacity = utils.input_int("Мин. вместимость: ")
                if excursion.check_excursion_capacity(
                        excursions, excursion_id, min_capacity):
                    print("Вмещает")
                else:
                    print("Не вмещает")
            case 4:
                key = utils.input_str("Ключ сортировки: ")
                try:
                    show_excursions(
                        excursion.sort_excursions(excursions, key)
                    )
                except ValueError as error:
                    print(error)
            case 5:
                show_excursions(excursions)
            case 6:
                excursion_id = utils.input_int("ID экскурсии: ")
                excursion.remove_excursion(excursions, excursion_id)
            case 0:
                return
            case _:
                print("Ошибка! Неверное число.")


def menu_group(groups: list[dict[str, Any]]) -> None:
    """Меню работы с группами"""
    while True:
        print(
            "Меню групп\n"
            "   1. Добавить группу\n"
            "   2. Найти группу\n"
            "   3. Группы экскурсии\n"
            "   4. Проверить вместимость\n"
            "   5. Отсортировать группы\n"
            "   6. Вывести группы\n"
            "   7. Удалить группу\n"
            "   0. Выход"
        )
        mode = utils.input_int("Действие: ")
        match mode:
            case 1:
                excursion_id = utils.input_int("ID экскурсии: ")
                name = utils.input_str("Название группы: ")
                capacity = utils.input_int("Вместимость: ")
                group.add_group(groups, excursion_id, name, capacity)
            case 2:
                query = utils.input_str("Поиск по названию: ")
                show_groups(group.find_group(groups, query))
            case 3:
                excursion_id = utils.input_int("ID экскурсии: ")
                show_groups(
                    group.filter_groups_by_excursion(
                        groups, excursion_id
                    )
                )
            case 4:
                group_id = utils.input_int("ID группы: ")
                min_capacity = utils.input_int("Мин. вместимость: ")
                if group.check_group_capacity(
                        groups, group_id, min_capacity):
                    print("Вмещает")
                else:
                    print("Не вмещает")
            case 5:
                key = utils.input_str("Ключ сортировки: ")
                try:
                    show_groups(group.sort_groups(groups, key))
                except ValueError as error:
                    print(error)
            case 6:
                show_groups(groups)
            case 7:
                group_id = utils.input_int("ID группы: ")
                group.remove_group(groups, group_id)
            case 0:
                return
            case _:
                print("Ошибка! Неверное число.")


def menu_enrollment(
    enrollments: list[dict[str, Any]],
    groups: list[dict[str, Any]]
) -> None:
    """Меню работы с записями участников"""
    while True:
        print(
            "Меню записей\n"
            "   1. Записать участника\n"
            "   2. Проверить, записан ли\n"
            "   3. Показать записи участника\n"
            "   4. Показать записи группы\n"
            "   5. Отменить запись\n"
            "   6. Вывести все записи\n"
            "   0. Выход"
        )
        mode = utils.input_int("Действие: ")
        match mode:
            case 1:
                user_id = utils.input_int("ID участника: ")
                excursion_id = utils.input_int("ID экскурсии: ")
                group_id = utils.input_int("ID группы: ")

                if group.check_group_capacity(
                        groups, group_id, 1) is False:
                    print("Группа не найдена")
                    continue

                enrolled_count = enrollment.count_enrolled(
                    enrollments, group_id
                )
                for group_data in groups:
                    if group_data["id"] == group_id:
                        if enrolled_count >= group_data["capacity"]:
                            print("В группе нет свободных мест")
                            break
                else:
                    result = enrollment.enroll_user(
                        enrollments, user_id,
                        excursion_id, group_id
                    )
                    if result is None:
                        print("Участник уже записан "
                              "на эту экскурсию")
                    else:
                        print("Записан")
            case 2:
                user_id = utils.input_int("ID участника: ")
                excursion_id = utils.input_int("ID экскурсии: ")
                is_enrolled = enrollment.is_user_enrolled(
                    enrollments, user_id, excursion_id
                )
                print(
                    enrollment.get_enrollment_status(is_enrolled)
                )
            case 3:
                user_id = utils.input_int("ID участника: ")
                show_enrollments(
                    enrollment.find_enrollments_by_user(
                        enrollments, user_id
                    )
                )
            case 4:
                group_id = utils.input_int("ID группы: ")
                show_enrollments(
                    enrollment.find_enrollments_by_group(
                        enrollments, group_id
                    )
                )
                print(
                    f"Всего: "
                    f"{enrollment.count_enrolled(enrollments, group_id)}"
                )
            case 5:
                enrollment_id = utils.input_int("ID записи: ")
                enrollment.cancel_enrollment(
                    enrollments, enrollment_id
                )
            case 6:
                show_enrollments(enrollments)
            case 0:
                return
            case _:
                print("Ошибка! Неверное число.")


def menu(
    users: list[dict[str, Any]],
    excursions: list[dict[str, Any]],
    groups: list[dict[str, Any]],
    enrollments: list[dict[str, Any]]
) -> None:
    """Главное меню приложения"""
    while True:
        print(
            "Главное меню\n"
            "   1. Меню пользователей\n"
            "   2. Меню экскурсий\n"
            "   3. Меню групп\n"
            "   4. Меню записей\n"
            "   0. Выход"
        )
        mode = utils.input_int("Действие: ")
        match mode:
            case 1:
                menu_user(users)
            case 2:
                menu_excursion(excursions)
            case 3:
                menu_group(groups)
            case 4:
                menu_enrollment(enrollments, groups)
            case 0:
                return
            case _:
                print("Ошибка! Неверное число.")


def main() -> None:
    """Загрузить данные, запустить меню, сохранить данные"""
    users = storage.load_users("data/users.json")
    excursions = storage.load_excursions("data/excursions.json")
    groups = storage.load_groups("data/groups.json")
    enrollments = storage.load_enrollments("data/enrollments.json")

    menu(users, excursions, groups, enrollments)

    storage.save_users("data/users.json", users)
    storage.save_excursions("data/excursions.json", excursions)
    storage.save_groups("data/groups.json", groups)
    storage.save_enrollments("data/enrollments.json", enrollments)


if __name__ == "__main__":
    main()
