import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    def get_single_chapter_and_save(url):
        single_chapter_url = url
        response = requests.get(url=single_chapter_url)
        html_content_bs = BeautifulSoup(response.text, features='html.parser')

        article_content = html_content_bs.find(name='article')

        # remove <ul class="pager"> and following node
        pager_node = article_content.find(class_='pager')
        for node in pager_node.find_all_next():
            node.extract()
        pager_node.extract()

        # remove reference node if exist
        reference_node = article_content.find(name='h2', id='参考')
        if reference_node is not None:
            for node in reference_node.find_all_next():
                node.extract()
            reference_node.extract()

        article_title = article_content.find(name='h1').string
        text_content = article_content.text.strip()

        with open(f'{article_title.replace("/","")}', 'w') as file:
            file.write(text_content)


    base_url = 'https://blackdn.github.io'
    get_page_response = requests.get(url=base_url)
    page_content_bs = BeautifulSoup(get_page_response.text, features='html.parser')

    chapter_list = page_content_bs.find(class_='postlist-container').find_all(class_='post-preview')

    for chapter_node in chapter_list:
        current_url = chapter_node.a['href']
        print(f'{base_url}{current_url}')
        get_single_chapter_and_save(f'{base_url}/{current_url}')

