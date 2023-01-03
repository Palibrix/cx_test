from django import forms

from orders.models import Customer


class CustomerForm(forms.Form):

    name = forms.CharField(label='Name', max_length=100)
    profile_picture = forms.ImageField()


class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
