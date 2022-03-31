from django.urls import include, path
from drf_yasg import openapi
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from .views import *
from drf_yasg.generators import OpenAPISchemaGenerator
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="RBT API",
        default_version='v1',
        description="RBT API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
    generator_class=BothHttpAndHttpsSchemaGenerator,
)

urlpatterns = []

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path('', schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'),
        path('redoc', schema_view.with_ui('redoc',
                                          cache_timeout=0), name='schema-redoc')
    ]

urlpatterns = urlpatterns + [
    path('', include('authentication.urls')),
    path('', include(router.urls))
]
