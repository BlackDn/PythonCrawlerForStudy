import requests
import os

# url for BiZhiMiao space: https://space.bilibili.com/6823116/album
if __name__ == '__main__':

    dir_path = 'miao/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    page_number = 0
    url_to_get_page = f'https://api.bilibili.com/x/dynamic/feed/draw/doc_list?uid=6823116&page_num={page_number}&page_size=30&biz=all&jsonp=jsonp'

    for current_page in range(10):
        page_number = current_page
        response_page = requests.get(url_to_get_page)
