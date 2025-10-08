
mass = float(input("Масса в кг: "))
height = float(input("Высота в метрах: "))
gravity = float(input("Ускорение свободного падения (м/с²): "))
energy = mass * gravity * height

print("Потенциальная энергия:", energy, "Дж")