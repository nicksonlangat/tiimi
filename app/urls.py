from django.urls import path

from .views import tenant_onboarding

urlpatterns = [
    path("onboarding", tenant_onboarding),
]
