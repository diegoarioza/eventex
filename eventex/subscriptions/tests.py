from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = response = self.client.get('/inscricao/')

    def test_get(self):
        ''' must receive 200'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''must load template'''
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        '''must have in html'''
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email')
        self.assertContains(self.resp, 'type="submit')

    def test_csrf(self):
        '''must have csrf in template'''
        self.assertContains(self.resp, 'csrfmiddlewaretoke')

    def test_has_form(self):
        '''Context must have subscriptiuon form'''
        form = self.resp.context['form']

        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        ''' form have for fields'''
        form = self.resp.context['form']
        self.assertEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
