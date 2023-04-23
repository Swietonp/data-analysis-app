from django.urls import path
from . import views

app_name = 'data_analysis_app'

urlpatterns = [
    path('', views.main_page, name='namepage')
]
