from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

class HomeTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://cdn.britannica.com/81/191581-050-8C0A8CD3/Alan-Turing.jpg',
            website='',
            description='Programadora e almirante da Marinha dos Estados Unidos nas décadas de 1940 e 1950, criadora da linguagem de programação de alto nível Flow-Matic — base para a criação do COBOL — e uma das primeiras programadoras do computador Harvard Mark I',

        )
        self.response = self.client.get(r('home'))

    def test_get(self):
        """ Get in / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        contents = [
            'Grace Hopper',
            'https://cdn.britannica.com/81/191581-050-8C0A8CD3/Alan-Turing.jpg',

               ]
        """Must show keynote speakers """

        for expect in contents:
            with self.subTest():
                self.assertContains(self.response, expect)

    def test_speakers_links(self):
        links = [
            'href="{}#sponsors"'.format(r('home')),
            'href="{}#speakers"'.format(r('home')),
            'href="{}#overview"'.format(r('home')),
            'href="{}#register"'.format(r('home')),
            'href="{}#venue"'.format(r('home')),
        ]
        for expected in links:
            with self.subTest():
                self.assertContains(self.response, expected)
