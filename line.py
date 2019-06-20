#-*- coding: utf-8-*-

import requests

def line():
    url = "https://notify-api.line.me/api/notify"
    token = "発行されたトークンをここに記入"
    headers = {"Authorization": "Bearer " + token}
    message = 'テスト'
    payload = {"message":  message}
    requests.post(url, headers=headers, params=payload)


if __name__ == '__main__':
    line()
