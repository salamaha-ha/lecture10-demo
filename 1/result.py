def convert_to_int(value):
    try:
        result = int(value)
        print(f"Преобразование успешно: {result}")
        return result
    except ValueError:
        print(f"Ошибка: '{value}' невозможно преобразовать в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Завершение попытки преобразования.")

# Проверка:
print("--- Проверка: корректная строка ---")
convert_to_int("123")

print("\n--- Проверка: некорректная строка ---")
convert_to_int("abc")

print("\n--- Проверка: другой тип данных (список) ---")
convert_to_int([1, 2, 3])