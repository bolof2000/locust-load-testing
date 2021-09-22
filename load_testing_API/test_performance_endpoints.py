from locust import HttpUser, constant, task, SequentialTaskSet
from load_testing_API.readtestdata import ReadCsvFile


class LoadRequest(SequentialTaskSet):

    @task
    def place_order(self):
        test_data = ReadCsvFile(
            "/Volumes/dev-env/Python-Projects/load-testing/load_testing_API/customer-data.csv").read()

        print(test_data)

        data = {

            "custname": test_data['name'],
            "custemail": test_data['email'],
            "size": test_data['size'],
            "topping": test_data['toppings'],
            "delivery": test_data['time'],
            "comments": test_data["instructions"]
        }

        name = "Order for " + test_data['name']

        with self.client.post("/post", catch_response=True, name=name, data=data) as response:

            if response.status_code == 200 and test_data['name'] in response.text:
                response.success()

            else:
                response.failure("failure in processing the order")


class LoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [LoadRequest]