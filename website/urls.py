from django.urls import path
from .views import home_site


urlpatterns = [
    path('', home_site, name='home_site')
]
