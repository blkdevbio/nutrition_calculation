from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('form/',views.form,name='form'),
    path('post/<int:id>/edit',views.edit,name='edit'),
    path('post/<int:id>/update',views.update,name='update'),
    path('post/<int:id>/delete',views.delete,name='delete'),
    path('post/<int:id>/detail',views.detail,name='detail'),
]