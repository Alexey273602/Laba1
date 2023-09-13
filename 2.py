string = input()
for i in string:
    print(ord(i))
string_array = string.split()
max = len(string_array[0])
j = 0
for i in string_array:
    if len(i) > max:
        max = len(i)
        j = i
print(j)