from bs4 import BeautifulSoup


html = """
<body>
    <p class="odd">Paragraph 1</p>
    <p class="even" id="vip">Paragraph 2</p>
    <p class="odd">Paragraph 3</p>
    <p class="even">Paragraph 4</p>
    <p class="odd">Paragraph 5</p>
</body>
"""


soup = BeautifulSoup(html, 'html.parser')
# odd_paragraphs = soup.find_all(class_='odd')
odd_paragraphs = soup.select('.odd')
print(odd_paragraphs)

