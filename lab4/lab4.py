class Laptop:
    def __init__(self, cpu_ghz=0.0, ram_gb=0, brand="Невідомо", price=0.0, color="Чорний"):
        # Приватні поля (згідно з таблицею)
        self.__cpu_ghz = float(cpu_ghz)
        self.__ram_gb = int(ram_gb)
        self.__brand = str(brand)

        # Публічні поля: числове (price) та стрічкове (color)
        self.price = float(price)
        self.color = str(color)

    # --- Методи доступу (гетери та сетери) для приватних полів ---

    def get_cpu_ghz(self):
        return self.__cpu_ghz

    def set_cpu_ghz(self, cpu_ghz):
        self.__cpu_ghz = float(cpu_ghz)

    def get_ram_gb(self):
        return self.__ram_gb

    def set_ram_gb(self, ram_gb):
        self.__ram_gb = int(ram_gb)

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = str(brand)

    # --- Перевизначення методів __str__ та __repr__ ---

    def __str__(self):
        return (f"Ноутбук: {self.__brand} | CPU: {self.__cpu_ghz} GHz | "
                f"RAM: {self.__ram_gb} GB | Колір: {self.color} | Ціна: ${self.price}")

    def __repr__(self):
        return (f"Laptop(cpu_ghz={self.__cpu_ghz}, ram_gb={self.__ram_gb}, "
                f"brand='{self.__brand}', price={self.price}, color='{self.color}')")

    # --- Деструктор ---

    def __del__(self):
        print(f"Об'єкт ноутбука '{self.__brand}' успішно видалено з пам'яті.")


def main():
    # 1. Об'єкт з параметрами за замовчуванням
    laptop1 = Laptop()

    # 2. Об'єкт з повною передачею параметрів
    laptop2 = Laptop(
        cpu_ghz=3.2,
        ram_gb=16,
        brand="Apple",
        price=1299.99,
        color="Space Gray"
    )

    # 3. Ще один об'єкт з параметрами
    laptop3 = Laptop(
        cpu_ghz=4.5,
        ram_gb=32,
        brand="Lenovo",
        price=1450.00,
        color="Black"
    )

    laptops = [laptop1, laptop2, laptop3]

    print("=== Список створених ноутбуків ===")
    for index, laptop in enumerate(laptops, start=1):
        print(f"\n--- Ноутбук #{index} ---")
        # Виведення через методи доступу та публічні поля
        print(f"Виробник: {laptop.get_brand()}")
        print(f"Частота CPU: {laptop.get_cpu_ghz()} GHz")
        print(f"Об'єм RAM: {laptop.get_ram_gb()} GB")
        print(f"Колір (публічне): {laptop.color}")
        print(f"Ціна (публічне): ${laptop.price}")

        # Демонстрація роботи __str__
        print(f"Опис (__str__): {laptop}")

    print("\n=== Завершення роботи програми ===")


if __name__ == "__main__":
    main()
