from django.shortcuts import render
from eventex.subscriptions.forms import SubForm

def subscribe(request):
    context = {'form': SubForm()}
    return render(request, 'subscriptions/subscription_form.html', context)