from django import forms
from django.forms.widgets import Widget
from django_countries.fields import CountryField
from pkg_resources import require
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St'
    }))
    department_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "Apartment or suite"
    }))
    country = CountryField(blank_label='(Select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
            'id': 'country'
        }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)
