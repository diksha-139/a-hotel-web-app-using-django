from django import forms
from .models import Registration
import datetime
from multiselectfield import MultiSelectFormField

class CustomerSignup(forms.Form):

    name = forms.CharField(label="Customer Name",widget=forms.TextInput(),required=True)
    phone = forms.CharField(widget=forms.NumberInput)
    address = forms.CharField(widget=forms.TextInput())
    time =forms.DateTimeField(label="Time of Arrival",initial=datetime.datetime.today)
    guests = forms.CharField(label="Number of Guests",widget=forms.NumberInput)
    orderList=[
        ('>Bacon wrapped wild gulf prawns','>Bacon wrapped wild gulf prawns'),
        ('Shawarma','Shawarma'),
        ('Kadahi Paneer','Kadahi Paneer'),
        ('Chicken Biryani','Chicken Biryani'),
        ('Special Thaali','Special Thaali'),
        ('Franky Roll','Franky Roll'),
        ('Lachcha Porotta','Lachcha Porotta'),
        ('chettinad chicken curry','chettinad chicken curry'),
        ('Egg Curry','Egg Curry'),
        ('Dal Makhani','Dal Makhani'),
        ('Aloo Matar Curry','Aloo Matar Curry'),
        
       
    ]
    orders = MultiSelectFormField(choices=orderList)

    password = forms.CharField(widget=forms.PasswordInput())

    confirm=forms.BooleanField()