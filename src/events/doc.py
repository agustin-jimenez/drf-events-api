from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

DESCRIPTION = """
___

Event tracker REST API

*Developed and maintained by* **[Agustin Jimenez](https://bit.ly/agustin-back)**
"""

schema_view = get_schema_view(
    openapi.Info(
        title="Events",
        default_version='v1',
        description=DESCRIPTION,
        terms_of_service="NOT DEFINED",
        contact=openapi.Contact(email="agustin.j@zohomail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

redoc = schema_view.with_ui('redoc', cache_timeout=0)
swagger = schema_view.with_ui('swagger', cache_timeout=0)
json = schema_view.without_ui(cache_timeout=0)
