from django.utils.translation import activate, gettext_lazy as _
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import get_language

def switch_language(request, lang: str):
    activate(lang)
    current_language = get_language()
    request.session['current_language'] = current_language
    messages.success(request, _('Language changed'))
    return redirect('home')