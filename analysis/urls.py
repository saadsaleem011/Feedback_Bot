from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('api/top_unit/', views.top_unit, name='top_unit'),
    path('api/unit_price_history/', views.unit_price_history, name='unit_price_history'),
    path('api/building_deals/', views.building_deals, name='building_deals'),
]
