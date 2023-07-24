from django.urls import path

from purchases import views

urlpatterns = [
    path('', views.purchases_view, name='purchases-list')
]