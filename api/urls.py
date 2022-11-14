from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('<int:a>/<int:b>', views.SummatorView.as_view(), name="summator"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]
