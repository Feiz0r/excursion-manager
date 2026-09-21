from datetime import date

group_name = "A"
capacity = 6
current_count = 4
excursion_date = date(2027, 1, 5)


def available(_capacity, _current_count):
    if _capacity > _current_count:
        return "Группа доступна для записи"
    return "Группа уже заполнена"


def enroll(_capacity, _current_count):
    if _capacity > _current_count:
        return _current_count + 1
    else:
        return _current_count


def available_count(_capacity, _current_count):
    return _capacity - _current_count


print(f"Группа: {group_name}")
print(f"Вместимость: {capacity} человек")
print(f"Записано: {current_count} человека")
print(f"Свободных мест: {available_count(capacity, current_count)}")
print(f"Дата: {excursion_date}")

print(available(capacity, current_count))

current_count = enroll(capacity, current_count)
print(f"После записи - записано: {current_count} человека")
print(f"Свободных мест: {available_count(capacity, current_count)}")