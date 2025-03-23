# База даних (зберігається в оперативній пам’яті)
users = {}

# === Реєстрація ===
def register():
    username = input("Введіть логін: ")
    if username in users:
        print("❌ Користувач вже існує!")
        return None

    password = input("Введіть пароль: ")
    users[username] = {"password": password, "transactions": []}
    print("✅ Реєстрація успішна!")
    return username

# === Вхід ===
def login():
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if username in users and users[username]["password"] == password:
        print("✅ Вхід успішний!")
        return username
    else:
        print("❌ Невірний логін або пароль.")
        return None

# === Додавання транзакції ===
def add_transaction(user):
    amount = float(input("Сума: "))
    category = input("Категорія (доходи/витрати): ").lower()
    
    transaction = {"amount": amount, "category": category}
    users[user]["transactions"].append(transaction)
    print("✅ Транзакція додана!")

# === Перегляд транзакцій ===
def show_report(user):
    transactions = users[user]["transactions"]
    if not transactions:
        print("📭 Немає транзакцій.")
        return

    print("\n📊 Ваші транзакції:")
    for t in transactions:
        print(f"{t['category'].capitalize()}: {t['amount']} грн")

# === Головна програма ===
def main():
    print("💰 Система фінансів")

    user = None
    while not user:
        action = input("Реєстрація (r) / Вхід (l): ").lower()
        if action == "r":
            user = register()
        elif action == "l":
            user = login()

    while True:
        print("\n📌 Меню:")
        print("1. Додати транзакцію")
        print("2. Показати звіт")
        print("3. Вийти")

        choice = input("Ваш вибір: ")
        if choice == "1":
            add_transaction(user)
        elif choice == "2":
            show_report(user)
        elif choice == "3":
            print("👋 До побачення!")
            break
        else:
            print("❌ Невірний вибір.")

if __name__ == "__main__":
    main()
