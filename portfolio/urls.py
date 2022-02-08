from django.urls import re_path
from portfolio import views

app_name = "portfolio"

urlpatterns = [
     re_path(r'^categories/$',views.categoryList,name="portfolio-category-list"),
     re_path(r'categories/(?P<pk>[0-9]+)$',views.categoryDetail,name="portfolio-category-detail"),
     re_path(r'^projects/$',views.ProjectList,name="portfolio-post-list"),
     re_path(r'^projects/(?P<pk>[0-9]+)$',views.ProjectDetail,name="portfolio-post-detail"),
     re_path(r'^images/$',views.ImageList,name="portfolio-image-list"),
     re_path(r'^images/(?P<pk>[0-9]+)$',views.ImageDetail,name="portfolio-image-detail"),
]
