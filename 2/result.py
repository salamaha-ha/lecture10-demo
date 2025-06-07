def validate_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("Входные данные должны быть словарём.")

    try:
        name = data['name']
        if not isinstance(name, str):
            raise ValueError("Имя пользователя должно быть строкой.")
    except KeyError as e:
        raise ValueError("Ключ 'name' отсутствует в словаре.") from e

    try:
        age = data['age']
        if not (isinstance(age, int) and age > 0):
            raise ValueError("Возраст должен быть положительным числом.")
    except KeyError as e:
        raise ValueError("Ключ 'age' отсутствует в словаре.") from e

    print("Валидация пройдена успешно!", data)
    return True

# Проверки:
print("--- Корректные данные ---")
validate_user_input({"name": "Alice", "age": 30})

print("\n--- Нет ключа 'name' ---")
try:
    validate_user_input({"age": 30})
except Exception as e:
    print(e)

print("\n--- Некорректный age (строка) ---")
try:
    validate_user_input({"name": "Bob", "age": "десять"})
except Exception as e:
    print(e)

print("\n--- Некорректный age (отрицательный) ---")
try:
    validate_user_input({"name": "Bob", "age": -5})
except Exception as e:
    print(e)

print("\n--- Некорректный тип входных данных (строка) ---")
try:
    validate_user_input("not a dict")
except Exception as e:
    print(e)
