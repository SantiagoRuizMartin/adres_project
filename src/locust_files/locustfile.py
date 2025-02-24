from locust import HttpUser, task, between


class loadTests(HttpUser):
    wait_time = between(
        1, 3
    )  # Users will wait between 1-3 seconds before the next request

    @task
    def navigate(self):
        """Simulates user go to the main page."""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed! Status: {response.status_code}")
            else:
                response.success()

    @task
    def login(self):
        """Simulates user login."""
        payload = {"username": "tomsmith", "password": "SuperSecretPassword!"}
        with self.client.post(
            "/authenticate", data=payload, catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed! Status: {response.status_code}")
            else:
                response.success()

        with self.client.get("/login", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed! Status: {response.status_code}")
            else:
                response.success()

    @task
    def download_file(self):
        """Simulates that a user download a file."""
        with self.client.get("/download/image.png", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed! Status: {response.status_code}")
            else:
                response.success()
