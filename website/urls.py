from django.contrib import admin
from django.urls import path
from .views import index,create,remove,update,login,logout

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("", index, name="home"),
    path("create/", create, name="create"),
    path("remove/<int:post_id>", remove, name="remove"),
    path("update/<int:post_id>", update, name="update"),

]
