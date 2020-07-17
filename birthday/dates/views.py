from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Birthdays
from .forms import *

# Create your views here.

def index(request):
    birthdays = Birthdays.objects.all()
    form = BirthdaysForm()
    if request.method == 'POST':
        form = BirthdaysForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'birthdays':birthdays,
        'form':form
    }
    return render(request, 'dates/list.html', context)
