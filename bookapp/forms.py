from django_countries.fields import CountryField
from django import forms
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES=(
    ('Y','Yenepay'),
    ('P','Paypal')
)

class CheckoutForm(forms.Form):
    street_address=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'street address'
    }))
    house_address=forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder':'house address'})) 
    country=CountryField(blank_label=('select country')).formfield(widget=CountrySelectWidget(attrs={

        'class':'custom-select d-block w-100'
    }))
    zip_code=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    same_billing_address=forms.BooleanField(widget=forms.CheckboxInput())
    save_info=forms.BooleanField(required=False)
    payment_option=forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)