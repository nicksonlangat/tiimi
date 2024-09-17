from django.shortcuts import render

# Create your views here.


def tenant_onboarding(request):
    return render(request, "onboarding.html")
