from django.shortcuts import render
from .models import position
from .LSE_Scrape import test

def index(request):

    position_data = position.objects.all()

    if request.method == 'POST' and 'run_script' in request.POST:
        test()

    context = {'positions': position_data}

    return render(request, 'index.html', context)
