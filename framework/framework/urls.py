from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from strawberry.django.views import GraphQLView
from framework.graphql.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=schema)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('api/', include(urlpatterns))
]