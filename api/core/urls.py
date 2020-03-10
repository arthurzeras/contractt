from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core import views

app_name = 'core'

routers = DefaultRouter()
routers.register(
    'health-check', views.HealthCheckViewSet, base_name='core_health_check'
)

routers.register(
    'candidatos', views.UserViewSet, base_name='core_user'
)

routers.register(
    'progress_detail', views.ProgressDetailViewSet, base_name='core_progress_detail'
)

urlpatterns = [path('', include(routers.urls))]
