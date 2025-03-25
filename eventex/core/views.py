from django.shortcuts import render
from eventex.subscriptions.forms import SubForm

# Create your views here.
def home(request):


    return render(request, 'index.html')