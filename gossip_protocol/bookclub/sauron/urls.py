from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('requests/', views.RequestView.as_view()),
]
