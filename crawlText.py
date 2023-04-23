import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    singleChapterUrl = 'https://blackdn.github.io/2023/04/02/Blog-Title-Border-Tab-2022.md/'
    response = requests.get(url=singleChapterUrl)
    htmlContentBs = BeautifulSoup(response.text, features='html.parser')

    articleContent = htmlContentBs.find(name='article')
    referenceNode = articleContent.find(id="参考")

    for node in referenceNode.find_all_next():
        node.extract()
    referenceNode.extract()

    articleTitle = articleContent.find(name='h1').string
    textContent = articleContent.text.strip()

    with open(f'{articleTitle}.txt', 'w') as file:
        file.write(textContent)

