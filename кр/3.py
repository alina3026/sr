import requests
def anxious(text, server="127.0.0.1:8080", limit=10):
    # url = f'http://{server}'
    response = requests.get(f'http://{server}').json()
        for slov in response:
