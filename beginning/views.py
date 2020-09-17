import openpyxl as px
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from .form import SalesUpdateForm
from .models import Sales


def create(request):
    wb = px.load_workbook('beginning/templates/sales.xlsx')
    ws = wb.active
    for sale in ws:

        if sale[0].row == 1:
            pass
        else:
            if sale[0].value is None:
                break
            print(sale[0].value, ",", sale[1].value)
            sale, created = Sales.objects.update_or_create(
                month=sale[0].value,
                defaults={'amount': sale[1].value}
            )
    return redirect('/beginning')


class SalesListView(ListView):
    model = Sales


class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesUpdateForm


class SalesDeleteView(DeleteView):
    model = Sales
    success_url = reverse_lazy('beginning:sales')
