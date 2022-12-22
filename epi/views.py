
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render

# Create your views here.

@login_required
def epi_home(request):
    messages.add_message(request, constants.SUCCESS, 'Mensagem teste!')
    return render(request, 'epi/epi-home.html')
