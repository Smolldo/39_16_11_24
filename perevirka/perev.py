import hashlib
import re

users_db = {}
wallets = {}  # Храним кошельки пользователей отдельно

class WeakPasswordError(Exception):
    def __init__(self, message="Пароль не відповідає вимогам безпеки"):
        super().__init__(message)

currencies_info = {
    "UAH": {"description": "UAH (Українські гривні)", "rate": 1.0},
    "USD": {"description": "USD (Долар США)", "rate": 0.027},
    "EUR": {"description": "EUR (Євро)", "rate": 0.025},
    "GBP": {"description": "GBP (Фунт стерлінгів)", "rate": 0.022},
    "CNY": {"description": "CNY (Юані)", "rate": 0.19}
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Добрий день. Будь ласка, введіть ваше ім'я: ").strip()
    if username in users_db:
        print("Цей логін вже використовується. Оберіть інший.")
        return

    password = input("Придумайте пароль: ")
    if len(password) < 10:
        raise WeakPasswordError("Пароль має містити принаймні 10 символів")
    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Пароль має містити мінімум одну велику літеру")
    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Пароль має містити мінімум одну цифру")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise WeakPasswordError("Пароль має містити мінімум один спец. символ")

    users_db[username] = hash_password(password)
    wallets[username] = {code: 0.0 for code in currencies_info}  # Инициализируем пустой кошелек
    print(f"Ласкаво просимо, {username}!")

def authenticate_user():
    username = input("Введіть логін для входу: ").strip()
    password = input("Введіть пароль: ").strip()

    if username in users_db and users_db[username] == hash_password(password):
        print(f"Ласкаво просимо, {username}!")
        return username
    else:
        print("Невірний логін або пароль.")
        return None

def show_wallet(username):
    print(f"\nВаш поточний гаманець ({username}):")
    for code, balance in wallets[username].items():
        print(f"  {currencies_info[code]['description']}: {balance:.2f}")

def convert_currency(username):
    show_wallet(username)
    
    from_curr = input("Введіть валюту, з якої хочете конвертувати: ").strip().upper()
    to_curr = input("Введіть валюту, в яку хочете конвертувати: ").strip().upper()

    if from_curr not in currencies_info or to_curr not in currencies_info:
        print("Помилка: Введена невідома валюта!")
        return

    try:
        amount = float(input("Введіть суму для конвертації: "))
        if amount <= 0:
            print("Сума повинна бути більше нуля!")
            return
        if wallets[username][from_curr] < amount:
            print("Недостатньо коштів!")
            return
    except ValueError:
        print("Помилка: введіть правильне число!")
        return

    from_rate = currencies_info[from_curr]["rate"]
    to_rate = currencies_info[to_curr]["rate"]

    amount_in_uah = amount / from_rate
    converted_amount = amount_in_uah * to_rate

    wallets[username][from_curr] -= amount
    wallets[username][to_curr] += converted_amount

    print(f"Конвертовано {amount:.2f} {from_curr} у {converted_amount:.2f} {to_curr} для {username}.")
    transactions(username, f"Конвертував {amount:.2f} {from_curr} у {converted_amount:.2f} {to_curr}.")

def show_curr_desc():
    print("\nДоступні валюти:")
    for code, data in currencies_info.items():
        print(f"  {code}: {data['description']}")

def transactions(username, transaction):
    with open("transactions.txt", "a", encoding="utf-8") as file:
        file.write(f"{username}: {transaction}\n")


def add_money(username):
    show_curr_desc()

    currency = input("Введіть валюту для додавання: ").strip().upper()
    if currency not in currencies_info:
        print("Невідома валюта!")
        return

    try:
        amount = float(input("Введіть суму для додавання: "))
        if amount <= 0:
            print("Сума повинна бути більше нуля!")
            return
    except ValueError:
        print("Помилка: введіть правильне число!")
        return

    wallets[username][currency] += amount
    print(f"Додано {amount:.2f} {currency} до гаманця {username}.")
    transactions(username, f"Додав {amount:.2f} {currency}")

while True:
    action = input("\nОберіть дію: 1.Реєстрація 2. Вхід 3. Вихід: ").strip()

    if action == "1":
        register_user()
    elif action == "2":
        username = authenticate_user()
        if username:
            while True:
                print("\nЩо ви хочете зробити з вашим гаманцем?")
                print("1. Показати поточний гаманець")
                print("2. Додати гроші до гаманця")
                print("3. Конвертувати гроші")
                print("4. Показати доступні валюти")
                print("5. Вийти з гаманця")

                choice = input("Виберіть опцію: ").strip()

                if choice == "1":
                    show_wallet(username)
                elif choice == "2":
                    add_money(username)
                elif choice == "3":
                    convert_currency(username)
                elif choice == "4":
                    show_curr_desc()
                elif choice == "5":
                    print(f"До побачення, {username}!")
                    transactions(username, "Вийшов з гаманця")
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")
    elif action == "3":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
