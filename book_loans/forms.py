from django import forms
from django.core.exceptions import ValidationError

from . import models


class FilterLoansForm(forms.Form):
    CHOICES = (
        ("lent", "Emprestado"),
        ("late", "Em atraso"),
        ("returned", "Devolvido"),
    )
    search = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Buscar empréstimo..."}),
    )
    q = forms.ChoiceField(choices=CHOICES, label="")

    def __init__(self, *args, **kwargs):
        self.base_fields["q"].initial = kwargs.pop("q")
        self.base_fields["search"].initial = kwargs.pop("search")
        super(FilterLoansForm, self).__init__(*args, **kwargs)


class BookLoanForm(forms.ModelForm):
    class Meta:
        model = models.Loan
        fields = ["book", "borrower", "date_return"]
        labels = {
            "book": "Livro",
            "borrower": "Leitor",
            "date_return": "Data de devolução",
        }
        widgets = {"date_return": forms.DateInput(attrs={"type": "date"})}


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ["title", "author"]
        labels = {
            "title": "Título",
            "author": "Autor",
        }


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = models.Borrower
        fields = ["name", "cpf"]
        labels = {
            "name": "Nome",
            "cpf": "CPF",
        }
