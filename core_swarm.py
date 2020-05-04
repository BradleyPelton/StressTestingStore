from collections import defaultdict
import csv
import random
import base64

from locust import HttpLocust, TaskSet, task, between, seq_task

users_dict = defaultdict(dict)
with open('users.csv', 'r') as bccsv:
    reader = csv.reader(bccsv, delimiter=',', quotechar='|')
    for row in reader:
        users_dict[row[0]]['password'] = row[1].strip()
        users_dict[row[0]]['cookies'] = []
print(users_dict)


class UserBehaviour(TaskSet):
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
        """login"""
        login_post_request = dict()  # build a payload with user credentials
        login_post_request['username'] = self.username
        # password needs to be encoded to base 64
        encoded_password = base64.b64encode(self.password.encode())  # Convert to b64
        encoded_password = encoded_password.decode()  # Convert from binary back to string
        login_post_request['password'] = encoded_password
        r = self.client.post("/login", json=login_post_request)
        # self.auth_token = r['Auth_token']
        assert 'Auth_token:' in r.text, f"Login failed for {self.username}"
        # print(f"status code for {self.username} login is {r.status_code}")
        # print(r.content)

    @seq_task(3)
    def add_item_to_my_cart(self):
        """I need an ID, and a cookie"""
        # example payload 
        # {"id":"4104ee74-7238-8b70-0fcf-e3a5f14293cd"
        # ,"cookie":"dGVzdGxvY3VzdDAxMTU4OTExOQ==","prod_id":1,"flag":true}

    # @seq_task(4)
    # def get_cart_info(self):
    #     """Print out the number of items in the cart and the total price"""
    # @seq_task(4)
    # def place_order(self):
    #     pass

    # @seq_task(5)

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

# r = requests.post('https://api.demoblaze.com/login', json= {"username": "testlocust01", "password":"Turing123"})

# locust -f core_swarm.py --no-web -c 5 -r .5
# -c (NUMBER_OF_LOCUSTS)
# -r (LOCUST_SPAWN_PER_SECOND)