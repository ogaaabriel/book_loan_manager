from datetime import date
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages

from . import models, forms


class ListBookLoansView(LoginRequiredMixin, generic.ListView):
    model = models.Loan
    context_object_name = "loans"
    template_name = "book_loans/loans.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "all")
        context["search"] = self.request.GET.get("search", "")
        context["filter_form"] = forms.FilterLoansForm(
            q=context["q"], search=context["search"]
        )
        return context

    def get_queryset(self):
        q = self.request.GET.get("q", "lent")
        search = self.request.GET.get("search", "")
        queryset = models.Loan.objects.filter(
            returned=False, date_return__gte=date.today()
        )

        if q == "late":
            queryset = models.Loan.objects.filter(
                date_return__lt=date.today(), returned=False
            )
        elif q == "returned":
            queryset = models.Loan.objects.filter(returned=True)

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
    template_name = "form_page.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Novo livro"
        context["btn_value"] = "Adicionar"
        return context


class CreateBorrowerView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.BorrowerForm
    success_url = reverse_lazy("book_loans:create_loan")
    success_message = "Leitor registrado com sucesso"
    template_name = "form_page.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Novo leitor"
        context["btn_value"] = "Adicionar"
        return context


def toggle_returned(request, loan_id):
    loan = get_object_or_404(models.Loan, id=loan_id)

    if request.method == "POST":
        q = request.GET.get("q", "lent")
        loan.returned = not loan.returned
        loan.save()
        messages.success(request, "Status atualizado com sucesso")
        return redirect(reverse("book_loans:loans") + f"?q={q}")
    else:
        raise Http404
