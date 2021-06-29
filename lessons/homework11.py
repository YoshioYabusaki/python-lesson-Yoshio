####### homework 11-1) <<< Йосио
import json
import re

def read_file(file_name):
    with open(file_name, "r") as json_file:
        contents = json_file.read()
        return eval(contents)

file_name = "data.json"
print(read_file(file_name))


####### homework 11-2) <<< Йосио

def sort_key_by_name(sort_dict):
    value = sort_dict.get("name")
    last_element = value.split()[-1]
    return last_element

result = sorted(read_file(file_name), key=sort_key_by_name)
print(result)


####### homework 11-3) <<< Йосио

def sort_key_by_death_year(sort_dict):
    the_life = sort_dict["years"]
    numbers = re.findall(r'\d+', the_life)
    if "BC" in the_life:
        numbers[1] = int(numbers[1]) * -1
    return int(numbers[1])

result = sorted(read_file(file_name), key=sort_key_by_death_year)
print(result)


####### homework 11-4) <<< Йосио

def length_of_text(sort_dict):
    the_text = sort_dict["text"]
    return len(the_text.split())

result = sorted(read_file(file_name), key=length_of_text)
print(result)