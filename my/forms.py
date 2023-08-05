from django import forms
from django.core import validators
from my.models import studentdata

def email_validate(value):
    if studentdata.objects.filter(email=value).exists():
        raise forms.ValidationError("Email Already Exists")
    

def contain(string,list):
    result=True
    l=[i for i in string]
    for j in l:
        if j in list:
            result=False
            break
        else:
            pass
    return result
    
symbols=['#','$','!','@','%','&','*','(',')']
numbers=list(map(str,list(range(10))))
underscore=['_','-']
def name_validae(value):
    if contain(value,symbols)==False or contain(value,numbers)==False or contain(value,underscore)==False:
        raise forms.ValidationError('*name not include special symbols or numbers')

class addrecord(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","name":"name"}),required=True,validators=[name_validae,validators.MaxLengthValidator(20,message="*Name should be less than 20 characters")])
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","name":"email"}),validators=[email_validate],required=True)

