from django.urls import path

from . import views

app_name = "book_loans"

urlpatterns = [
    path("", views.ListBookLoansView.as_view(), name="loans"),
    path("novo_emprestimo/", views.CreateBookLoansView.as_view(), name="create_loan"),
    path("livros/", views.ListBooksView.as_view(), name="books"),
    path("novo_livro/", views.CreateBookView.as_view(), name="create_book"),
    path("leitores/", views.ListBorrowersView.as_view(), name="borrowers"),
    path("novo_leitor/", views.CreateBorrowerView.as_view(), name="create_borrower"),
    path(
        "atualizar_status/<int:loan_id>/", views.toggle_returned, name="toggle_returned"
    ),
]
