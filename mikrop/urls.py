from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hikayeler/', views.hikayeler, name='hikayeler'),
    path('hikayeler/<int:karakter_id>/', views.karakter_detay, name='karakter_detay'),
    path('forum/', views.forum, name='forum'),
    path('technicalSupport/', views.technicalSupport, name="technicalSupport"),
    path('sss/', views.sss, name="sss"),
]