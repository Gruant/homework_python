import json
from collections import Counter
import xml.etree.ElementTree as ET
from pprint import pprint

def take_data_json(data):
    str_list = ''
    for data_str in data['rss']['channel']['items']:
        str_list += data_str['description'].lower()
    return take_list(str_list)

def take_data_xml(root):
    str_list = ''
    xml_data = root.findall('channel/item/description')
    for xml_str in xml_data:
        str_list += xml_str.text
    return take_list(str_list)

#использую новый список, т.к. при использовании remove или del данные выводятся неверно
def check_len(some_list):
    new_list = []
    for index, word in enumerate(some_list):
        if len(word) > 6:
            new_list.append(word)
    return new_list

def take_list(str_list):
    new_list = str_list.split(' ')
    return check_len(new_list)


def json_top():
    with open('newsafr.json', encoding='utf-8') as data:
        json_data = json.load(data)
        top_dict = Counter(take_data_json(json_data)).most_common(10)
    return top_dict

def xml_top():
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    top_dict = Counter(take_data_xml(root)).most_common(10)
    return top_dict


def main():
    command = str(input('Введите расширение файла который читаем (json / xml): '))
    if command == 'json':
        for i, top in enumerate(json_top()):
            print('{} место: {} - {} повторений'.format(i+1, top[0], top[1]))
    elif command == 'xml':
        for i, top in enumerate(xml_top()):
            print('{} место: {} - {} повторений'.format(i + 1, top[0], top[1]))
    else:
        print('Неверное расширение')


if __name__ == '__main__':
    main()