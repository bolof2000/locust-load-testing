from locust import HttpLocust, TaskSet, task, HttpUser, constant
import json
from requests.auth import HTTPBasicAuth


class Tests(HttpUser):
    host = "https://sandbox-api.marqeta.com/v3"
    wait_time = constant(1)

    # headers = {"Content-Type": "application/json"}

    @task
    def createUser(self):
        data = {
            "first_name": "Bbsegungtetsts",
            "last_name": "JSONBOLOFINDE01",
            "token": "User_MQ_016",
            "email": "mqusertoken16@gmail.com",
            "password": "P@ssw0rd"
        }

        headers = {"Content-Type": "application/json"}
        response = self.client.request(method="POST", url="/users", data=json.dumps(data),
                                       auth=HTTPBasicAuth(username="f2f9f87d-c8af-498c-9f09-4c1256371098",
                                                          password="c4c90ed8-b8b5-403b-aab0-f1a91e3f371d"),
                                       headers=headers)
        print(response.status_code)
        print(response.text)

    @task
    def getAllUsers(self):
        headers = {"Content-Type": "application/json"}
        response = self.client.request(method="GET", url="/users",
                                       auth=HTTPBasicAuth(username="f2f9f87d-c8af-498c-9f09-4c1256371098",
                                                          password="c4c90ed8-b8b5-403b-aab0-f1a91e3f371d"),
                                       headers=headers)

        print(response.status_code)
        print(response.text)
