while 1:
    n = input("Введите число элементов\n")
    if not n.isdigit():
        print("Некоректное значение")
    else:
        n = int(n)
        break
i = 0
cube = []
while i < n:
    element = input(f"Введите {i+1} элемент\n")
    if element.isdigit():
        element = int(element)
        cube.append(element ** 3)
        i += 1
    else:
        print("Некоректное значение")
print("Список: ", cube)
