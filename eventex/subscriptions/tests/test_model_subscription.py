from django.test import TestCase
from eventex.subscriptions.models import Subscription



class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'User 1',
            cpf = '14785236978',
            email = 'alph23@gmail.com',
            phone = '21- 89786546'
        )
        self.obj.save()