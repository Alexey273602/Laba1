my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for i in range(3):
    print(f"Ключ с топ-{i + 1} значением: {max(my_dict, key=my_dict.get)}")
    for j in my_dict:
        if j == max(my_dict, key=my_dict.get):
            my_dict.pop(j)
            break
