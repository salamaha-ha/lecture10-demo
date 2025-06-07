class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным!"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"NegativeNumberError: {self.message} Получено значение: {self.value}"

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num, "Ошибка: получено отрицательное число.")
    print(f"Число {num} — положительное!")
    return True

# Проверки:
print("--- Отрицательное число ---")
try:
    check_positive_number(-7)
except NegativeNumberError as e:
    print(e)

print("\n--- Положительное число ---")
try:
    check_positive_number(10)
except NegativeNumberError as e:
    print(e)
