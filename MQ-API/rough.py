from locust import User, task


class CreateTests(User):

    @task
    def launch(self):
        print("launching the URL")

    @task
    def search(self):
        print("searching")
