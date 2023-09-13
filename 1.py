seconds = 1
minutes = 0
hours = 0
days = 0
print("\n")
while seconds != 0:
    seconds = str(input("Введите число секунд\n"))
    if seconds.isdigit():
        seconds = int(seconds)
        days = seconds // 86400
        hours = seconds // 3600 - days * 24
        minutes = seconds // 60 - hours * 60 - days * 24 * 60
        seconds = seconds - minutes * 60 - hours * 3600 - days * 24 * 3600
        print(f"{days}:{hours}:{minutes}:{seconds}")
    else:
        print("Неккоректные данные")
else:
    print("Работа завершена")