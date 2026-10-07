from lab_selectors import extract_listings

with open('sample_listings.html', encoding='utf-8') as f:
    listings = extract_listings(f.read())
print(listings[0])
print(len(listings))
