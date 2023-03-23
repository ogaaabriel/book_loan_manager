from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from . import forms


class Signup(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("accounts:signup")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "form_page.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Cadastrar novo usuário"
        context["btn_value"] = "Cadastrar"
        return context
