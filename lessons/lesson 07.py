ascii_table = {number: chr(number) for number in range(ord("a"), ord("z") + 1)}
print(ascii_table)

key = '100'
# if key in ascii_table: # in 鍵があるかどうか確かめる
#     print(ascii_table[key])

result = ascii_table.get[key]

print(ascii_table.get(key))