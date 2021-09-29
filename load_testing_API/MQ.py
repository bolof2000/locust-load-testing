import requests
from requests.auth import HTTPBasicAuth
import json


class MarqetaAPI(object):

    def __init__(self):
        self.username = "f2f9f87d-c8af-498c-9f09-4c1256371098gbhfggfh"
        self.password = "c4c90ed8-b8b5-403b-aab0-f1a91e3f371dgghffdfgd"
        self.user_endpoint = "/users"
        self.url = "https://sandbox-api.marqeta.com/v3/users"
        self.base_url = "https://sandbox-api.marqeta.com/v3"
        self.header = {"Content-Type": "application/json"}
        self.auth = HTTPBasicAuth(self.username, self.password)
        self.userToken = None
        self.response = None

    def loginRequest(self):
        self.response = requests.get(url=self.base_url + "/users",
                                     auth=HTTPBasicAuth(self.username, self.password))

        # print(response.status_code)
        print(self.response.text)

    def createUser(self):
        with open("/Volumes/dev-env/Python-Projects/load-testing/load_testing_API/createUser.json") as testdata:
            payload = json.load(testdata)

        self.response = requests.post(url=self.base_url + "/users", data=json.dumps(payload),
                                      headers=self.header, auth=self.auth)

        # print(response.status_code)
        print(self.response.text)
        # print(response.json().get("token"))
        self.userToken = self.response.json().get("token")
        print(self.userToken)

    # create a card for a specific user
    def createCard(self):
        payload = {
            "token": "my_test_card_01",
            "user_token": self.userToken,
            "fulfillment": {
                "card_personalization": {
                    "text": {
                        "name_line_1": {
                            "value": "Jane Doe"
                        },
                        "name_line_2": {
                            "value": "My card personalization line 2"
                        }
                    },
                    "images": {
                        "card": {
                            "name": "my_card_logo.png",
                            "thermal_color": "Black"
                        },
                        "signature": {
                            "name": "my_signature.png"
                        },
                        "carrier_return_window": {
                            "name": "my_return_address_image.png"
                        }
                    }
                }
            },
            "card_product_token": "my_cardproduct_01",
            "metadata": {
                "key1": "value1",
                "key2": "value2"
            }
        }

        self.response = requests.post(url=self.base_url + "/cards", data=json.dumps(payload),
                                      headers=self.header, auth=self.auth)
        print(self.response.status_code)
        print(self.response.text)


testMQ = MarqetaAPI()
print(testMQ.loginRequest())
# testMQ.createUser()
# testMQ.createCard()
