from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = {'name':'Diego','cpf':'12345678901', 'email':'diego@diego.com', 'phone':'3453343435'}
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'diego@diego.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        self.assertIn('Diego', self.email.body)
