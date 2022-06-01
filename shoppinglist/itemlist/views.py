from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class ItemListView(ListView):
	model = models.Item

class ItemDetailView(DetailView):
	model = models.Item

class ItemUpdateView(UpdateView):
	model = models.Item
	fields ="__all__"
	success_url = "/"

class ItemCreateView(CreateView):
	model = models.Item
	fields ="__all__"
	success_url = "/"

class ItemDeleteView(DeleteView):
	model = models.Item
	success_url = "/item/"
