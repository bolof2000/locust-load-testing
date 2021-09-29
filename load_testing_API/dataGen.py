from faker import Faker

fake = Faker()


def generate_api_test_data():
    dataProvider = {
        "custname": fake.name(),
        "custemail": fake.email(),
        "username": fake.simple_profile()['username']
    }

    return dataProvider
