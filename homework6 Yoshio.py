####### homework 06-1) <<< Йосио

my_list = ['vocal', 'onaip', 'guitar', 'smurd', 'bass']
new_list = []
for index, value in enumerate(my_list):
    if index % 2:
        value = value[::-1]
    new_list.append(value)
print(new_list)


####### homework 06-2) <<< Йосио

my_list = ['microsoft', 'sony', 'nokia', 'samsung', 'apple', 'xiaomi', 'asus']
new_list = []
for value in my_list:
    if value[0] == 'a':
        new_list.append(value)
print(new_list)


####### homework 06-3) <<< Йосио

my_list = ['microsoft', 'sony', 'nokia', 'samsung', 'apple', 'xiaomi', 'asus']
new_list = []
for value in my_list:
    if 'a' in value:
        new_list.append(value)
print(new_list)


####### homework 06-4) <<< Йосио

my_list = ['sony', 200, 'apple', 150, 'asus', 100]
new_list = []
for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)


####### homework 06-5) <<< Йосио

my_str = 'telephone'
new_list = []
for value in my_str:
    if my_str.count(value) == 1:
        new_list.append(value)
print(new_list)


####### homework 06-6) <<< Йосио

my_str_1 = "telephone"
my_str_2 = "elephant"
new_list = []
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
result_set = my_set_1.intersection(my_set_2)
new_list.extend(result_set)
print(new_list)


####### homework 06-7) <<< Йосио

my_str_1 = "telephone"
my_str_2 = "elephant"
new_list = []
for value_1 in my_str_1:
    for value_2 in my_str_2:
        if my_str_1.count(value_1) == my_str_2.count(value_2) == 1 and value_1 == value_2:
            new_list.append(value_1)
print(new_list)


####### homework 06-8) <<< Йосио

Person = {"Фамилия": "Lennon",
          "Имя": "John",
          "Возраст": "81",
          "Проживание": {"Страна": "USA",
                         "Города": "NY",
                         "Улица": "1 W 72nd St"},
          "Работа": {"Наличие": "yes",
                     "Должность": "Chief Producer"}}
print(Person["Проживание"]["Улица"])


####### homework 06-9) <<< Йосио

good_cake = {"Составляющие":
                   {"Коржи": {"Мука": "200 г",
                              "Молоко": "50 мл",
                              "Масло": "10 г",
                              "Яйцо": "2 шт"},
                    "Крем": {"Сахар": "100 г",
                             "Масло": "100 г",
                             "Ваниль": "1 г",
                             "Сметана": "200 г"},
                    "Глазурь": {"Какао": "80 г",
                                "Сахар": "10 г",
                                "Масло": "10 г"}}}
print(good_cake["Составляющие"]["Крем"]["Сметана"])
