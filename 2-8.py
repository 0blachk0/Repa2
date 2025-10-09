mass = float(input("Масса в кг: "))
heat_capacity = float(input("Удельная теплоёмкость: "))
delta_temp = float(input("Изменение температуры в °C: "))
heat = mass * heat_capacity * delta_temp

print("Количество теплоты:", heat, "Дж")