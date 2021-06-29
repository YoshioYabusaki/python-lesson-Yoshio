# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)

# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
import requests
import json
import csv

def how_many_quotations(the_order):

    for number in range(the_order):
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": number,
                  "lang": "ru"}
        responce = requests.get(url, params=params)
        the_data = responce.json()

        the_data.pop('senderName')
        the_data.pop('senderLink')
        the_data['Author'] = the_data['quoteAuthor']
        del the_data['quoteAuthor']
        the_data['Quote'] = the_data['quoteText']
        del the_data['quoteText']
        the_data['URL'] = the_data['quoteLink']
        del the_data['quoteLink']
        if the_data['Author'] != "":
            return the_data

read_quote = how_many_quotations(5)
print(read_quote)

def write_file(file_path, the_data):
    with open(file_path, "w", newline='') as the_file:
        writer = csv.DictWriter(the_file, fieldnames=['Author', 'Quote', 'URL'])
        writer.writeheader()
        writer.writerow(the_data)

write_file("Homework12_file.csv", read_quote)


# def get_quote(the_url):
#     params = {"method": "getQuote",
#               "format": "json",
#               "key": 1,
#               "lang": "ru"}
#     responce = requests.get(the_url, params=params)
#     the_data = responce.json()
#     return the_data
#
# the_url = "http://api.forismatic.com/api/1.0/"
# the_quote = get_quote(the_url)
# print(the_quote)
#
# how_many = 5
# the_goal = []
# num = 0
# while num < how_many:
#     the_goal.append(the_quote)
#     num = num + 1
# print(the_goal)



# def how_many_quotations(the_order):
#
#     for number in range(the_order):
#
#
#         the_data.pop('senderName')
#         the_data.pop('senderLink')
#         the_data['Author'] = the_data['quoteAuthor']
#         del the_data['quoteAuthor']
#         the_data['Quote'] = the_data['quoteText']
#         del the_data['quoteText']
#         the_data['URL'] = the_data['quoteLink']
#         del the_data['quoteLink']
#         if the_data['Author'] != "":
#             return the_data

# read_quote = how_many_quotations(5)
# print(read_quote)

# def write_file(file_path, the_goal):
#     with open(file_path, "w", newline='') as the_file:
#         writer = csv.DictWriter(the_file, fieldnames=['Author', 'Quote', 'URL'])
#         writer.writeheader()
#         writer.writerow(the_goal)
#
# write_file("Homework12_file.csv", the_goal)


# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.


# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]


# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.
