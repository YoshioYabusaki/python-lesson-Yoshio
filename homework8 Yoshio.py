####### homework 08-1) <<< Йосио

import string, random as rnd
from random import randint

def create_email(names, domains):
    return rnd.choice(names) + \
           "." + \
           str(rnd.randint(100, 999)) + \
           "@" + \
           "".join(rnd.choice(string.ascii_lowercase) for i in range(randint(5,7))) + \
           "." + \
           rnd.choice(domains)

names = ["Paul", "John", "Ringo", "George"]
domains = ["net", "com", "jp", "ua"]
e_mail = create_email(names, domains)
print(e_mail)


####### homework 08-2) <<< Йосио
print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")


def random_length(min_limit, max_limit):
    return "".join(rnd.choice(string.ascii_lowercase) for i in range(randint(min_limit, max_limit)))
result_str = random_length(60, 100)
print(result_str)


####### homework 08-3) <<< Йосио
print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")


def make_spaces(result_str): # добавление пробелов и символов
    my_list = list(result_str)
    num = 0
    while num < len(my_list):
        insert_point = randint(num + 1, num + 10)
        insert_variation = [" ",
                            ", ",
                            " " + str(rnd.randint(1, 999999)) + " "]
        value = rnd.choice(insert_variation)
        my_list.insert(insert_point, value)
        num = insert_point + 1
    result = "".join(my_list)
    return result

def the_first_word(goal_str):  # большая буква в начале текста
    Make_it_big = goal_str.capitalize()
    return Make_it_big
#
def modify_word(word, percentage=0.3): # случайная большая буква в тексте
    if rnd.random() < percentage:
        word = word.capitalize()
    return word

def modify_str(goal_str):
    goal_str_split = goal_str.split()
    result = []
    for word in goal_str_split:
        word = modify_word(word)
        result.append(word)
    return " ".join(result)
#
def period_and_change_line(goal_str): # точка в конце и переход на новую страку
    my_list = list(goal_str)
    if my_list[-1] == ",":
        my_list[-1] = "."
    else:
        my_list.append(".")

    num = 0
    while num < rnd.randint(1, 5):
        insert_point = rnd.randint(1, len(my_list) - 1)

        if my_list[insert_point] != " ":
            if my_list[insert_point] != ",":
                if my_list[insert_point] != ".":
                    my_list.insert(insert_point, "\n")
                    num = num + 1
    result = "".join(my_list)
    return result

goal_str = make_spaces(result_str)
goal_str = the_first_word(goal_str)
goal_str = modify_str(goal_str)
goal_str = period_and_change_line(goal_str)
print(goal_str)