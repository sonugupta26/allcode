from django.urls import path
from demoapp.views import contact, about, home, addresh

app_name = "demoapp"

urlpatterns = [
    path("home/", home, name = "home"),
    path("about/", about, name = "about"), 
    path("contact/", contact, name = "contact"),
    path("addresh/", addresh, name = "addresh"),
]