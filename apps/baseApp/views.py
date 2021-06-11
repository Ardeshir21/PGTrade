from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils import translation
from . import models, forms
from django.conf import settings
from django.contrib import messages


# Here is the Extra Context ditionary which is used in get_context_data of Views classes
def get_extra_context():
    extraContext = {
        'DEBUG_VALUE': settings.DEBUG,
        'from_python': _('SOMETHING'),
        'current_language': translation.get_language(),
        }
    return extraContext

# Index View
class IndexView(generic.edit.FormView):

    success_url = reverse_lazy('baseApp:index')
    form_class = forms.ContactForm

    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/RTL/index.html"]
        # LTR languages
        else:
            return ["baseApp/LTR/index.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        return context

    def form_valid(self, form):
        # Success Message
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            messages.add_message(self.request, messages.SUCCESS, 'پیام شما با موفقیت ارسال شد.')
        # LTR languages
        else:
            messages.add_message(self.request, messages.SUCCESS, 'Your message has been successfully sent.')

        # This method is called when valid form data has been POSTed.
        # current_url = resolve(request.path_info).url_name
        form.send_email(current_url=self.request.build_absolute_uri())
        return super().form_valid(form)
