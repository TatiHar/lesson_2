#задание №1
my_list = [14, 5.3, "he", 5698, None, -9]
for el in range(len(my_list)):
        print(type(my_list[el]))

#задание №2
my_list = input("Введите элементы списка: ").split()
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)

#задание №3
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print('Error')

#задание №4
text = input("Введите текст:")
line = []
i = 1
for el in range(text.count(' ') + 1):
    line = text.split()
    if len(str(line)) <= 10:
        print(f" {i} {line [el]}")
        i += 1
    else:
        print(f" {i} {line [el] [0:10]}")
        i += 1

#задание №5
num = int(input("Введите номер: "))
my_list = [7, 4, 3, 2]
i = my_list.count(num)
for el in my_list:
    if i > 0:
        a = my_list.index(num)
        my_list.insert(a+i, num)
        break
    else:
        if num > el:
            b = my_list.index(el)
            my_list.insert(b, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)

