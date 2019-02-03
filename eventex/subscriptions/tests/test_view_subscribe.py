from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
import unittest


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
        # print(self.resp.context)

    def test_get(self):
        ''' must receive 200'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''must load template'''
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        '''must have in html'''
        tags = (('<form', 1),
               ('<input', 6),
               ('type="text"', 3),
               ('type="email', 1),
               ('type="submit', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        '''must have csrf in template'''
        self.assertContains(self.resp, 'csrfmiddlewaretoke')

    def test_has_form(self):
        '''Context must have subscription form'''
        form = self.resp.context['form']

        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        ''' form have for fields'''
        form = self.resp.context['form']
        self.assertEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostValid(TestCase):
    def setUp(self):
        data = {'name':'Diego', 'cpf':'12345678901', 'email':'diego@diego.com', 'phone':'3453343435'}
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)
        self.assertRedirects(self.resp, '/inscricao/1/')

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

@unittest.skip('To be removed.')
class SubscribeSucessMessage(TestCase):
    def setUp(self):
        data = dict(name='Diego', cpf='3424324234', email='diego@sdsd.dsd', phone='4545435345')
        self.resp = self.client.post('/inscricao/', data, follow=True)

    def test_Message(self):
        self.assertContains(self.resp, 'Inscricao realizada com Sucesso')

    def test_subscriptionb_link(self):
        self.assertContains(self.resp, 'href="/inscricao/"')
