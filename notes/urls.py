# /notekeeper/notes/urls.py

from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.NoteUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='delete'),
    path('archive/<int:pk>/', views.archive_note, name='archive'),
]