import random
from locust import HttpUser, task, between

from aueb_api.aueb_api.settings import STRESS_TEST_TOKEN


class AuebApiUser(HttpUser):
    """ A user querying the AUEB API. """
    wait_time = between(1, 5)  # Wait for 1 to 5 seconds
    header = {
        'Authorization': 'Token {}'.format(STRESS_TEST_TOKEN),
    }

    DEPARTMENTS = [
        'ΠΛΗΡ',
        'ΔΕΟΣ',
    ]


    @task(2)
    def query_exams(self):
        """ Query the standard API endpoint, returning all exams. """
        self.client.get('/api/exams')


    @task
    def query_exams_by_department(self):
        """ Use a department while querying the exams. """
        url = '/api/exams?department={}'.format(random.choices(self.DEPARTMENTS))
        self.client.get(url)


    def on_start(self):
        self.client.headers = self.header
