from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if not form.is_valid():
            return render(request, 'subscriptions/subscription_form.html', {'form': form})

        # Send E-mail
        template_name = 'subscriptions/subscription_email.txt'
        context = form.cleaned_data
        subject = 'Confirmação de inscrição'
        from_ = settings.DEFAULT_FROM_EMAIL
        to = form.cleaned_data['email']

        body = render_to_string(template_name, context)
        try:
            mail.send_mail(subject, body, from_, [from_, to])
        except:
            pass

        improviso = form.cleaned_data.get('name')
        Subscription.objects.create(**{'name': improviso})
        # Success Feedback
        messages.success(request, 'Inscricao realizada com Sucesso')
        return HttpResponseRedirect('/inscricao/')



def new(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


