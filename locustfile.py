import os
import string
from locust import HttpLocust, TaskSet, task
from random import randint

class UserBehavior(TaskSet):
    @task(1000)
    def index(self):
        response = self.client.get("/")

    @task(30)
    def contribute(self):
        self.client.get("/contribute")

    @task(30)
    def project2261(self):
        self.client.get("/project/2261")

    @task(30)
    def project1788(self):
        self.client.get("/project/1788")

    @task(30)
    def randomProject(self):
        self.client.get("/project/%d" % randint(20,2300), name="/project/[n]")

    @task(30)
    def randomPage(self):
        self.client.get("/contribute?page=%d&difficulty=ALL" % randint(1,83), name="/contribute?page=[n]")

    @task(30)
    def randomProjectTask(self):
        self.client.get("/project/%d?task=%d" % (randint(20,2300), randint(1,20)), name="/project/[n]?task=[n]")

class MyLocust(HttpLocust):
    host = os.getenv('TARGET_URL', "http://localhost")
    task_set = UserBehavior
    min_wait = 45
    max_wait = 50
