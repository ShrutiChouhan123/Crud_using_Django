from . import views
from django.urls import path
urlpatterns = [
    path('',views.index),
    path('adddata',views.adddata),
    path('updatedata',views.updatedata)
]