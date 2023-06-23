from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model

from . import forms

User = get_user_model()


class Signup(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("accounts:users")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "form_page.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Cadastrar novo usuário"
        context["btn_value"] = "Cadastrar"
        return context


class ListUsersView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = "users"
    template_name = "accounts/users.html"
    paginate_by = 10
