from locust import HttpUser, constant, task, SequentialTaskSet


class LoadRequest(HttpUser):

    def __init__(self):
        self.username = "f2f9f87d-c8af-498c-9f09-4c1256371098"
        self.password = "c4c90ed8-b8b5-403b-aab0-f1a91e3f371d"
        self.user_endpoint = "/users"
        self.url = "https://sandbox-api.marqeta.com/v3/users"
        self.base_url = "https://sandbox-api.marqeta.com/v3"
        self.header = {"Content-Type": "application/json"}
        # self.auth = HTTPBasicAuth(self.username, self.password)
        self.userToken = None
        self.response = None

    @task
    def place_order(self):
        self.response = self.client.get(url="/users")
        print(self.response.status_code)
