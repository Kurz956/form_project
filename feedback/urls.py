from django.urls import path
from .views import index, done

urlpatterns = [
    path('done', done),
    path('', index),
]