
from django.urls import path
from . import views

urlpatterns = [

    path('', views.catalog, name = 'catalog'),
    path('<int:dress_id>/', views.catalog_detail, name = 'catalog_detail'),

]