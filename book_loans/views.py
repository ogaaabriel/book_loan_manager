from datetime import date
from django.views import generic

from . import models, forms


class ListBookLoansView(generic.ListView):
    model = models.Loan
    context_object_name = "loans"
    template_name = "book_loans/loans.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "all")
        context["filter_form"] = forms.FilterLoansForm(q=context["q"])
        return context

    def get_queryset(self):
        q = self.request.GET.get("q", "all")

        if q == "late":
            return models.Loan.objects.filter(date_return__lt=date.today())
        else:
            return models.Loan.objects.all()
