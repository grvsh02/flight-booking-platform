from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from framework.graphql.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(schema=schema,graphiql=True))),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('api/', include(urlpatterns))
]