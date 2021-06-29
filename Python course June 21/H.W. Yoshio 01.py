def parse(text) -> dict:
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
    return the_dict

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(text) -> dict:
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
    return the_dict

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}