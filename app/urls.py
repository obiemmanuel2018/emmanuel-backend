from django.urls import re_path
from app import views

app_name = "app"

urlpatterns = [
     re_path(r'^categories/$',views.categoryList,name="portfolio-category-list"),
     re_path(r'categories/(?P<pk>[0-9]+)$',views.categoryDetail,name="portfolio-category-detail"),
]
