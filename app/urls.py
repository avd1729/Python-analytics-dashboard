from django.urls import path
from app import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('report/retail', views.ecommerce_report_page, name='retail_report'),
    path('report/marketing', views.marketing_report_page, name='marketing_report'),
]