import requests


# https://httpbin.org IS A GREAT WEBSITE FOR TESTING REQUESTS


# HTTP VERBS: GET, PUT, POST, DELETE, HEAD, OPTIONS
# ALL RETURN A RESPONSE OBJECT, r
r = requests.get('https://api.github.com/events')
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

# passing in URL PARAMS, manually vs params=paylod
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)  # Using the built in params tool
r = requests.get('https://httpbin.org/get?key2=value2&key1=value1')  # Manually passing in k, v

#
r = requests.get('https://overlay.adv.gg/advtesttwitch0')
for k, v in vars(r).items():
    print(k, v)

# custom headers 
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)


# Many apis don't even respond to request.OPTIONS . Pretty much an old deprecated http verb