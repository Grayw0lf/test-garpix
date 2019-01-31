from django.urls import path
from .views import login
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Ticket API')

app_name = 'ticket'
urlpatterns = [
    path('docs/', schema_view),
    path('login/', login),
]
