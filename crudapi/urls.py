from django.urls import path
from .views import *
urlpatterns = [
    path("", ActorsList.as_view(), name='actors'),
    path("<int:actor_id>/", ActorsDetail.as_view(), name='actors'),
    path("<int:pk>/delete/", DeleteView.as_view(), name='actors'),
    path("update/<int:actor_id>/", Update.as_view(), name='actors')


]