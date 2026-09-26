from datetime import date


def input_int(prompt: str) -> int:
    """Запросить целое число"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите целое число.")


def input_date(prompt: str) -> date:
    """Запросить дату"""
    while True:
        try:
            return date.fromisoformat(input(prompt))
        except ValueError:
            print("Ошибка! Формат даты: ГГГГ-ММ-ДД.")


def input_str(prompt: str) -> str:
    """Запросить непустую строку"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка! Строка не может быть пустой.")
