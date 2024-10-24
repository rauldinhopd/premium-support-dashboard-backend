from locust import HttpUser, TaskSet, task, between


# Define user behavior
class UserBehavior(TaskSet):

    @task(1)
    def get_overview(self):
        self.client.get("/overview")


# Define Locust user class
class FastAPIUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Simulates a delay between requests
