from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(),
                              required=True)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message)
        send_mail(
                    'Contato Django E-commerce',
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER]
        )
