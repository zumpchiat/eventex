from django.test import TestCase

from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Renan Machado', cpf='12312356789',
                    email='zumpchiat@gmail.com', phone='21992034123')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):

        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'zumpchiat@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['zumpchiat@gmail.com', 'zumpchiat@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Renan Machado',
            '12312356789',
            'zumpchiat@gmail.com',
            '21992034123',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)


