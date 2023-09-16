from settings import CURRENCIES


def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURRENCIES[current_currency]
    to_value = currencies.get(to_currency)
    coefficient = to_value / from_value
    return round(amount * coefficient, 2)


print("Добро пожаловать в конвертатор валют!")

print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

print("Доступные валюты:")

for key in CURRENCIES:
    print(f'* {key}')

current_currency = input("Введите исходную валюту: ")
if current_currency not in CURRENCIES:
    current_currency = input("Вы ввели недоступную валюту. Попробуйте еще раз: ")

result_currency = input("Введите результирующую валюту: ")
if result_currency not in CURRENCIES:
    current_currency = input("Вы ввели недоступную валюту. Попробуйте еще раз: ")

amount = input("Введите количество: ")
if not amount.isnumeric():
    amount = input("Можно вводить только числа. Введите количество: ")

result = convert(float(amount), current_currency, result_currency, CURRENCIES)

print(f'{amount} {current_currency} = {result} {result_currency}')
