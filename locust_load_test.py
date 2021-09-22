import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # @task
    # def slow_page(self):
    # self.client.get(url="/slow")

    # @task
    # def index_page(self):
    #   self.client.get(url="/hello")

    @task
    def articles_page(self):
        self.client.get(url="/api/articles?limit=10&offset=0")
