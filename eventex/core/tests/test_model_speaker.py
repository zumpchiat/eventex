from django.test import TestCase
from eventex.core.models import Speaker

class SpeakerModelTest(TestCase):
    def test_create(self):
        speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://hips.hearstapps.com/hmg-prod/images/gettyimages-515352074.jpg?crop=1xw:1.0xh;center,top&amp;resize=640:*',
            website='https://globo.com',
            description='Programadora e almirante da Marinha dos Estados Unidos nas décadas de 1940 e 1950, criadora da linguagem de programação de alto nível Flow-Matic — base para a criação do COBOL — e uma das primeiras programadoras do computador Harvard Mark I',
        )

        self.assertTrue(Speaker.objects.exists())