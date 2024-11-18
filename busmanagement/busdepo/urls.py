from django.urls import path
from .import views


urlpatterns = [


    path('',views.bus_list,name='bus_list'),
    path('driver/', views.driver, name='driver'), 
    path('add',views.bus_add,name='add'),
    path('delete/<int:pk>/',views.bus_delete, name='bus_delete'),
    path('update/<int:pk>/', views.bus_update, name='bus_update'),








]