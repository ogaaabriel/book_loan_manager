from datetime import date
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms


class ListBookLoansView(LoginRequiredMixin, generic.ListView):
    model = models.Loan
    context_object_name = "loans"
    template_name = "book_loans/loans.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "all")
        context["search"] = self.request.GET.get("search", "")
        context["filter_form"] = forms.FilterLoansForm(
            q=context["q"], search=context["search"]
        )
        return context

    def get_queryset(self):
        q = self.request.GET.get("q", "all")
        search = self.request.GET.get("search", "")
        queryset = models.Loan.objects.all()

        if q == "late":
            queryset = queryset.filter(date_return__lt=date.today())

        if search:
            queryset = queryset.filter(
                Q(book__title__istartswith=search)
                | Q(book__author__istartswith=search)
                | Q(borrower__name__istartswith=search)
                | Q(borrower__cpf__iexact=search)
            )

        return queryset


class CreateBookLoansView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.BookLoanForm
    success_url = reverse_lazy("book_loans:loans")
    success_message = "Empréstimo registrado com sucesso"
    template_name = "book_loans/create_loan.html"
    context_object_name = "form"


class CreateBookView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.BookForm
    success_url = reverse_lazy("book_loans:create_loan")
    success_message = "Livro registrado com sucesso"
    template_name = "form.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Adicionar um novo livro"
        context["btn_value"] = "Adicionar"
        return context


class CreateBorrowerView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.BorrowerForm
    success_url = reverse_lazy("book_loans:create_loan")
    success_message = "Leitor registrado com sucesso"
    template_name = "form.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Adicionar um novo leitor"
        context["btn_value"] = "Adicionar"
        return context
