import requests
from urllib.parse import urlencode

TOKEN =  '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

class User():
    id = ''

    def __init__(self, id):
        params = {
            'v': '5.;/l.101',
            'access_token': TOKEN,
            'user_ids': self.id,
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params).json()
        self.id = response['response'][0]['id']
#запрос списка друзей
#запрос групп
#получение id участников групп
#сравнение Id участников групп и списка друзей
    # если нет совпадений, записываем в группу Json

    # def do_request (self, URL, params)
    #     static_params = {
    #         'v': '5.101',
    #         'access_token': TOKEN
    #     }


    def int_id(self):
        params_user = {
            'v': '5.;/l.101',
            'access_token': TOKEN,
            'user_ids': self.id,
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params_user).json()
        self.id = response['response'][0]['id']
    
    # def take_friends_list(self)
    #     params_user = {
    #         'v': '5.101',
    #         'access_token': TOKEN,
    #         'user_ids': self.id,
    #     }
    #     response = requests.get('https://api.vk.com/method/users.get', params=params_user).json()


    def take_groups(self):    
        params_user = {
            'v': '5.101',
            'access_token': TOKEN,
            'user_id': self.id,
            'count': '1000',
            'extended': '1',
            'fields': 'members_count'
        }
        response = requests.get('https://api.vk.com/method/groups.get', params=params_user).json()
        group_list = []
        for i in response['response']['items']:
            group_list.append(dict(gid = i['id'], name = i['name'], members_count = i['members_count']))
        return group_list

    def friends_id_from_groups(self, groups_list):
        print('Выбираем группы в которой нет друзей:')
        for group in groups_list:
            params = {
                'v': '5.101',
                'access_token': TOKEN,
                'group_id': group['gid'],
                'filter': 'friends'
            }
            response_friend_in_group = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()
            print(response_friend_in_group)
            print('.', end='')





user1=User('eshmargunov')
groups_list = user1.take_groups()
print(user1.friends_id_from_groups(groups_list)