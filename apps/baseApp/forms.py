from django import forms
from django.core.mail import send_mail
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Invisible
from django.utils.translation import gettext as _



class ContactForm(forms.Form):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    name = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': _('Your Name*'),
                                                            'size': '40'})
                            )
    message = forms.CharField(max_length=2500,
                                widget=forms.Textarea(attrs={'placeholder': _('Your Message*'),
                                                                'rows': '10',
                                                                'style':'width:100%;'}))
    client_email = forms.EmailField(
                                widget=forms.EmailInput(attrs={'placeholder': _('Your Email*'),
                                                                'size': '40'})
                                )
    subject = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': _('Subject*'),
                                                            'size': '40'})
                            )

    def send_email(self, current_url):
        name = self.cleaned_data['name']
        message = self.cleaned_data['message']
        client_email = self.cleaned_data['client_email']
        client_subject = self.cleaned_data['subject']
        recipients = ['contact@lavinomood.com', client_email]
        mail_subject = 'LaVino Group Received Your Message - {}'.format(client_subject)

        message_edited = '''Dear {},

Many thanks for contacting us.
We have successfully received your below message. Our team will contact you shortly.

___________________________________________

{}
eMail Address: {}

{}

___________________________________________
Kind Regards,
LaVino Mood Team
https://www.lavinomood.com
'''
        message_edited = message_edited.format(name, name, client_email, message)
        send_mail(mail_subject, message_edited, 'contact@lavinomood.com', recipients)
        pass
