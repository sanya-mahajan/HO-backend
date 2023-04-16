from django.urls import path

from learn import views

app_name = "learn"

urlpatterns = [
    path("search/", views.SearchMedInfo, name="search"),
    
]