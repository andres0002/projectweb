from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from apps.ContactApp.forms import ContactForm

# Create your views here.

class Contact(View):
    template_name = 'ContactApp/Contact.html'
    forms_class = ContactForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'contactForm': self.forms_class})

    def post(self, request, *args, **kwargs):
        forms_class = ContactForm(request.POST)
        if(forms_class.is_valid()):
            nameContactForm = request.POST.get("nameContactForm")
            emailContactForm = request.POST.get("emailContactForm")
            contentContactForm = request.POST.get("contentContactForm")

            email = EmailMessage("Message from the ContactApp",
            "The user with Name: {} with the diretion of Email: {} escribe lo siguiente:\n\n {}".format(nameContactForm, emailContactForm, contentContactForm),
            "",["frivandres038@gmail.com"], reply_to=[emailContactForm])
            try:
                email.send()
                return redirect('/Contact/?is_valid')
            except:
                return redirect('/Contact/?not_is_valid')
        return render(request, self.template_name, {'contactForm': self.forms_class})