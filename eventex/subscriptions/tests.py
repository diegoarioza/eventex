from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

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

class Subscribe_Post_Test(TestCase):
    def setUp(self):
        data = {'name':'Diego','cpf':'12345678901', 'email':'asas@asass.ass', 'phone':'3453343435'}
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, email.subject)


    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)


    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'diego@diego.com']

        self.assertEqual(expect, email.to)

