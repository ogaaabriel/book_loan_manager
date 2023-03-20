from django.urls import path

from . import views

app_name = "book_loans"

urlpatterns = [
    path("emprestimos/", views.ListBookLoansView.as_view(), name="loans"),
    path("novo_emprestimo/", views.CreateBookLoansView.as_view(), name="create_loan"),
    path("novo_livro/", views.CreateBookView.as_view(), name="create_book"),
    path("novo_leitor/", views.CreateBorrowerView.as_view(), name="create_borrower"),
]
