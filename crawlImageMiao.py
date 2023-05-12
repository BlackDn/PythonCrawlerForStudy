import requests
import os

# url for BiZhiMiao space: https://space.bilibili.com/6823116/album
if __name__ == '__main__':

    dir_path = 'miao/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    page_number = 0
    url_to_get_page = f'https://api.bilibili.com/x/dynamic/feed/draw/doc_list?uid=6823116&page_num={page_number}&page_size=30&biz=all&jsonp=jsonp'

    # only crawl 3 pages
    for current_page in range(3):
        page_number = current_page
        print(f'We are in page {page_number}')

        response_page = requests.get(url_to_get_page)
        response_page_json = response_page.json()
        img_list = response_page_json['data']['items']

        # only crawl 5 images in each page
        for img_index in range(5):
            for index, pics in enumerate(img_list[img_index]['pictures']):
                img_name = f'page{page_number}-img{img_index}-{index}.jpg'

                if pics['img_width'] < pics['img_height']:
                    print(f'skip {img_name}')
                    break

                img_url = pics['img_src']
                img_response = requests.get(img_url)

                with open(f'{dir_path}{img_name}', 'wb') as f:
                    f.write(img_response.content)
                print(f'download {img_name} successfully')

