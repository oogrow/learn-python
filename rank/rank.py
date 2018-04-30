# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
}   #模拟浏览器

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    ranks = soup.select('.pc_temp_num')
    songnames = soup.select('.pc_temp_songname')
    song_times = soup.select('.pc_temp_time')

    for rank, songname, song_time in zip(ranks, songnames, song_times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': songname.get_text().split('-')[0].strip(),
            'song': songname.get_text().split('-')[1].strip(),
            'song_time': song_time.get_text().strip()
        }
        print(data)
        file = open('E://Kugou Music Rank/rank.txt', 'a')
        file.write(str(data))
        file.write('\n\n')

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/html/rank.html']
    for url in urls:
        get_info(url)
