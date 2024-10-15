from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from faker import Faker
import time

faker = Faker()


def post_cart():
    for _ in range(1000):
        cart = faker.profile()
        response = requests.post(
            'http://localhost:8080/cart'
        )
        #time.sleep(0.1)


def post_item():
    for i in range(1000):
        response = requests.post(
            'http://localhost:8080/item',
            json={
                'id': 0,
                'name': f'New good {i}',
                'price': 10.0,
                'deleted': False
            }
        )
        #time.sleep(0.1)

def get_item():
    for i in range(1000):
        response = requests.get(
            'http://localhost:8080/item/{i}'
        )
        print (response)
        #time.sleep(0.1)


post_cart()
post_item()
get_item()