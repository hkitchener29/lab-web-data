from bs4 import BeautifulSoup

with open('sample_listings.html', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.price'):
    print(tag.text)

print(len(soup.select('.sponsored')))

link = soup.select('a.title')[0]
print(link.text)
print(link['href'])

dollars = '$49.99'.replace('$', '')
print(int(round(float(dollars) * 100)))