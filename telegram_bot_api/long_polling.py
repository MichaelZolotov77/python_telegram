import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7948499726:AAGy_XmMMlvYNCr4iiUL0JYdMxjwdp7p33M'
offset = -2
timeout = 20
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')