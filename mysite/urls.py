from django.urls import include, path

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include("client_app.urls")),
    # path("", include("app.urls")),
]
