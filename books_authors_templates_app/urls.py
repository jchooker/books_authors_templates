from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createBook', views.createBook),
    path('addAuthor', views.addAuthor),
    path('createAuthor', views.createAuthor),
    path('view-book/<int:id>', views.view_book),
    path('view-author/<int:id>', views.view_author),
    path('createRel/<int:id>', views.createRel)
]
