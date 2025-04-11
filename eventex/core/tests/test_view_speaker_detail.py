from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

from django.test import TestCase


class SpeakerDetailGet(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://cdn.britannica.com/81/191581-050-8C0A8CD3/Alan-Turing.jpg',
            website='',
            description='Programadora e almirante da Marinha dos Estados Unidos nas décadas de 1940 e 1950, criadora da linguagem de programação de alto nível Flow-Matic — base para a criação do COBOL — e uma das primeiras programadoras do computador Harvard Mark I',

        )
        self.response = self.client.get(r('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        """Get should return  status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Should return template core/speaker_detail.html"""
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',

        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def text_context(self):
        """Speaker must be in context"""
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug='not_found'))
        self.assertEqual(404, response.status_code)