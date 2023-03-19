from django import forms


class FilterLoansForm(forms.Form):
    CHOICES = (
        ("all", "Todos"),
        ("late", "Em atraso"),
    )
    q = forms.ChoiceField(choices=CHOICES, label="")

    def __init__(self, *args, **kwargs):
        self.base_fields["q"].initial = kwargs.pop("q")
        super(FilterLoansForm, self).__init__(*args, **kwargs)
