from datetime import datetime, timedelta

# Получение текущей даты и времени
current_datetime = datetime.now()

# Добавление 2 часов
new_datetime = current_datetime + timedelta(hours=2)

# Вывод результата
print("Текущая дата и время:", current_datetime)
print("Дата и время через 2 часа:", new_datetime)