from django.urls import path

from . import views

app_name = "book_loans"

urlpatterns = [
    path("emprestimos/", views.ListBookLoansView.as_view(), name="loans")
]
