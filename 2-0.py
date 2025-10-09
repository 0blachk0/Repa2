import os

def main():
    while True:
        print("\nВыбор задачи:")
        print("1 - Скорость")
        print("2 - Масса") 
        print("3 - Температура")
        print("4 - Работа")
        print("5 - Кинетическая энергия")
        print("6 - Потенциальная энергия")
        print("7 - Давление")
        print("8 - Теплота")
        print("9 - Частота")
        print("10 - Объем цилиндра")
        print("q - Выход")
        
        choice = input("Выберите задачу (1-10 или q): ")
        
        if choice == 'q':
            print("Выход")
            break
        elif choice in ['1','2','3','4','5','6','7','8','9','10']:
            os.system(f'python 2-{choice}.py')
            input("Нажмите Enter чтобы продолжить...")
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()