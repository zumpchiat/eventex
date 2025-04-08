from cmath import phase

from django.test import TestCase
from eventex.subscriptions.forms import SubForm


class SubuscptionFormTest(TestCase):

    def test_has_fields(self):
        """" Form must have 4 fields """
        self.form = SubForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digits(self):
        """CPF must only accept digits. """
        form = self.make_validate_form(cpf='ABDC12345672')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits. """
        form = self.make_validate_form(cpf='1114')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_name_must_be_capitalize(self):
        """Name must be capitalize."""
        form = self.make_validate_form(name='José SILVa')
        self.assertEqual('José Silva', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validate_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validate_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email or Phone are optional, but one must be informed."""
        form = self.make_validate_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validate_form(self, **kwargs):
        valid = dict(name='José Silva', cpf='12345678912',
                     email='jose@gmail.com', phone='2198898888')
        data = dict(valid, **kwargs)
        form = SubForm(data)
        form.is_valid()
        return form
