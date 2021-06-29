import csv
import json

####### homework 10-1) <<< Йосио

def read_file(file_path):
    if file_path.endswith(".json"):
        with open(file_path, "r") as json_file:
            contents = json_file.read()
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding='UTF-8') as txt_file:  # у меня windows поэтому пишу "encoding"
            contents = txt_file.read()
    elif file_path.endswith(".csv"):
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            contents = []
            for row in reader:
                contents.append(row)
    else:
        contents = "Unsupported file format"
    return contents

file_path = "New_Homework_json.json" # <---Выбор файла
print(read_file(file_path))



####### homework 10-2) <<< Йосио

txt_data = "Сейчас мы с женой думаем что заказать. Я хочу наполеон, а жена хочет вафельный торт."
csv_data = {'Name':'Eric', 'Age':17, 'Value':123.79, 'Univ':'KNTEU'}, \
           {'Name':'Jef', 'Age':19, 'Value':321.46, 'Univ':'KNLU'}, \
           {'Name':'John', 'Age':21, 'Value':987.51, 'Univ':'Tokyo'}
json_data = {"Ukraine": 111222333000,
             "USA": 444555666000,
             'Japan': 777888999000}
str_data = 'You will find your guitar.'

the_data = csv_data  # <---Выбор данных

if the_data == txt_data:
    file_path = "New_Homework_txt.txt"
elif the_data == csv_data:
    file_path = "New_Homework_csv.csv"
elif the_data == json_data:
    file_path = "New_Homework_json.json"
else:
    file_path = "unsupported_file"
    print("Unsupported file format")

def write_file (file_path, the_data):
    if file_path.endswith(".txt"):
        with open(file_path, "w", encoding='UTF-8') as the_file:
            the_file.writelines(the_data)
    elif file_path.endswith(".csv"):
        with open(file_path, "w", newline='') as the_file:
            writer = csv.DictWriter(the_file, fieldnames=['Name', 'Age', 'Value', 'Univ'])
            writer.writeheader()
            writer.writerows(the_data)
    else:
        with open(file_path, "w") as the_file:
            json.dump(the_data, the_file, indent=4)

write_file(file_path, the_data)