from django.shortcuts import render, redirect

from .forms import PersonsForm
from django.urls import reverse_lazy
from .models import Training
# Create your views here.


def index(request):
    trainings = Training.objects.order_by('training_date').all()
    if request.method != 'POST':
        form = PersonsForm()
    else:
        #przekazano dane za pomoca zadania POST, ttrzeba je przetworzyc
        form = PersonsForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('sgapp:index')

    context = {'trainings': trainings, 'form': form}
    return render(request, 'sgapp/index.html', context)