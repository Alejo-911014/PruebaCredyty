from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import User
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users:users')


class UserUpdate(UpdateView):
    model = User
    fields = ['Nombre','Apellido','Edad', 'Profesion','Perfil']
    template_name_suffix = '_update_form' 

    def get_success_url(self):
        return reverse_lazy('users:update', args=[self.object.id]) + '?ok'  

class UserCreate(CreateView): #
    model = User
    fields = ['Nombre','Apellido','Edad', 'Profesion','Perfil']
    success_url = reverse_lazy('users:users')

class UserListView(ListView):
    model = User # modelo


class UserDetailView(DetailView):
    model = User