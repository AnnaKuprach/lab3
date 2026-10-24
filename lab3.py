

# Каталог 
products = {
    "Хліб": {"price": 25.50, "quantity": 10},
    "Молоко": {"price": 42.90, "quantity": 8},
    "Яблука": {"price": 35.00, "quantity": 15},
    "Сир": {"price": 120.75, "quantity": 5},
    "Шоколад": {"price": 55.25, "quantity": 12}
}

# Кошик покупця
cart = {}

# Дані адміністратора
admin_login = "admin"
admin_password = "admin123"

# Функція форматування ціни за допомогою lambda
format_price = lambda price: f"{price:.2f} грн"


# Перегляд к
def show_catalog():
    print("\n=== КАТАЛОГ ТОВАРІВ ===")

    for name, info in products.items():
        print(
            name,
            "| Ціна:", format_price(info["price"]),
            "| Залишок:", info["quantity"]
        )


# Додавання 
def add_to_cart():
    show_catalog()

    name = input("\nВведіть назву товару: ").strip().capitalize()

    if name in products:
        if products[name]["quantity"] > 0:
            if name in cart:
                cart[name] = cart[name] + 1
            else:
                cart[name] = 1

            print("Товар додано до кошика!")
        else:
            print("Цього товару немає в наявності.")
    else:
        print("Такого товару немає в каталозі.")


# Перегляд 
def show_cart():
    print("\n=== ВАШ КОШИК ===")

    if len(cart) == 0:
        print("Кошик порожній.")
    else:
        total = 0

        for name, quantity in cart.items():
            price = products[name]["price"]
            item_total = price * quantity
            total = total + item_total

            print(
                name,
                "| Кількість:", quantity,
                "| Сума:", format_price(item_total)
            )

        print("Загальна сума:", format_price(total))


# Видалення товару з кошика
def remove_from_cart():
    show_cart()

    if len(cart) > 0:
        name = input("\nВведіть назву товару для видалення: ").strip().capitalize()

        if name in cart:
            cart[name] = cart[name] - 1

            if cart[name] == 0:
                del cart[name]

            print("Товар видалено з кошика.")
        else:
            print("Цього товару немає у кошику.")


# Покупка товарів
def buy_products():
    if len(cart) == 0:
        print("\nКошик порожній. Додайте товари перед покупкою.")
    else:
        show_cart()

        answer = input("\nПідтвердити покупку? (так/ні): ").strip().lower()

        if answer == "так":
            for name, quantity in cart.items():
                products[name]["quantity"] = products[name]["quantity"] - quantity

            cart.clear()

            print("Покупку успішно оформлено!")
        else:
            print("Покупку скасовано.")


# Вхід адміністратора
def admin_panel():
    login = input("Логін адміністратора: ").strip()
    password = input("Пароль адміністратора: ").strip()

    if login == admin_login and password == admin_password:
        print("\n=== ЗАЛИШКИ ТОВАРІВ ===")

        for name, info in products.items():
            print(
                name,
                "| Кількість:", info["quantity"],
                "| Ціна:", format_price(info["price"])
            )
    else:
        print("Неправильний логін або пароль!")


# Головне меню
while True:
    print("\n===== МІНІ-МАГАЗИН =====")
    print("1. Переглянути каталог")
    print("2. Додати товар у кошик")
    print("3. Переглянути кошик")
    print("4. Видалити товар з кошика")
    print("5. Купити товари")
    print("6. Вхід адміністратора")
    print("0. Вихід")

    choice = input("Оберіть дію: ").strip()

    if choice == "1":
        show_catalog()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        show_cart()
    elif choice == "4":
        remove_from_cart()
    elif choice == "5":
        buy_products()
    elif choice == "6":
        admin_panel()
    elif choice == "0":
        print("Дякуємо за покупку!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
