####### homework 05-1) <<< Йосио

my_int = 3208925123890112301
my_value = str(my_int)
result = my_value.count("0")
print(result)


####### homework 05-2) <<< Йосио

my_int = 320890251238901123000
my_value = str(my_int)
new_str = my_value[::-1]
if new_str[0] != "0":
    print("Нет нуля в конце этого числа :-)")
else:
    num = 0
    while new_str[num] == "0":
        num = num + 1
    print(new_str.count("0", 0, num))


####### homework 05-3a) <<< Йосио

my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [100, 200, 300, 400, 500]
my_result = []
my_result.extend(my_list_1[::2] + my_list_2[1::2])
print(my_result)


####### homework 05-3b) <<< Йосио

my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = [101, 202, 303, 404, 505]
my_result = []
for n1 in my_list_1:
    if n1 % 2 == 0:
        my_result.append(n1)
for n2 in my_list_2:
    if n2 % 2 != 0:
        my_result.append(n2)
print(my_result)


####### homework 05-4) <<< Йосио

my_list = [111, 555, 444, 333, 222]
new_list = []
new_list.extend(my_list[1:])
new_list.append(my_list[0])
print(new_list)


####### homework 05-5) <<< Йосио

my_list = [11, 55, 44, 33, 22]
value = my_list.pop(0)
my_list.append(value)
print(my_list)


####### homework 05-6) <<< Йосио

my_str = "14 плюс 6 равно 20"
my_list = []
Split_List = my_str.split(" ")
for symbol in Split_List:
    if symbol.isdigit():
        symbol = int(symbol)
        my_list.append(symbol)
print(sum(my_list))


####### homework 05-7) <<< Йосио

my_str = "qwertyn"
my_str = list(my_str)
my_list = []
if len(my_str) % 2 != 0:
    my_str.append('_')
for index, symbol in enumerate(my_str):
    if index % 2 == 0:
        my_list.append(my_str[index] + my_str[index + 1])
print(my_list)


####### homework 05-8) <<< Йосио

my_str = "my_guitar"
l_limit = "y"
r_limit = "a"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]
print(sub_str)


####### homework 05-9) <<< Йосио

my_str = "their_guitars"
l_limit = "h"
r_limit = "r"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)


####### homework 05-10) <<< Йосио

my_list = [2,4,1,5,3,9,0,7]
new_list = []
for index, my_int in enumerate(my_list):
    if my_int in my_list[1:-1] and my_int > my_list[index - 1] + my_list[index + 1]:
        new_list.append(my_int)
print(len(new_list))

