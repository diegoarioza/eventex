from django.test import TestCase

class SubscribeTest(TestCase):
    def test_get(self):
        response = self.client.get('/inscricao/')
        self.assertEqual(200, response.status_code)
