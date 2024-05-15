import requests

response1 = requests.get("https://pypi.org")
print(response1.text)
# print(response.status_code)

payload = {
    "q": "flask"
}

response = requests.get("https://pypi.org", params=payload)
# print(response.url)

url = "https://jsonplaceholder.typicode.com/posts"

response2 = requests.get(url)
data = response2.json()
# print(data)