from django.shortcuts import resolve_url as r

from django.test import TestCase


class SpeakerDetailGet(TestCase):
    def setUp(self):
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
            'Programadora e almirante'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)