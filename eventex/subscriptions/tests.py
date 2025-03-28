from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubForm



class SubscrisptionTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
    def test_get(self):
        """Get in / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain crsf_token"""
        self.assertContains(self.response, 'csrfmiddlewaretoken' )

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Renan Machado', cpf='12312356789',
                    email='zumpchiat@gmail.com', phone='21992034123')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid Post should redirect to /inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'zumpchiat@gmail.com'
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['zumpchiat@gmail.com', 'zumpchiat@gmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Renan Machado', email.body)
        self.assertIn('12312356789', email.body)
        self.assertIn('zumpchiat@gmail.com', email.body)
        self.assertIn('21992034123', email.body)

class SubscribeInvalidPost(TestCase):
    def setUp(self):
        data = dict(name='Renan Machado', cpf='12312356789',
                    email='zumpchiat@gmail.com', phone='21992034123')
        self.response = self.client.post('/inscricao/', {})
    def test_post(self):
        """Invalid Post should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_tamplate(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubForm )

    def test_form_has_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMessage(TestCase):
    def test_has_success(self):
        data = dict(name='Renan Machado', cpf='12312356789',
                    email='zumpchiat@gmail.com', phone='21992034123')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso')