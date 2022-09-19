import os

from dotenv import load_dotenv
from utils.request_helper import BaseSession

load_dotenv()


def reqres() -> BaseSession:
    base_url = os.getenv('reqres_url')
    return BaseSession(base_url=base_url)


def demoqa() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    return BaseSession(base_url=demo_url)

