from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["title", "author"], name="Unique book")
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"


class Borrower(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(
        max_length=11, unique=True, error_messages={"unique": "CPF já cadastrado"}
    )

    def __str__(self):
        return f"{self.name} - {self.cpf}"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    date_return = models.DateField(
        validators=[MinValueValidator(date.today(), "Data inválida")]
    )

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return f"{self.book} - {self.borrower}"
