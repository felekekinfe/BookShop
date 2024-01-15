from django_countries.fields import CountryField
from django import forms

PAYMENT_CHOICES=(
    ('Y','Yenepay'),
    ('P','Paypal')
)

class CheckoutForm(forms.Form):
    street_address=forms.CharField(max_length=100)
    house_address=forms.CharField(max_length=100)
    country=CountryField(blank_label=('select country'))
    zip_code=forms.CharField(max_length=100)
    same_billing_address=forms.BooleanField(widget=forms.CheckboxInput())
    save_info=forms.BooleanField(widget=forms.CheckboxInput())
    payment_option=forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)