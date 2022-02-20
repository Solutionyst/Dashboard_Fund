from django.shortcuts import render
from .models import position

def index(request):

    position_data = position.objects.all()

    context = {'positions': position_data}

    return render(request, 'index.html', context)
