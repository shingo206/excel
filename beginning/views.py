from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .form import LogForm
from .models import Log


def index(request):
    return render(request, 'beginning/index.html', context={'form': 'form'})


class LogListView(ListView):
    model = Log


class LogCreateView(CreateView):
    model = Log
    form_class = LogForm
    success_url = reverse_lazy('beginning:logs')


class LogUpdateView(UpdateView):
    model = Log
    form_class = LogForm
    success_url = reverse_lazy('beginning:logs')


class LogDeleteView(DeleteView):
    model = Log
    success_url = reverse_lazy('beginning:logs')
