import requests
from urllib.parse import urlencode


def get_user_access():
    URL = 'https://oauth.vk.com/authorize'
    params = {
        'client_id': '7148260',
        'response_type': 'token',
        'display': 'page',
        'scope': 'friends',
        'v': '5.101',
    }
    print('?'.join((URL, urlencode(params))))
    TOKEN = input('Введите токен из ссылки редиректа: ')
    return TOKEN


TOKEN = get_user_access()


class User():
    first_name = ''
    last_name = ''
    # id может быть число или имя (далее мы будем всегда получать числовой id, чтобы получать список друзей.
    id = ''
    link = 'https://vk.com/'
    is_closed = bool
    class_list = []

    def __init__(self, id):
        self.id = id
        params = {
            'v': '5.101',
            'access_token': TOKEN,
            'user_ids': self.id,
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params).json()
        self.is_closed = response['response'][0]['is_closed']
        self.first_name = response['response'][0]['first_name']
        self.last_name = response['response'][0]['last_name']
        self.id = response['response'][0]['id']
        self.link += response['response'][0]['domain']

    def __str__(self):
        return '{} - {} {}'.format(self.link, self.first_name, self.last_name)

    def __and__(self, other):
        if not self.is_closed:
            params = {
                'v': '5.101',
                'access_token': TOKEN,
                'source_uid': self.id,
                'target_uid': other.id,
            }
            response = requests.get('https://api.vk.com/method/friends.getMutual', params=params).json()
            friends_list = response['response']
            newlist = []
            for i in friends_list:
                newlist.append(User(i))
            return newlist
        else:
            return None


def main():
    user1, user2 = input('Введите id 2-х пользователей и комманду в виде аперанда(без пробелов): ').split('&')
    # get_user_access()
    user1 = User(user1)
    user2 = User(user2)
    ids_list = user1 & user2
    if len(ids_list) == 0:
        print('Общих друзей нет')
    else:
        print(f'Кол-во общих друзей: {len(ids_list)}')
        for i in ids_list:
            print(str(i))


if __name__ == '__main__':
    main()
