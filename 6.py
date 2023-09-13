while 1:
    sequence = input()
    my_list = sequence.split(',')
    a = 0
    for i in my_list:
        if not i.isdigit():
            print("Введит ЧИСЛОВУЮ последовательность")
            a += 1
            break
    if a == 0:
        print(f"Список: {my_list}")
        my_tuple = tuple(my_list)
        print(f"Кортеж: {my_tuple}")
        break
