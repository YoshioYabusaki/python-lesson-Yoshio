####### homework 04-1) <<< Йосио

my_list = [1, 10, 100, 1000, 2, 21, 211, 2111]
for value in my_list:
    if value > 100:
        print(value)


####### homework 04-2) <<< Йосио

my_list = [1, 10, 100, 1000, 2, 21, 211, 2111]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)


####### homework 04-3) <<< Йосио

my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)


####### homework 04-4) <<< Йосио
# не было задачи :-)


####### homework 04-5) <<< Йосио

my_list = ["red", "blue", "yellow", "green", "white"]
my_indexes = [0, 1, 2, 3, 4]
for index in my_indexes:
    print(my_list[index])


####### homework 04-6) <<< Йосио

my_list_1 = ["red", "blue", "yellow", "green", "white"]
my_list_2 = ["A", "B", "C", "D", "E"]
my_indexes = [0, 1, 2, 3, 4]
for index in my_indexes:
    print((my_list_1[index], my_list_2[index]))


####### homework 04-7) <<< Йосио

my_string = '0123456789'
list = []
for symb_1 in my_string:
    for symb_2 in my_string:
        list.append(int(symb_1 + symb_2))
print(list)