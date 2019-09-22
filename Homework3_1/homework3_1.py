import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
TOKEN = 'AgAAAAAAoNqMAAXiBqI7Lom3qkx4t-ZOPGTAuBI'
GET_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_file, to_file, tran_in, tran_out='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    text = ''
    with open(from_file, mode='r', encoding='utf-8') as file:
        for line in file:
            text += line


    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(tran_in, tran_out),
        'option': 1
    }

    response = requests.get(URL, params=params)
    json = response.json()
    result = ''.join(json['text'])

    file_name = f'result_from_{tran_in}_to_{tran_out}.txt'
    full_path = os.path.join(to_file, file_name)

    with open(full_path, mode='w') as f:
        f.write(result)

    print(f'Перевод записан в {full_path}')

#получаем ссылку загрузчика Yandex Disk
def uploader(full_path):
    params = {
        'path': full_path
    }
    headers = {
        'Authorization': 'OAuth {}'.format(TOKEN),
        'Content-Type': 'application/json'

    }
    take_link = requests.get(GET_URL, headers=headers, params=params)
    link_json = take_link.json()
    uploader_link = link_json['href']

    return uploader_link

def translate_it_yadisk(from_file, tran_in, tran_out='ru'):
    text = ''
    with open(from_file, mode='r') as file:
        for line in file:
            text += line


    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(tran_in, tran_out),
        'option': 1
    }

    response = requests.get(URL, params=params)
    json = response.json()
    result = ''.join(json['text'])
    file_name = f'result_from_{tran_in}_to_{tran_out}.txt'
    link = uploader(file_name)

#запись в файл, отправка на диск и удаление с локального диска
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(result)
        requests.put(link, data=result.encode('utf-8'))
    os.remove(file_name)



if __name__ == '__main__':
    command = input('Какую задачу выполняем 1 или 2: ')
    if command == '1':
        from_file_path = input('Введите путь к файлу, который переводим: ')
        to_file_path = input('В какую папку записать результат: ')
        if os.path.exists(to_file_path):
            tran_in = input('С какого языка переводим (например en): ').lower()
            tran_out = input('На какой язык переводим: ').lower()
            translate_it(from_file_path, to_file_path, tran_in, tran_out)
        else:
            print('Такой папки не существует')
    elif command == '2':
        from_file_path = input('Введите путь к файлу, который переводим: ')
        tran_in = input('С какого языка переводим (например en): ').lower()
        tran_out = input('На какой язык переводим (по умолчанию ru): ').lower()
        translate_it_yadisk(from_file_path, tran_in, tran_out)
        print('Спасибо, файл записался на мой аккаунт, только к нему у меня есть токен')

