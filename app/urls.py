from django.urls import path

from .views import landing_page, tenant_onboarding

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("onboarding", tenant_onboarding),
]
