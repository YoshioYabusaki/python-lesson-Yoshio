####### homework 07-1) <<< Йосио

import random as rnd

my_list = []
num = 0
while num < 20:
    value = rnd.randint(1, 100)
    my_list.append(value)
    num = num + 1
print(my_list)



####### homework 07-2) <<< Йосио

def create_random_point():
    point = (rnd.randint(-10, 10),
             rnd.randint(-10, 10))
    return point
triangle = {"A": create_random_point(),
            "B": create_random_point(),
            "C": create_random_point()}
print(triangle)



####### homework 07-3) <<< Йосио

my_str = "have a cup of coffee"
def my_print(my_str):
       print("***" + my_str + "***")
my_print(my_str)



####### homework 07-4) <<< Йосио

Persons = [{"name": "Aki", "age": 20},
           {"name": "Hachiko", "age": 20},
           {"name": "Totoro", "age": 25},
           {"name": "Doraemon", "age": 45},
           {"name": "Ken", "age": 50}]

# 4-a)
age_list = [d["age"] for d in Persons]
age_set = set(age_list)
youngest_age = min(age_set)
for item in Persons:
    if item["age"] == youngest_age:
        print(item["name"])

# 4-б)
name_set = set([d["name"] for d in Persons])
longest = max(len(item) for item in name_set)
for who in Persons:
    if len(who["name"]) == longest:
        print(who["name"])

# 4-в)
ave = sum(age_list) / len(age_list)
print(ave)



####### homework 07-5) <<< Йосио

my_dict_1 = {"1.Guitar_brand": "Gibson",
             "2.model": "Les_poul",
             "3.year": 1972,
             "4.price": "USD3500",
             "5.shop": "YAMAHA_online"}
my_dict_2 = {"1.Guitar_brand": "Fender",
             "2.model": "Telecaster",
             "3.year": 1968,
             "4.owner": "Mr.Hancock",
             "5.status": "neck_repaired"}

# 5-a)
common_keys = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
print(common_keys)

# 5-б)
unique_keys = set(my_dict_1.keys()) - common_keys
print(unique_keys)

# 5-в)
new_dict = {key: value for key, value in my_dict_1.items() if key in unique_keys}
print(new_dict)

# 5-г)
new_dict = {}
new_dict.update(my_dict_1)
new_dict.update(my_dict_2)
for key in new_dict.keys():
    if key in common_keys:
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]
print(new_dict)