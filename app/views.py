from django.shortcuts import redirect, render

from .forms import InstitutionForm
from .models import Client, Domain

# Create your views here.


def landing_page(request):
    return render(request, "landing.html")


def tenant_onboarding(request):
    if request.method == "POST":
        form = InstitutionForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # create client/tenant and domain objects
            tenant = Client(schema_name=data["name"], name=data["name"])
            tenant.save()
            domain = Domain(
                domain=f"{data['name']}.localhost", tenant=tenant, is_primary=True
            )
            domain.save()

            # create institution object
            institution = form.save()
            institution.domain = domain
            institution.save()

            # redirect to the sub-domain after save
            new_url = f"http://{domain.domain}:8000"
            return redirect(new_url)

    form = InstitutionForm()

    return render(request, "onboarding.html", {"form": form})
