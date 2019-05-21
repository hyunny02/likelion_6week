from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bulletin

class BulletinListView(ListView):
    model = Bulletin

class BulletinDetailView(DetailView):
    model = Bulletin

class BulletinCreateView(CreateView):
    model = Bulletin
    fields = ['title', 'content']
    success_url = reverse_lazy('bulletin:list')
    template_name_suffix = '_create'

class BulletinUpdateView(UpdateView):
    model = Bulletin
    fields = ['title', 'content']
    template_name_suffix = '_update'

class BulletinDeleteView(DeleteView):
    model = Bulletin
    success_url = reverse_lazy('bulletin:list')

