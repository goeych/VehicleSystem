from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.forms import widgets



from .models import Vehicleexpense,Dailyexpense,Customer



class DateInput(forms.DateInput):
    input_type = 'date'

class ExpensesForm(forms.ModelForm):

    date_created = forms.DateField(widget=DateInput)
    class Meta:
        model = Vehicleexpense
        fields= ['vehicle','name','price','category','mileage','description','note','date_created']
        #exclude=['customer ']
        

    def __init__(self,*args,**kwargs):
        super(ExpensesForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Product name...'})
        self.fields['price'].widget.attrs.update({'class':'form-control','placeholder':'Price...'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Choice catogory...'})
        self.fields['mileage'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mileage...'})
        self.fields['description'].widget.attrs.update({'class':'form-control','placeholder':'Description...'})
        self.fields['note'].widget.attrs.update({'class':'form-control','placeholder':'Note ...'})
        self.fields['date_created'].widget.attrs.update({'class':'form-control','placeholder':'Date...'})


class DailyexpensesForm(forms.ModelForm):

    date_created = forms.DateField(widget=DateInput)
    class Meta:
        model = Dailyexpense
        fields= ['name','price','category','description','note','date_created']
        #exclude=['customer ']
        

    def __init__(self,*args,**kwargs):
        super(DailyexpensesForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Product name...'})
        self.fields['price'].widget.attrs.update({'class':'form-control','placeholder':'Price...'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Choice catogory...'})
        self.fields['description'].widget.attrs.update({'class':'form-control','placeholder':'Description...'})
        self.fields['note'].widget.attrs.update({'class':'form-control','placeholder':'Note ...'})
        self.fields['date_created'].widget.attrs.update({'class':'form-control','placeholder':'Date...'})
