import csv

def read_csv(filename: str) -> list:
    with open(filename, "r") as csv_file:
        data = []
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data):
    with open(filename, "w", newline="") as csv_file: # У меня windows поэтому: newline=""
        writer = csv.writer(csv_file)
        writer.writerows(data)

filename = "test_02.csv"
data = read_csv(filename)

data.append(["Andrey", 45, 10.0, "KNTEU"])
data[0].append("Text")
for row in data[1:]:
    row.append("test")

write_csv(filename, data)

