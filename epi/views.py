from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def epi_home(request):
    return render(request, 'epi/epi-home.html')
