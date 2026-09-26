from user import add_user, find_user, remove_user


def test_add_user() -> None:
    users = []
    add_user(users, "Иван", 20, "+7-000")
    assert len(users) == 1


def test_find_user() -> None:
    users = []
    add_user(users, "Иван Иванов", 20, "+7-000")
    result = find_user(users, "иван")
    assert len(result) == 1


def test_remove_user() -> None:
    users = []
    add_user(users, "Иван", 20, "+7-000")
    assert remove_user(users, 1) is True
    assert len(users) == 0
