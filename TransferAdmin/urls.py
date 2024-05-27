from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

from transferencias_app.views import (TransferenciaListCreate,
                                      TransferenciaRetrieveUpdateDestroy, UserCreate, TokenObtainPair)

schema_view = get_schema_view(
    openapi.Info(
        title="TransferAdmin API",
        default_version='v1', ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('transferencias/', TransferenciaListCreate.as_view(), name='transferencia-list-create'),
    path('transferencias/<uuid:pk>/', TransferenciaRetrieveUpdateDestroy.as_view(), name='transferencia-detail'),
    path('users/', UserCreate.as_view(), name='user-create'),
    path('token/', TokenObtainPair.as_view(), name='token_obtain_pair'),
]
