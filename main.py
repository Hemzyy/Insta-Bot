import bs4, requests, sys, re
from random import randint
from instapy_cli import client

memelinks = []

while memelinks == []:
    res = requests.get('https://www.reddit.com/user/kerdaloo/m/dankmemer/')
    page = bs4.BeautifulSoup(res.text, 'html.parser')

    mo = [img for img in page.find_all('img', {'alt': 'Post image'})]

    urlReg = re.compile(r'https://preview.redd.it/\w+.jpg?\S+')
    links = urlReg.findall(str(mo))

    for a in links:
        memelinks += [a.replace("amp;", "")]

meme = requests.get(memelinks[randint(1, 2)].replace('"', ''))
with open('./memes/meme.jpg', 'wb') as f:
    f.write(meme.content)

username = 'username'
password = 'password'
image = './file/path.jpg'
text = 'This is a test.' + '\r\n' + '#test'

with client(username, password) as cli:
    cli.upload(image, text)

print('Meme posted!')
