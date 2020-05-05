from collections import defaultdict
import csv
import random
import base64
import uuid

from locust import HttpLocust, TaskSet, TaskSequence, task, between, seq_task

users_dict = defaultdict(dict)  # TODO- switch to an ordered dict?
with open('users.csv', 'r') as bccsv:
    reader = csv.reader(bccsv, delimiter=',', quotechar='|')
    for row in reader:
        users_dict[row[0]]['password'] = row[1].strip()
        users_dict[row[0]]['cookies'] = []
print(users_dict)


class UserBehaviour(TaskSequence):
    # TODO- TIMEOUTS
    def setup(self):
        """setup the taskset class"""
        pass

    def teardown(self):
        """teardown the taskset class"""
        pass

    def on_start(self):
        """on_start is called when a Locust is created"""
        random_user = users_dict.popitem()
        self.username = random_user[0]
        self.password = random_user[1]['password']  # the value(a dict) is the second object
        self.uuid = str(uuid.uuid1())  # UUID to be used multiple places as a payload obj
        self.auth_token = ''  # Created in the login process

        # TODO- add proxy logic here

    def on_stop(self):
        """on_stop is called when the Locust finishes is stopping """
        pass

    @seq_task(1)
    def home_page(self):
        # self.client starts a request Session(). this session keeps track of some headers
        self.client.get("https://demoblaze.com")

    @seq_task(2)
    def login(self):
        """login. TODO- refactor with a custom request.auth.AuthBase class?"""
        login_post_request = dict()  # build a payload with user credentials
        login_post_request['username'] = self.username

        # password needs to be encoded to base 64
        encoded_password = base64.b64encode(self.password.encode())  # Convert to b64
        encoded_password = encoded_password.decode()  # Convert from binary back to string
        login_post_request['password'] = encoded_password

        r = self.client.post("/login", json=login_post_request)
        assert 'Auth_token:' in r.text, f"Login failed for {self.username}"

        self.auth_token = r.json().split(": ")[-1]
        # print(f"generated auth_token is {self.auth_token}")

    @seq_task(3)
    def add_item_to_my_cart(self):
        """ Add a random item to my cart by sending a post request"""
        # TODO- UNTESTED INSIDE LOCUST CLASS (tested standalone)
        # Need to construct a payload
        payload = {}
        if not self.auth_token:
            print(f"NO AUTH TOKEN FOUND FOR {self.username}")
        payload["cookie"] = self.auth_token
        payload["prod_id"] = random.randint(1, 15)  # 15 items in the database
        payload["id"] = self.uuid
        payload["flag"] = 'true'
        # print(f"payload for {self.username} is")
        # print(payload)

        new_item_post = self.client.post('/addtocart', json=payload)

        # print(f"add new item post {self.username} has status code {new_item_post.status_code}")
        print(new_item_post.content)

        # assert new_item_post.status_code == 200
        # assert new_item_post.content == b''

    @seq_task(4)
    def get_cart_info(self):
        """Print out the number of items in the cart and the total price"""
        payload = {}
        payload["cookie"] = self.auth_token
        payload["flag"] = 'true'

        view_cart_post = self.client.post('/viewcart', json=payload)

        # print(f"view_cart_post status code is {view_cart_post.status_code}")
        # print(view_cart_post.content)

        assert "Items" in view_cart_post.content, "view_cart_post failed, maybe empty cart?"
        # TODO- TEST RUNNING VIEWCART ON AN EMPTY CART

    @seq_task(5)
    def place_order(self):
        # There is no place_order request? The only request generated is a deletecart post
        payload = {}
        payload["cookie"] = self.username

        delete_cart_post = self.client.post('/deletecart', json=payload)

        # print(f"delete_cart_post status code is {delete_cart_post.status_code}")
        # print(delete_cart_post.content)

        assert "Item deleted" in delete_cart_post.content, "place order post failed"

    # def logout(self):
    #     self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    # def index(self):
    #     self.client.get("/")

    # def profile(self):
    #     self.client.get("/profile")


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(2, 3)
    host = 'https://api.demoblaze.com'


# import requests
# s = requests.Session()
# s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
# (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'})

# # LOGIN POST REQUEST, WORKING
# r = s.post('https://api.demoblaze.com/login', json={
#     "username": "testlocust01", "password": "VHVyaW5nMTIz"})

# # ADD ITEM TO CART POST REQUEST, WORKING
# payload = {}
# payload["cookie"] = r.json().split(": ")[-1]
# payload["prod_id"] = 1
# payload["id"] = str(uuid.uuid1)
# payload["flag"] = 'true'
# new_item_post = s.post('https://api.demoblaze.com/addtocart', json=payload)


# EXAMPLE 
# user=15b052bb-14cf-27c5-b923-559ca30046ee
# HERE IS HOW THE UUID/GUID IS BEING GENERATED
# function guid() {
#   function s4() {
#     return Math.floor((1 + Math.random()) * 0x10000)
#       .toString(16)
#       .substring(1);
#   }
#   return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
#     s4() + '-' + s4() + s4() + s4();
# }

# document.cookie = "user=" + guid();
# https://stackoverflow.com/questions/39232293/how-to-get-a-uuid-with-python-requests


# locust -f core_swarm.py --no-web -c 5 -r .5
# -c (NUMBER_OF_LOCUSTS)
# -r (LOCUST_SPAWN_PER_SECOND)