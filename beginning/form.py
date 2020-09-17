from django.forms import ModelForm

from .models import Sales


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['month', 'amount']


class SalesUpdateForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['amount']
