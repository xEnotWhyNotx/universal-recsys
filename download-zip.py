import requests

url = 'https://api.github.com/repos/xEnotWhyNotx/universal-recsys/contents/train_dataset_DCS.zip'
response = requests.get(url)
response.raise_for_status()

download_url = response.json()['download_url']
response = requests.get(download_url)
response.raise_for_status()

with open('train_dataset_DCS.zip', 'wb') as file:
    file.write(response.content)