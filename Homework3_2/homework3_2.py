import requests

SERVICE_TOKEN = 'adcae950adcae950adcae95046ada7e3f7aadcaadcae950f043253928122f9fc7f4ade7'


class User():
    first_name = ''
    last_name = ''
    # id может быть число или имя (далее мы будем всегда получать числовой id, чтобы получать список друзей.
    id = ''
    link = 'https://vk.com/'
    is_closed = ''

    def __init__(self, id):
        self.id = id

    def user_info(self):
        params = {
            'v': '5.101',
            'access_token': SERVICE_TOKEN,
            'user_ids': self.id,
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params).json()
        self.is_closed = response['response'][0]['is_closed']
        self.first_name = response['response'][0]['first_name']
        self.last_name = response['response'][0]['last_name']
        self.id = response['response'][0]['id']
        self.link += response['response'][0]['domain']
        return response



    def user_friends(self):
        if self.is_closed == False:
            params = {
                'v': '5.101',
                'access_token': SERVICE_TOKEN,
                'user_id': self.user_info()['response'][0]['id']
            }
            response = requests.get('https://api.vk.com/method/friends.get', params=params).json()
            friends_list = set(response['response']['items'])
            return friends_list
        else:
            return False

def common_friends(set1, set2):
    common = list(set1 & set2)
    return common


def userclass(userlist):
    newlist = []
    for i in userlist:
        newlist.append(User(i))
    return newlist


def main():
    user_a, command, user_b = input('Введите id 2-х пользователей и комманду в виде аперанда: ').split()
    if command == '&':
        user1, user2 = User(user_a), User(user_b)
        user1.user_info()
        user2.user_info()
        if user1.is_closed == True:
            print (f'Пользователь {user1.link} ограничил доступ к списку друзей')
        elif user1.is_closed == True:
            print (f'Пользователь {user2.link} ограничил доступ к списку друзей')
        else:
            common_friend = common_friends(user1.user_friends(), user2.user_friends())
            classlist = userclass(common_friend)
            if len(classlist) == 0:
                print ('Общих друзей нет')
            else:
                print(f'Кол-во общих друзей: {len(classlist)}')
                for i in classlist:
                    i.user_info()
                    print('{} - {} {}'.format(i.link, i.first_name, i.last_name))
    else:
        print('Введена неверная команда')


if __name__ == '__main__':
    main()