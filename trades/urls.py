from django.urls import path
from . import views

app_name = "trades"

urlpatterns = [
    path('stock_form', views.stock_form, name="stock_form"),
    path('stock_search', views.stock_search, name="stock_search")
]
