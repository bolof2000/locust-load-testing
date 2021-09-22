#locust -f locust_load_test.py --host http://localhost:3000 --users 50 --spawn-rate 2
locust -f locust_load_test.py --host https://conduit.productionready.io --users 50 --spawn-rate 2