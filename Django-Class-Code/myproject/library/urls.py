from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('update/<int:id>/', views.update_book, name='update_book'),
]
