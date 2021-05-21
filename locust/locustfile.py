from locust import HttpUser, task, between


class PyUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def hello_world(self):
        self.client.get("/api/js")

    @task(5)
    def crud(self):
        self.client.post("/api/js/database/register", {
            "name": "Test",
            "username": "test-0-1"
        })
        self.client.get("/api/js/database/profile?name=Test")
        self.client.delete("/api/js/database/delete?name=Test")

class JsUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def hello_world(self):
        self.client.get("/api/py")

    @task(5)
    def crud(self):
        self.client.post("/api/py/database/register", json={
            "name": "Test",
            "username": "test-0-1"
        })
        self.client.get("/api/py/database/profile?name=Test")
        self.client.delete("/api/py/database/delete?name=Test")
