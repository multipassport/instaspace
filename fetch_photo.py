import requests

def fetch_photo(url, filepath):
    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)