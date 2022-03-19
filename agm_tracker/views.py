from django.shortcuts import render, redirect
from .models import agm
from .forms import agmform


def agm_tracker(request):
    agm_data = agm.objects.all()

    context = {'agms': agm_data}

    return render(request, 'agm_report.html', context)


def new_agm(request):
    AGMs = agmform

    if request.method == 'POST':
        AGMs = agmform(request.POST)
        if AGMs.is_valid():
            AGMs.save()
            return redirect('agm_tracker')

    context = {'AGM_Add': AGMs}
    return render(request, "new_agm.html", context)


def agm_delete(request, pk):
    AGMs = agm.objects.get(codename=pk)
    if request.method == 'POST':
        AGMs.delete()
        return redirect('agm_tracker')
    context = {'AGM_Delete': AGMs}
    return render(request, 'agm_delete.html', context)

