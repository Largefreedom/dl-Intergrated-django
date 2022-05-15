from django.urls import path

from . import views

urlpatterns = [
    path('upload-image',views.paddle_image_upload)

]