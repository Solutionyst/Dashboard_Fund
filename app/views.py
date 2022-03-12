from django.shortcuts import render, redirect
from .models import position
from .LSE_Scrape import test
from .forms import PositionForm

def index(request):

    position_data = position.objects.all()

    if request.method == 'POST' and 'run_script' in request.POST:
        test()

    context = {'positions': position_data}

    return render(request, 'index.html', context)

def new_position(request):
    positions = PositionForm

    if request.method == 'POST':
        positions = PositionForm(request.POST)
        if positions.is_valid():
            positions.save()
            return redirect('Dashboard')

    context = {'position_add': positions}
    return render(request, "new-position.html", context)

def Position_Delete(request,pk):
    positions = position.objects.get(ticker=pk)
    if request.method == 'POST':
        positions.delete()
        return redirect('Dashboard')
    context = {'position_delete': positions}
    return render(request, 'position-delete.html', context)


