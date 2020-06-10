from django.urls import path
from .views import UserListView, UserDetailView, UserCreate, UserUpdate, UserDelete

users_patterns = ([
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/<slug:slug>/', UserDetailView.as_view(), name='user'),
    path('create/', UserCreate.as_view(), name='create'), 
    path('update/<int:pk>', UserUpdate.as_view(), name ='update'), 
    path('delete/<int:pk>', UserDelete.as_view(), name='delete'),
], 'users')