from django.test import SimpleTestCase

# Create your tests here.
from app.views import nearhundred


class test_nearhundered(SimpleTestCase):
    def test_near_hundred93(self):
        response = self.client.get("/warmup-1/near-hundred/93")
        self.assertContains(response, True)

    def test_near_hundred90(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, True)

    def test_near_hundred89(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, False)