import requests
server = input()
port = input()
a, b = int(input()), int(input())
response = requests.get(f'{server}:{port}?a={a}&b={b}').json()
result = sorted(response['result'])
check = response['check']
print(*result)
print(check)