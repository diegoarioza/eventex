from django.test import TestCase
from eventex.subscriptions.models import Subscriptions


class SubscriptionModelTest(TestCase):
    def test_create(self):
        obj = Subscriptions(
            name = "Diego Arioza"
        )
        obj.save()
        self.assertTrue(Subscriptions.objects.exists())