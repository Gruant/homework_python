import requests
from urllib.parse import urlencode

TOKEN =  '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

class User():
    id = ''
    is_closed = bool

    def __init__(self, id):
        self.id = id

    def take_user_info(self):    
        params_user = {
            'v': '5.101',
            'access_token': TOKEN,
            'user_ids': self.id,
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params_user).json()
        self.is_closed = response['response'][0]['is_closed']
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
        print('.')
        group_list = []
        for i in response['response']['items']:
            group_list.append(dict(gid = i['id'], name = i['name'], members_count = i['members_count']))
        print(group_list)

user1=User('eshmargunov')
user1.take_user_info()
print(user1.take_groups())