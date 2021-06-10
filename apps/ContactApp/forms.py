from django import forms

class ContactForm(forms.Form):
    nameContactForm = forms.CharField(label='Name', required=True)
    emailContactForm = forms.EmailField(label='Email', required=True)
    contentContactForm = forms.CharField(label='Content', widget=forms.Textarea, required=True)