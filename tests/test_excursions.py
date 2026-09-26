from excursion import (
    add_excursion,
    check_excursion_capacity,
    find_excursion,
)


def test_add_excursion() -> None:
    excursions = []
    add_excursion(excursions, "Музей", "2026-10-15", "Центр", 30)
    assert len(excursions) == 1


def test_find_excursion() -> None:
    excursions = []
    add_excursion(excursions, "Музей", "2026-10-15", "Центр", 30)
    assert len(find_excursion(excursions, "музей")) == 1


def test_check_excursion_capacity() -> None:
    excursions = []
    add_excursion(excursions, "Музей", "2026-10-15", "Центр", 30)
    assert check_excursion_capacity(excursions, 1, 20) is True
    assert check_excursion_capacity(excursions, 1, 50) is False
    assert check_excursion_capacity(excursions, 99, 10) is False
