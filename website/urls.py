from django.contrib import admin
from django.urls import path
from .views import index,create,remove,update

urlpatterns = [
    path("", index, name="home"),
    path("create/", create, name="create"),
    path("remove/<int:post_id>", remove, name="remove"),
    path("update/<int:post_id>", update, name="update"),
]
