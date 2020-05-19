import bs4, requests, sys, re
from random import randint

goodlinks = []

while goodlinks == []:
    res = requests.get('https://www.reddit.com/user/kerdaloo/m/dankmemer/')
    page = bs4.BeautifulSoup(res.text, 'html.parser')

    mo = [img for img in page.find_all('img', {'alt': 'Post image'})]

    urlReg = re.compile(r'https://preview.redd.it/\w+.jpg?\S+')
    links = urlReg.findall(str(mo))

    for a in links:
        goodlinks += [a.replace("amp;", "")]


meme = requests.get(goodlinks[randint(1, 2)].replace('"', ''))
with open('./memes/meme.png', 'wb') as f:
    f.write(meme.content)

print('Meme downloaded!')
