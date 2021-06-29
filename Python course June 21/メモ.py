mylist = [1, 2]
mylist.remove(2)
print(mylist)

mydict = {1: 'apple', 2: 'orange', 3: 'banana'}
print(mydict)

myvalue = mydict[2]
print(myvalue)

print(3 in mydict.keys())

print('banana' in mydict.values())

mydict[0] = "peach"

print(mydict)

mydict[156] = mylist

print(mydict)

mydict.pop(2)

print(mydict)

sortedDict = sorted(mydict.items())

print(sortedDict)

mydict2 = dict(sortedDict)
print(mydict2)

test_str = 'hello, world!'
test_split = test_str.split('o')
print(test_split)

test_str = "http://192.168.1.1/version/api"
test_split = test_str.split('/', 1)
print(test_split)

text = 'name=Dima=User;age=28;'
if text == '':
    the_dict = {}
else:
    new_text = text.split(';')
    if '' in new_text:
        new_text.remove('')
    new_list = []
    for value in new_text:
        split_text = value.split('=', 1)
        new_list.append(split_text)
        the_dict = dict(new_list)
print(the_dict)


text = 'https://example.com/path/to/page?name=ferret&color=purple&'
the_mark = text.find('?')
new_text = text[the_mark + 1:]
if new_text == '' or '?' not in text:
    the_dict = {}
else:
    final_text = new_text.split('&')
    if '' in final_text:
        final_text.remove('')
    new_list = []
    for value in final_text:
        split_text = value.split('=', 1)
        new_list.append(split_text)
        the_dict = dict(new_list)
print(the_dict)





