

import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL.title)

print(page.text)
