import requests
import json
from urllib.parse import urlencode
from pprint import pprint

TOKEN =  '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

class User:
    id = ''

    def __init__(self, id):
        self.id = id
        params = {
            'v': '5.101',
            'access_token': TOKEN,
            'user_ids': self.id,
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params).json()
        self.id = response['response'][0]['id']


    def take_groups(self):    
        params_user = {
            'v': '5.101',
            'access_token': TOKEN,
            'user_id': self.id,
            'count': '1000',
            'extended': '1',
            'fields': ['members_count']
        }
        response = requests.get('https://api.vk.com/method/groups.get', params=params_user).json()
        group_list = []
        print(response)
        for i in response['response']['items']:
            group_list.append(dict(gid=i['id'], name=i['name'], members_count=i['members_count']))
        return group_list

    def groups_without_frieds(self, groups_list):
        list_without_friends = []
        print('Выбираем группы в которой нет друзей')
        for ind, group in enumerate(groups_list):
            params = {
                'v': '5.101',
                'access_token': TOKEN,
                'group_id': group['gid'],
                'filter': 'friends'
            }
            response_friend_in_group = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()
            print('\r{} из {} групп пройдено'.format(ind+1, len(groups_list)), end='')
            if response_friend_in_group['response']['count'] == 0:
                list_without_friends.append(groups_list[ind])
        print()
        return list_without_friends

def write_to_json(group_list):
    with open('groups.json', mode='w', encoding='utf-8') as file:
        json.dump(group_list, file, ensure_ascii=False, indent=4)
    print('Список групп записан в файл groups.json')

def main():
    user1 = User('eshmargunov')
    groups_list = user1.take_groups()
    write_to_json(user1.groups_without_frieds(groups_list))

if __name__ == '__main__':
    main()

