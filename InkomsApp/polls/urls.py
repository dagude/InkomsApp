from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="index"),
    path("<int:question_id>/", views.results, name="index"),
    path("<int:question_id>/", views.vote, name="index")
]