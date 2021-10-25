from locust import TaskSet, constant, task, HttpUser
import json
from requests.auth import HTTPBasicAuth


class TestAllTasks(TaskSet):

    def __init__(self):
        self.username = "f2f9f87d-c8af-498c-9f09-4c1256371098"
        self.password = "c4c90ed8-b8b5-403b-aab0-f1a91e3f371d"

        self.headers = {"Content-Type": "application/json"}

    @task
    def getAllUsers(self):
        self.client.reques


class LoadTests(HttpUser):
    host = "https://sandbox-api.marqeta.com/v3"
    wait_time = constant(1)
    tasks = [TestAllTasks]