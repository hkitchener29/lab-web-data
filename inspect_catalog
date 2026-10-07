from lab_selectors import extract_listings

with open('sample_merchandise.html', encoding='utf-8') as f:
    catalog = extract_listings(f.read())
for item in catalog:
    print(item['name'])