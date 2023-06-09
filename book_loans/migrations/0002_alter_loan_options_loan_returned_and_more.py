# Generated by Django 4.1.7 on 2023-03-20 21:37

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_loans", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="loan",
            options={"ordering": ["date_return"]},
        ),
        migrations.AddField(
            model_name="loan",
            name="returned",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="loan",
            name="date_return",
            field=models.DateField(
                validators=[
                    django.core.validators.MinValueValidator(
                        datetime.date(2023, 3, 20), "Data inválida"
                    )
                ]
            ),
        ),
    ]
