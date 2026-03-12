import requests

url = 'https://openlibrary.org/search.json'
params = {
    'author': 'J.K. Rowling',
    'published_in': 1997
}

response = requests.get(url, params=params)

if response.status_code == 200:
    books = response.json()
    for book in books['docs'][:5]:  # limit to first 5 results
        print(f"Title: {book.get('title')}, Year: {book.get('first_publish_year')}")
else:
    print(f"Error: {response.status_code}")

#print(books)    
