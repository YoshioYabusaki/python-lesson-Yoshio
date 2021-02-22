import os
import string
import json
from random import randint, choice, choices, uniform

####### homework 09-1) <<< Йосио

def read_txt(file_path):
    with open(file_path, "r") as txt_file:
        data = []
        for line in txt_file.readlines():
            data.append(line.split())
    return data

path = "homework Yoshio"
the_txt = read_txt(r"C:\Users\yoshio\PycharmProjects\python-lesson-Yoshio\homework Yoshio\names.txt")

the_name_list = []
for item in the_txt:
    the_name_list.append(item[1])
print(the_name_list)



####### homework 09-2) <<< Йосио

def a_good_dict(num_keys):
    num = 0
    new_dict = {}
    while num < num_keys:
        key = "".join(choice(string.ascii_lowercase) for i in range(5))
        value = choices(['a', 'b', 'c'])
        my_dict = {key: value}

        for index in my_dict:
            if value == ['a']:
                my_dict[index] = randint(-100, 100)
            elif value == ['b']:
                my_dict[index] = uniform(0, 1)
            else:
                my_dict[index] = bool(randint(0, 1))
            new_dict.update(my_dict)
            num = num + 1
    return new_dict

print(a_good_dict(randint(5, 20)))



####### homework 09-3) <<< Йосио

result = a_good_dict(randint(5, 20))

def generate_and_write_json(file_path):
    with open(file_path, "w") as js_file:
        json.dump(result, js_file, indent=2)

file_path = "Homework_json.json"
generate_and_write_json(file_path)




