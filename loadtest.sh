#locust -f locust_load_test.py --host http://localhost:3000 --users 50 --spawn-rate 2
locust -f locust_load_test.py --host https://conduit.productionready.io --users 50 --spawn-rate 2

locust -f- load_testing_API/test_performance_endpounts.py -U 2 -r 2 -t 10s --headless

locust -f pef.py --host https://sandbox-api.marqeta.com/v3 --user 2 --spawn-rate 2
