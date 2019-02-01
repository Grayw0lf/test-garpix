from django.urls import path
from .views import login
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Ticket API')

app_name = 'ticket'
urlpatterns = [
    path('docs/', schema_view, name='api_docs'),
    path('login/', login, name='login'),
]
