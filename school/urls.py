from django.contrib import admin
from django.urls import path
from student_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  # Set home page as the root URL
    path('home/',views.home),
    path('register/',views.register),
    path('existing/',views.existing),
    path('search/',views.search),
    path('dropout/', views.dropout),
]
