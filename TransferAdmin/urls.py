from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from transferencias_app.views import (TransferenciaListCreate, ClienteListCreate, ClienteRetrieveUpdateDestroy,
                                      BeneficiarioListCreate, BeneficiarioRetrieveUpdateDestroy,
                                      TransferenciaRetrieveUpdateDestroy, UserCreate, TokenObtainPair)

schema_view = get_schema_view(
    openapi.Info(
        title="Transferencias API",
        default_version='v1',
        description="API para la gestión de transferencias.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-retrieve-update-destroy'),

    path('beneficiarios/', BeneficiarioListCreate.as_view(), name='beneficiario-list-create'),
    path('beneficiarios/<int:pk>/', BeneficiarioRetrieveUpdateDestroy.as_view(),
         name='beneficiario-retrieve-update-destroy'),

    path('transferencias/', TransferenciaListCreate.as_view(), name='transferencia-list-create'),
    path('transferencias/<uuid:pk>/', TransferenciaRetrieveUpdateDestroy.as_view(), name='transferencia-detail'),

    path('users/', UserCreate.as_view(), name='user-create'),

    path('token/', TokenObtainPair.as_view(), name='token_obtain_pair'),
]
