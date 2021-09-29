import requests
from requests.auth import HTTPBasicAuth
import json


class PerformanceTests(object):

    def __init__(self):
        self.baseurl = "https://api.realworld.io/api/"
        self.user_endpoint = "users"
        self.response = None
        self.login_endpoint = "users/login"
        # self.autho = 'Token ' + self.login()
        self.header = {"Content-Type": "application/json"}

    def login(self):
        payload = {
            "user": {
                "email": "locust02@gmail.com",
                "password": "locust"
            }
        }

        self.response = requests.post(url=self.baseurl + self.login_endpoint, data=json.dumps(payload),
                                      headers=self.header)

        # print(self.response.text)
        print(self.response.status_code)
        token = self.response.json().get("user").get("token")

        return token

    def createUserTest(self):
        payload = {
            "user": {
                "email": "locust06@gmail.com",
                "password": "locust",
                "username": "locust06"
            }
        }

        self.response = requests.post(url=self.baseurl + self.user_endpoint, data=json.dumps(payload),
                                      headers=self.header)

        print(self.response.status_code)
        print(self.response.text)

    def testCreateArticle(self):
        auth = 'Token ' + self.login()
        head = {'Authorization': auth}

        payload = {
            "article": {
                "tagList": [],
                "title": "Test locus new one ",
                "description": "test articulateness",
                "body": "article creation "
            }
        }
        response = requests.post(url="https://api.realworld.io/api/articles/", data=json.dumps(payload),
                                 headers=head)

        print(response.status_code)
        print(response.text)


test = PerformanceTests()
# test.createUserTest()
# test.login()
test.testCreateArticle()
