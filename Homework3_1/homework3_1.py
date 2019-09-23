import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
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


def take_token():
    URL = 'https://oauth.yandex.ru/token'
    print('Для записи на ваш Yandex Disk необходимо предоставить доступ:')
    print('Перейдите по ссылке https://oauth.yandex.ru/authorize?response_type=code&client_id=f49521549fa840b3bdb30d5a139df49c')
    user_code = input('И введите полученный код: ')

    data = {
        'grant_type': 'authorization_code',
        'code': user_code,
        'client_id': 'f49521549fa840b3bdb30d5a139df49c',
        'client_secret': '178fe59134b3485c990ee94cf55297ac',
    }

    resp = requests.post(URL, data=data)
    token = resp.json()['access_token']
    return token


# получаем ссылку загрузчика Yandex Disk
def uploader(full_path):
    token = take_token()
    params = {
        'path': full_path
    }
    headers = {
        'Authorization': 'OAuth {}'.format(token),
        'Content-Type': 'application/json'

    }
    take_link = requests.get(GET_URL, headers=headers, params=params)
    uploader_link = take_link.json()['href']
    # print(uploader_link)

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

# запись в файл, отправка на диск и удаление с локального диска
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(result)
        requests.put(link, data=result.encode('utf-8'))
    os.remove(file_name)

    print(f'/nФайл {file_name} записан на ваш Yandex Disk')


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


