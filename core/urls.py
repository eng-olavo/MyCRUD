from django.urls import path
from core import views


urlpatterns = [

    path('', views.index, name='index'),
    path('getView/',views.getView, name='getView'),
    path('postView/',views.postView, name='postView'),
    path('putView/',views.putView, name='putView'),
    path('deleteView/',views.deleteView, name='deleteView'),

    # path('CRUD_get', views.GetView, name='GetV'),
    # path('CRUD_post', views.GetPost, name='PostV'),
    # path('CRUD_put/<str:pk>/', views.GetPut, name='PutV'),
    # path('CRUD_delete/<str:pk>', views.GetDelete, name='DelV'),
]
