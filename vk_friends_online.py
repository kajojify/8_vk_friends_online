import vk
import os
import sys


APP_ID = 5571082


def get_user_login():
    return input("Введите логин  ---  ")


def get_user_password():
    return input("Введите пароль ---  ")


def get_online_friends(login, password):
    """Производит авторизацию пользователя вк. Возвращает None
    в случае, если друзей онлайн нет. Возвращает список словарей,
    содержащих информацию о друзьях онлайн."""

    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password
    )
    api = vk.API(session)
    online_friends_id = api.friends.getOnline()
    if not online_friends_id:
        return None
    else:
        friends_online = api.users.get(user_ids=online_friends_id)
        return friends_online


def output_friends_to_console(friends_online):
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")
    if friends_online is None:
        print("\nСейчас у Вас нет друзей онлайн!")
    else:
        print("\nВаши друзья онлайн:\n")
        for friend in friends_online:
            print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        print("Неправильный пароль или логин! Завершение программы.")
        exit()
    output_friends_to_console(friends_online)
