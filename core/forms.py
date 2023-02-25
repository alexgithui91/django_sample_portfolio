from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    email_address = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
