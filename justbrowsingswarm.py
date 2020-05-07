from collections import defaultdict
import base64
import uuid
import random

from locust import HttpLocust, TaskSet, TaskSequence, task, between, seq_task


##############################################################################################
##############################################################################################
##############################################################################################
""" THESE TESTS ARE ONLY DESIGNED FOR USERS WHO ARE "just browsing" I.E. NOT LOGGED IN. NO
COMPLEX BEAHVIOR(e.g. purchases) WILL BE PERFORMED. THE STRESS TESTS ARE JUST GENERAL GET
REQUESTS TO THE VARIOUS PAGES. FOR MORE COMPLICATED TESTS, SEE coreswarm.py
"""
##############################################################################################
##############################################################################################
##############################################################################################


class UserBehaviour(TaskSet):
    # def setup(self):
    #     """setup the taskset class"""
    #     pass

    # def teardown(self):
    #     """teardown the taskset class"""
    #     pass

    # def on_start(self):
    #     """on_start is called when a Locust is created"""
    #     self.uuid = str(uuid.uuid1())  # UUID to be used multiple places as a payload obj

        # TODO- add proxy logic here

    # def on_stop(self):
    #     """on_stop is called when the Locust finishes is stopping """
    #     pass

    @task(1)
    def home_page(self):
        page_get = self.client.get("/")

        assert page_get.status_code == 200

    @task(1)
    def index_page(self):
        page_get = self.client.get("/index.html")

        assert page_get.status_code == 200

    @task(1)
    def cart_page(self):
        page_get = self.client.get('/cart.html')

        assert page_get.status_code == 200

    @task(1)
    def random_product_page(self):
        random_id = random.randint(1, 15)  # 15 unique product pages.
        payload = {"idp_": random_id}
        page_get = self.client.get('/prod.html', params=payload)

        assert page_get.status_code == 200



class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(2, 3)
    host = 'https://demoblaze.com'



# locust -f justbrowsingswarm.py --no-web -c 5 -r .5
# -c (NUMBER_OF_LOCUSTS)
# -r (LOCUST_SPAWN_PER_SECOND)