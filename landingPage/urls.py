from django.urls import path

from . import views

app_name = "landingPage"

urlpatterns = [
    path("", views.index, name="index"),
    path("coming-soon", views.coming_soon, name="coming-soon"),
    path("thank-you", views.thank_you, name="thank-you"),
]