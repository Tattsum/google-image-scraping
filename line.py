#-*- coding: utf-8-*-

import requests
import datetime
import googleimagescraping
import argparse
import os

# TOKEN = os.environ["TOKEN"] #環境変数"TOKEN"を取得

def line(message, images):
    url = "https://notify-api.line.me/api/notify"
    token = "vsX9w5PycFVrnzvgJzbvYyHYrFcMYd9yUTPEIpCZy6H"
    headers = {"Authorization": "Bearer " + token}
    payload = {"message":  message}

    if len(images) == 0:
        # 画像なしテキストのみ送信
        requests.post(url, data=payload, headers=headers)
    else:
        # 画像ありテキスト＋画像送信
        files = {"imageFile": open(images, "rb")}
        requests.post(url, data=payload, headers=headers, files=files)

def main():
    # googleimagescraping.scraping()
    message = '嵐 最高!!'
    path = googleimagescraping.download_path
    base_path = os.path.abspath(path)
    for dirname in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, dirname)):
            dir = base_path + "/" +dirname
            for filename in os.listdir(dir):
                if os.path.isfile(os.path.join(dir,filename)):
                    files =  base_path + "/" + dirname + "/" +filename
                    file_full_path = os.path.abspath(files)
                    line(message,file_full_path)


if __name__ == '__main__':
    main()
