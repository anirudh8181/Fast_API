import requests

url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)

if response.status_code==200:
    print(response.json())
else:
    print(f"failed")

