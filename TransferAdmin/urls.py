from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from transferencias_app.views import (TransferenciaListCreate, ClienteListCreate, ClienteRetrieveUpdateDestroy,
                                      BeneficiarioListCreate, BeneficiarioRetrieveUpdateDestroy,
                                      TransferenciaRetrieveUpdateDestroy, UserCreate, TokenObtainPair)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

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
