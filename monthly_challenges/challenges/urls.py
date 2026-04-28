from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.num_redirect),
    path("<str:month>", views.mon_challenge, name="month-challenge")
]