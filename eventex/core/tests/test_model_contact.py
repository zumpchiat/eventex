from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='RZM',
            slug='rzm',
            photo='https://tm.ibxk.com.br/2025/04/03/03094025585000.jpg'
        )

    def test_create(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='contato@bol.com')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact(speaker=self.speaker, kind=Contact.PHONE,
                          value='21993456677')

    def test_choices(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)
