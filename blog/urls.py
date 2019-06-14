from django.urls import path 
from . import views

urlpatterns = [
    path('',views.allblogs,name='allblogs'),
    path('<int:blogs_id>/',views.detailpage,name='detailpage'),
]
