from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("detect_color/", views.detect_color, name="detect_color"),
    # path("upload_image/", views.upload_image, name="upload_image"),
]
