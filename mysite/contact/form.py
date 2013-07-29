from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    organization = forms.CharField(max_length=100)
    message = forms.CharField(widget = forms.Textarea(attrs={'rows':4, 'cols':15}))