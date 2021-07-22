from django.urls import include
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from events.doc import redoc, swagger, json

urlpatterns = [
    # Doc
    path('', redoc, name='doc-redoc'),
    path('doc/', swagger, name='doc-swagger'),
    re_path(r'^atua(?P<format>\.json)$', json, name='schema-json'),
    # API
    path('api/', include('api.urls'), name='api'),
]

