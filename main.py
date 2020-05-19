import bs4, requests, sys, re
from random import randint

res = requests.get('https://www.reddit.com/user/kerdaloo/m/dankmemer/')
page = bs4.BeautifulSoup(res.text, 'html.parser')

mo = [img for img in page.find_all('img', {'alt': 'Post image'})]

urlReg = re.compile(r'https://preview.redd.it/\w+.jpg?\S+')
links = urlReg.findall(str(mo))

goodlinks = []
for a in links:
    goodlinks += [a.replace("amp;", "")]

if links != []:
    meme = requests.get(goodlinks[randint(1, 2)].replace('"', ''))
else:
    print('memes list is empty right now.')
    sys.exit()

with open('./memes/meme.png', 'wb') as f:
    f.write(meme.content)

print('Meme downloaded!')
