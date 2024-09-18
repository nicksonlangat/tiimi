from django.forms import ModelForm

from .models import Institution


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = [
            "name",
            "email",
            "phone_number",
            "domain",
            "county",
            "sub_county",
            "ward",
        ]
