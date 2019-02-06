from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .views import TicketViewSet, UserStatisticViewSet


router = DefaultRouter()
router.register('tickets', TicketViewSet, basename='tickets')
router.register('statistic', UserStatisticViewSet)

schema_view = get_swagger_view(title='Ticket API')

app_name = 'ticket'
urlpatterns = [
    path('', include(router.urls)),
    path('docs-ticket/', schema_view, name='docs_ticket'),
]
