import os

import openpyxl as px
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from ..form import SalesUpdateForm
from ..models import Sales


class SalesListView(ListView):
    model = Sales


class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesUpdateForm


class SalesDeleteView(DeleteView):
    model = Sales
    success_url = reverse_lazy('beginning:sales')


def create(request):
    file = os.path.join('beginning', 'static', 'sales.xlsx')
    work_book = px.load_workbook(file, data_only=True, read_only=True)
    sheet = work_book.active
    for row in sheet.iter_rows(min_row=2, max_row=13):
        Sales.objects.update_or_create(
            month=row[0].value,
            defaults={'amount': row[1].value}
        )
    work_book.close()
    return redirect('beginning:sales')
