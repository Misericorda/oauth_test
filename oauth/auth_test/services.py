def get_friends(user_id):
    import requests
    # in case of non-numeric user names
    # api call to find out numeric id
    if not user_id.isdigit():
        url = url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': user_id, 'v': 5.52}
        r = requests.get(url, params=params)
        data = r.json()
        user_id = data['response'][0]['id']
    # api call to get friends and their photos
    url = 'https://api.vk.com/method/friends.get'
    params = {'user_id': user_id, 'order': 'random',
              'count': 5, 'fields': 'photo_200', 'v': 5.52}
    r = requests.get(url, params=params)
    data = r.json()
    friends = data['response']['items']
    return friends
