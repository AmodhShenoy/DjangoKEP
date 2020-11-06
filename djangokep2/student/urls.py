from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.listView, name='listView'),
    path('detail/<id>',views.detailView, name='detailView'),
    path('add/',views.addView, name='addView'),
]