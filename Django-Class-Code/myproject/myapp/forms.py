from django import forms

class InputForm1(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
    
    
    
from django import forms   
class InputForm2(forms.Form):
    name  = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    website = forms.URLField(required=False)
    agree = forms.BooleanField(label="I agree to the terms and conditions")