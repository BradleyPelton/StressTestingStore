from lxml.html import fromstring
import requests
# from itertools import cycle
# import traceback

#########################################################
#########################################################
#########################################################
# TODO- This is probably all going to have to be reworked once everything gets moved
# Docker. Leave it be for now


# Scrape a list of proxies from a free website and use them
# https://free-proxy-list.net/

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def get_proxy_dict(ip_address: str):
    proxy_dict = {
              "http": "http://" + ip_address + ":3128",
              "https": "https://" + ip_address + ":1080",
              "ftp": "ftp://" + ip_address + ":3128"
    }
    return proxy_dict

# Create a random CLASS A ipv4 address
# (simplified for brevity, I'm losing some e.g. 124.255.255.255)
random_ip = ".".join(map(str, (random.randint(1, 124) for _ in range(4))))

r = requests.get('https://yahoo.com', proxies=proxyDict)
r = requests.get('https://demoblaze.com', proxies=proxyDict)



# proxies = get_proxies()
# print(proxies)
# proxy_pool = cycle(proxies)

# url = 'https://httpbin.org/ip'
# for i in range(1,11):
#     #Get a proxy from the pool
#     proxy = next(proxy_pool)
#     print("Request #%d"%i)
#     try:
#         response = requests.get(url,proxies={"http": proxy, "https": proxy})
#         print(response.json())
#     except:
#         #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
#         #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
#         print("Skipping. Connnection error")